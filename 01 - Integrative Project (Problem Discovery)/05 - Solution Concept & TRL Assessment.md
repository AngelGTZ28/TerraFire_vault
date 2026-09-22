---
title: "Concepto de Solución TERRA-FIRE y Evaluación TRL 1-2"
subject: "Integrative Project III"
code: "LITD9A"
authors:
  - "Angel Emilio Gutierrez Lozano (4341)"
  - "Emiliano Betanzos Valtierra (4795)"
advisor: "Dr. Sergio Valadez Godínez"
tags:
  - solution-concept
  - trl-assessment
  - feasibility
  - integrative-project
---

# 🚀 Concepto de Solución TERRA-FIRE y Evaluación TRL 1-2

---

## 1. Documento de Concepto de Solución Inicial (TERRA-FIRE)

- **Nombre de la Solución:** **TERRA-FIRE** *(Plataforma de Inteligencia Predictiva y Cartografía Táctica Forestal)*.
- **Propósito Central:** Cerrar la brecha histórica entre los datos satelitales globales de observación terrestre y las brigadas comunitarias desconectadas en campo. Pronostica el agotamiento de humedad vegetal viva y el riesgo microclimático de ignición con **48 a 72 horas de anticipación a una resolución de 10 a 20 metros**, transformando el combate reactivo en prevención táctica.
- **Usuarios Destinatarios:**
  1. *Líderes de Brigadas Comunitarias y Ejidatarios:* Alertas semafóricas offline en dispositivos móviles para programar quemas agrícolas seguras.
  2. *Jefes Operativos de CONAFOR y Protección Civil:* Cartografía predictiva 72h para pre-despliegue estratégico de pipas y cuadrillas.
  3. *Técnicos Forestales y Analistas de Riesgo:* Modelos explicables (SHAP) y capas de combustible vivas para sustentar planes de manejo.
- **Beneficios Esperados:**
  - *Anticipación Real:* Mitigación previa de 3 días en lugar de reaccionar horas después de la columna de humo.
  - *Precisión Micro-Topográfica:* Detección de desecación en cañadas y laderas específicas gracias a vóxeles de 10–20 m de Sentinel-2.
  - *Continuidad Operativa Desconectada:* Funcionamiento ininterrumpido en la sierra profunda sin depender de red celular.
  - *Preservación de Vidas:* Eliminación de atrapamientos en cañadas gracias a rutas de escape claras.
- **Tecnologías Disruptivas Convergentes:**
  - Ingesta satelital automatizada (Copernicus Sentinel-2 MSI y Sentinel-1 SAR C-band).
  - Inteligencia artificial supervisada explicable (XGBoost + TreeSHAP).
  - Aplicación web progresiva offline-first (PWA + teselas MapLibre `.pbf` + SQLite/WASM).

---

## 2. Evaluación de Madurez Tecnológica (TRL 1 a TRL 2)

> [!note] Definición del Nivel TRL 1-2
> - **TRL 1 (Principios Básicos Observados):** Validación matemática y biofísica de que el índice NDMI se correlaciona fuertemente ($R^2 > 0.82$) con el contenido de humedad de combustibles vivos (LFMC), y que el Déficit de Presión de Vapor (VPD) gobierna la facilidad de ignición.
> - **TRL 2 (Concepto Tecnológico Formulado):** Se ha diseñado la arquitectura técnica completa, clasificado las fuentes de datos, establecido el esquema de dataset Parquet y definido el flujo operativo del sistema.

### Revisión de Literatura Científica de Respaldo:
1. *Jain et al. (2020):* Validación del rendimiento superior de algoritmos de árboles de decisión aumentados por gradiente (XGBoost) en cartografía de peligro de incendios sobre métodos clásicos.
2. *Chuvieco et al. (2020):* Demostración de que la combinación de bandas de infrarrojo cercano (NIR - B8) e infrarrojo de onda corta (SWIR - B11/B12) permite estimar con precisión el contenido de humedad del follaje vivo (LFMC).
3. *Seager et al. (2015):* Evidencia del Déficit de Presión de Vapor (VPD) como el principal motor termodinámico de desecación de biomasa y propagación extrema del fuego.

---

## 3. Reflexión de Factibilidad Técnica

| Aspecto | Evaluación Técnica | Estrategia de Mitigación |
| :--- | :--- | :--- |
| **Fortalezas Clave** | Cero costo de inversión en hardware (Zero CapEx); aprovechamiento de APIs abiertas y libres de la Agencia Espacial Europea (ESA) y ECMWF; escalabilidad algorítmica nacional. | No se depende de financiamiento de hardware municipal. |
| **Limitaciones Actuales** | Cobertura nubosa densa que obstruye la reflectancia óptica de Sentinel-2 durante la transición a lluvias. | Fusión temporal con radar de apertura sintética (Sentinel-1 SAR C-Band) y splines de decaimiento con VPD. |
| **Supuestos Centrales** | Disponibilidad continua y gratuita del catálogo de datos de Copernicus y Planetary Computer; adopción comunitaria de las recomendaciones semafóricas. | Creación de réplicas de datos y diseño de interfaces sin texto complejo para campesinos. |
| **Factores de Evolución** | Transición en TRL 3-4 hacia prototipado funcional del pipeline ETL en Python y empaquetado de la PWA. | Ejecución de pruebas piloto en una microcuenca con brigadas locales de CONAFOR. |

---

## 4. Conclusión del Problem Discovery Lab

El laboratorio de descubrimiento del problema demostró con evidencia documental y análisis de usuarios que **el principal cuello de botella del combate de incendios en México no es la falta de valentía de los brigadistas ni la carencia de agua, sino la asimetría y el retraso en la información**. TERRA-FIRE sienta las bases conceptuales y teóricas (TRL 2) para resolver esta asimetría mediante una solución elegante, reproducible y adaptada a la realidad comunitaria.

---
*Notas vinculadas:* [[01 - Problem Definition & Context]] | [[04 - Ideation, HMW & Concept Evaluation]] | [[End-to-End System Pipeline]]
