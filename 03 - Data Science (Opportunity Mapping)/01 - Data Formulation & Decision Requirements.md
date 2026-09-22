---
title: "Formulación de Datos y Requisitos de Decisión"
subject: "Data Science"
code: "LITD9A"
authors:
  - "Angel Emilio Gutierrez Lozano (4341)"
  - "Emiliano Betanzos Valtierra (4795)"
advisor: "Dr. Sergio Valadez Godínez"
tags:
  - data-science
  - decision-analysis
  - information-needs
  - data-opportunity-mapping
---

# 📊 Formulación de Datos y Requisitos de Decisión

> [!abstract] Reencuadre a Ciencia de Datos
> El manejo de incendios forestales en México enfrenta una crisis operativa arraigada en un desfase técnico sistémico. La protección civil opera bajo esquemas de combate reactivo tras la detección de anomalías térmicas en órbita. Este documento transforma el reto: **de una crisis de respuesta de emergencia a un problema de ingeniería de Big Data y analítica predictiva**.

---

## 1. Análisis de Toma de Decisiones y Actores

![[assets/decision-making-stakeholders.png]]
*Figura 1: Matriz de Decisiones Operativas, Actores e Información Requerida (Sección 2 DOM).*

| Código | Decisión Operativa | Tomador de Decisión | Información Clave Requerida | Cadencia y Urgencia |
| :--- | :--- | :--- | :--- | :--- |
| **DEC-01** | **Despliegue Preventivo de Brigadas y Recursos** *(Tactical Staging)* | Protección Civil Estatal y Municipal; Coordinadores Operativos de CONAFOR. | Mapas de probabilidad de ignición 48–72h; zonas con desecación crítica de combustible (NDMI/LFMC); red vial y accesibilidad. | **Diaria (06:00 AM)** <br> Actualizada cada 24 horas. |
| **DEC-02** | **Aprobación de Quemas y Moratorias Forestales** *(Preventive Moratoria)* | Autoridades Forestales Municipales; Comisariados Ejidales; Protección Civil. | Demanda evaporativa atmosférica (VPD); índices de humedad de combustible muerto; vectores y ráfagas de viento a 72h. | **Bisemanal / Pico de Estiaje** <br> Consulta diaria en sequía. |
| **DEC-03** | **Ruteo Táctico y Rutas Seguras de Evacuación** *(Fireline Safety)* | Brigadas Forestales de Primera Línea; Ejidatarios Voluntarios; Cuadrillas Rápidas. | Superficies de riesgo localizadas en teselas offline; zonas de "efecto chimenea" por pendiente; canales de escape. | **Tiempo Real en Campo** <br> Ejecución offline en PWA. |
| **DEC-04** | **Evaluación de Perímetro y Severidad de Daño** *(Damage Verification)* | Analistas Ambientales de CONAFOR; Evaluadores Técnicos Post-Incidente. | Índice Diferenciado de Quema (dNBR); imágenes Sentinel-2 pre y post-incendio; polígonos de biomasa perdida. | **< 48h Post-Incendio** <br> Ciclo de contención. |

---

## 2. Evaluación de Necesidades de Información Ambiental

![[assets/info-needs-environmental.png]]
*Figura 2: Mapeo de Requisitos Biofísicos, Termodinámicos y Espaciales (Sección 2 DOM).*

| Necesidad de Información | Granularidad Requerida | Entidades y Características Objetivo | Fuente de Datos Primaria | Salida Funcional en el Pipeline |
| :--- | :--- | :--- | :--- | :--- |
| **Estrés Hídrico y Desecación del Dosel** | Res. 10–20 m; ciclo orbital 5 días; latencia en nube <6h. | NDMI: $(B8 - B11) / (B8 + B11)$ <br> NDWI: $(B8 - B12) / (B8 + B12)$ <br> SAVI: Corrección de reflectancia de suelo. | **Copernicus Sentinel-2 MSI L2A** *(Reflectancia BOA)* | **Capa Proxy LFMC:** Índice dinámico de inflamabilidad de vegetación viva. |
| **Demanda Evaporativa Micro-Atmosférica** | Temporal horaria; resolución espacial $0.1^\circ$ (~9 km) reducida a 30 m por DEM. | Temperatura de aire 2m ($T_{air}$), punto de rocío ($T_{dew}$), Déficit de Presión de Vapor (VPD en kPa), vectores de viento horizontal 10m (U/V). | **ECMWF ERA5-Land** *(API CDS Copernicus)* | **Superficie de Secado Atmosférico:** Fuerza evaporativa que deshidrata el combustible fino. |
| **Pendiente, Orientación y Exposición Solar** | Resolución espacial 30 m; capa base estática; latencia cero. | Pendiente ($0^\circ–90^\circ$), Orientación en radianes de radiación solar acumulada, Índice Topográfico de Humedad (TWI). | **Copernicus GLO-30 DEM / SRTM** | **Multiplicador de Terreno:** Aceleración por convección en laderas y efecto embudo en cañadas. |
| **Humedad Superficial del Suelo** | Diaria / multicapa ($0–7$ cm Capa 1, $7–28$ cm Capa 2). | Agua volumétrica del suelo ($m^3/m^3$); retrodispersión SAR co/cross-ratio. | **ERA5-Land & Sentinel-1 SAR** | **Sequedad de Sotobosque:** Umbral de ignición de hojarasca y combustibles muertos. |
| **Etiquetas Históricas de Ignición** | Polígonos históricos; puntos VIIRS de 375 m; coincidencia temporal 48–72h. | Coordenadas Lat/Lon de anomalías térmicas; marcas de tiempo GPS; validación cruzada con reportes oficiales. | **CONAFOR SNIF & NASA FIRMS** | **Etiquetas Objetivo Binarias:** Variable supervisada $Y \in \{0, 1\}$ para entrenamiento XGBoost. |

---
*Notas vinculadas:* [[02 - Data Source Catalog & Ingestion]] | [[04 - Feature Taxonomy & Prioritization]] | [[01 - Problem Definition & Context]]
