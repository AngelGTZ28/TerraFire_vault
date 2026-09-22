---
title: "Mapa de Oportunidades, Brechas y Gestión de Riesgos"
subject: "Data Science"
code: "LITD9A"
authors:
  - "Angel Emilio Gutierrez Lozano (4341)"
  - "Emiliano Betanzos Valtierra (4795)"
advisor: "Dr. Sergio Valadez Godínez"
tags:
  - gap-analysis
  - risk-matrix
  - data-quality
  - data-science
---

# 🛡️ Mapa de Oportunidades, Brechas y Gestión de Riesgos

---

## 1. Mapa Integral de Oportunidad de Datos

![[assets/comprehensive-data-opportunity-map.png]]
*Figura 1: Trazabilidad Extremo a Extremo de TERRA-FIRE (Sección 7 DOM).*

La arquitectura asegura una trazabilidad ininterrumpida:
1. **Problema Central:** Desfase temporal de combate reactivo y ceguera de datos de las brigadas en terreno montañoso.
2. **Actores Involucrados:** Protección Civil, Jefaturas CONAFOR y Brigadas Ejidales / Voluntarias.
3. **Decisiones Tácticas (48–72h):** Pre-posicionamiento de activos, moratorias de quema y selección de rutas seguras.
4. **Necesidades de Información:** Humedad viva del follaje (LFMC a 10m), Déficit de Presión de Vapor y teselas vectoriales sin red.
5. **Fuentes Abiertas:** Copernicus Sentinel-2/1, ECMWF ERA5-Land, GLO-30 DEM, NASA FIRMS y CONAFOR.
6. **Matriz de Salida:** Vóxeles tabulares métricos en formato Parquet listos para entrenamiento y predicción.

---

## 2. Informe de Análisis de Brechas Técnicas

![[assets/gap-analysis-report.png]]
*Figura 2: Brechas Identificadas y Estrategias de Mitigación por Software (Sección 8 DOM).*

| Dominio de Información | Estado Operativo Requerido | Estado Disponible Actual | Brecha Identificada | Estrategia de Mitigación por Software |
| :--- | :--- | :--- | :--- | :--- |
| **Humedad In-Situ de Combustible** | Red continua de sensores de humedad en hojas en montes de México. | Estaciones muy dispersas (<1 por cada 2,500 km² en sierras). | **Brecha de Calibración** | Ecuaciones biofísicas empíricas que vinculan NDMI con LFMC ($R^2 > 0.82$) validadas en bosques de pino-encino. |
| **Cobertura Satelital Óptica** | Observación constante de reflectancia cada 5 días sin interrupción. | Nubosidad densa frecuente en periodos de transición a lluvias. | **Brecha de Latencia Óptica** | Fusión con radar SAR Sentinel-1 C-Band (penetra nubes) y splines matemáticos de decaimiento con VPD. |
| **Micro-Meteorología** | Resolución espacial fina (30 m) que capture inversiones térmicas en cañadas. | Reanálisis en cuadrícula tosca de ~9 km ($0.1^\circ$) de ERA5-Land. | **Brecha de Escala Espacial** | Downscaling topográfico aplicando gradiente adiabático ($-6.5^\circ C/km$) sobre curvas de nivel del DEM GLO-30. |
| **Etiquetas de Incendios Históricos** | Marcas de tiempo exactas de inicio y polígonos delimitados por GPS. | CONAFOR registra la fecha en que se reportó; coordenadas de un solo punto. | **Brecha de Fidelidad de Etiquetas** | Cruce de registros con detecciones térmicas orbitales de NASA FIRMS (VIIRS 375m) y reconstrucción dNBR. |

---

## 3. Matriz de Riesgos de Adquisición y Machine Learning

![[assets/data-risk-matrix.png]]
*Figura 3: Evaluación Sistemática de Riesgos y Contramedidas Técnicas (Sección 9 DOM).*

| ID Riesgo | Evento y Causa Raíz | Severidad | Probabilidad | Nivel de Riesgo | Impacto Operativo y Analítico | Protocolo y Contramedida de Ingeniería |
| :---: | :--- | :---: | :---: | :---: | :--- | :--- |
| **R-01** | **Desbalance Extremo de Clases** <br> Ignición real $<0.05\%$ de vóxeles. | **Alta** | **Alta** | `CRÍTICO` 🔴 | El modelo logra 99.95% de exactitud ingenua prediciendo siempre "Sin Fuego", fallando en detectar el 100% de los incendios. | Descartar métrica de exactitud (*accuracy*); evaluar con **PR-AUC**; aplicar `scale_pos_weight` en XGBoost y submuestreo espacial de ceros. |
| **R-02** | **Oclusión por Nubosidad** <br> Frentes nubosos en estiaje tardío. | **Alta** | **Media** | `ALTO` 🟠 | Pérdida de bandas ópticas en momentos críticos, dejando el NDMI sin actualizar. | Fusión con radar SAR Sentinel-1 (retrodispersión C-Band) y fallback temporal a modelo puramente meteorológico. |
| **R-03** | **Fuga Espacial (*Spatial Leakage*)** <br> Validación cruzada k-fold aleatoria. | **Alta** | **Alta** | `ALTO` 🟠 | Métricas de precisión artificialmente optimistas que colapsan al llevar el modelo a sierras no vistas. | Implementar estrictamente **Blocked Spatial Cross-Validation** y validación por regiones excluidas (*Leave-One-Region-Out*). |
| **R-04** | **Saturación de Memoria en Celulares** <br> Teléfonos Android de gama baja. | **Alta** | **Media** | `ALTO` 🟠 | Pestañas del navegador colapsan en campo al parsear pesados archivos GeoJSON. | Comprimir geometrías en teselas vectoriales Mapbox (`.pbf`); límite estricto de <15 MB por zona de descarga. |
| **R-05** | **Ruido y Desfase en Bitácoras CONAFOR** <br> Fechas reportadas vs reales. | **Media** | **Media** | `MEDIO` 🟡 | Fuga temporal de datos y etiquetado erróneo de polígonos. | Anclar la estampa de tiempo al primer píxel térmico de NASA FIRMS y validar daño con dNBR post-fuego. |
| **R-06** | **Cuotas y Límites de APIs Externas** <br> Bloqueos de CDS o Copernicus. | **Media** | **Baja** | `MEDIO` 🟡 | Retraso en la descarga del lote diario a las 02:00 UTC. | Espejos en la nube (AWS Open Data / Planetary Computer); caché rodante de 72h y fallback a API Open-Meteo. |

---
*Notas vinculadas:* [[04 - Feature Taxonomy & Prioritization]] | [[06 - Dataset Specification & Recommendations]] | [[Offline-First Edge Architecture]]
