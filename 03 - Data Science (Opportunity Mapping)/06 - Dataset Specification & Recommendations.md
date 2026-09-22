---
title: "Especificación del Dataset y Recomendaciones Estratégicas"
subject: "Data Science"
code: "LITD9A"
authors:
  - "Angel Emilio Gutierrez Lozano (4341)"
  - "Emiliano Betanzos Valtierra (4795)"
advisor: "Dr. Sergio Valadez Godínez"
tags:
  - dataset-design
  - parquet-schema
  - recommendations
  - data-science
---

# 💾 Especificación del Dataset y Recomendaciones Estratégicas

---

## 1. Diseño Preliminar del Conjunto de Datos: `terra_fire_spatiotemporal_matrix_v1.parquet`

![[assets/dataset-design-schema.png]]
*Figura 1: Esquema de Almacenamiento Columnar Parquet para Entrenamiento de XGBoost (Sección 10 DOM).*

| Nombre de Columna | Tipo de Dato | Fuente Física | Ingesta | Cadencia de Actualización | Propósito Operativo y Analítico |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **`voxel_id`** | `String (UUID)` | Malla Espacial H3 / UTM | Malla Estática | Clave Permanente | Identificador único de anclaje espacial ($20\times20$ m). |
| **`fire_ignition_48h`** | `Int8 ∈ {0, 1}` | CONAFOR / NASA FIRMS | **Etiqueta Objetivo** | Ventana 48–72h | Variable objetivo binaria supervisada para clasificación con XGBoost. |
| **`ndmi_canopy_water`** | `Float32 [-1, 1]` | Sentinel-2 MSI (B8, B11) | Ciclo 5 Días | Ventana rodante 5 días | Proxy de Contenido de Humedad de Combustible Vivo (LFMC). |
| **`savi_vegetative_vigor`** | `Float32 [-1, 1]` | Sentinel-2 MSI (B4, B8) | Ciclo 5 Días | Ventana rodante 5 días | Vigor de sotobosque con corrección de brillo de suelo arenoso. |
| **`nbr_fuel_dryness`** | `Float32 [-1, 1]` | Sentinel-2 MSI (B8, B12) | Ciclo 5 Días | Ventana rodante 5 días | Índice de combustibilidad y desecación severa del dosel. |
| **`vpd_kpa`** | `Float32 [kPa]` | ERA5-Land (Downscaled) | CDS Horario | Diario (02:00 UTC) | Presión de succión atmosférica que deshidrata combustibles finos. |
| **`temp_2m_celsius`** | `Float32 [°C]` | ERA5-Land (Lapse DEM) | CDS Horario | Diario (02:00 UTC) | Superficie de temperatura ambiente ajustada por elevación de terreno. |
| **`wind_speed_ms`** | `Float32 [m/s]` | ERA5-Land (U10, V10) | CDS Horario | Diario (02:00 UTC) | Magnitud de velocidad horizontal de ráfagas superficiales de viento. |
| **`soil_water_layer1`** | `Float32 [m³/m³]` | ERA5-Land (0–7 cm) | CDS Diario | Diario (02:00 UTC) | Humedad base del mantillo superficial de hojarasca seca. |
| **`slope_degrees`** | `Float32 [0°-90°]` | Copernicus GLO-30 DEM | Topo Estática | Ingesta Única | Factor de aceleración por precalentamiento convectivo en pendientes. |
| **`aspect_radians`** | `Float32 [0, 2π]` | Copernicus GLO-30 DEM | Topo Estática | Ingesta Única | Exposición acumulada a radiación solar deshidratante. |
| **`dist_roads_meters`** | `Float32 [m]` | OpenStreetMap Líneas | Semiestática | Extracción Mensual | Proxy de riesgo de chispas vehiculares y accesibilidad humana. |
| **`dist_agri_meters`** | `Float32 [m]` | INEGI / CONABIO | Semiestática | Extracción Estacional | Proximidad a parcelas agrícolas sujetas a prácticas de roza y quema. |
| **`days_since_rain`** | `Int16 [Días]` | Precipitación ERA5 | CDS Diario | Diario (02:00 UTC) | Rastreador de sequía acumulada sin lluvias significativas. |

---

## 2. Recomendaciones Estratégicas para la Fase de Modelado (TRL 3-4)

1. **Estrategia ante el Desbalance de Clases:**
   Dado que los eventos de ignición representan menos del **0.05% de los vóxeles** espaciales, no se debe utilizar la precisión (*accuracy*) como métrica de evaluación. Se debe optimizar el área bajo la curva de Precisión-Exhaustividad (**PR-AUC**) y calibrar el parámetro `scale_pos_weight` en XGBoost para penalizar los falsos negativos.
2. **Particionamiento y Almacenamiento Columnar:**
   El dataset debe almacenarse en formato Apache Parquet con compresión Snappy, particionado lógicamente por:
   `year=YYYY/month=MM/zone_utm=XX/data.parquet`
   Esto permite que los scripts de entrenamiento solo lean las columnas y regiones territoriales estrictamente necesarias sin saturar la RAM.
3. **Validación Espaciotemporal Robusta:**
   Queda estrictamente prohibido utilizar particiones aleatorias (*random train_test_split*), ya que la autocorrelación espacial genera resultados ilusorios. Debe utilizarse validación cruzada espaciotemporal por bloques territoriales (*Spatial Block Cross-Validation*).

---
*Notas vinculadas:* [[04 - Feature Taxonomy & Prioritization]] | [[05 - Gap & Risk Analysis]] | [[Feature Store & Parquet Schema]]
