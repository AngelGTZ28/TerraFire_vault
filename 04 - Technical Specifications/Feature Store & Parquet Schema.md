---
title: "Feature Store, Fórmulas Matemáticas y Esquema Parquet"
project: "TERRA-FIRE"
category: "Technical Specifications"
tags:
  - formulas
  - feature-store
  - parquet-schema
  - mathematical-models
---

# 📐 Feature Store, Fórmulas Matemáticas y Esquema Parquet

---

## 1. Fórmulas Matemáticas de Índices Biofísicos y Variables Físicas

### 1. Índice de Humedad de Diferencia Normalizada (NDMI)
Proxy biofísico de alta fidelidad del Contenido de Humedad de Combustible Vivo (*Live Fuel Moisture Content - LFMC*):
$$NDMI = \frac{B8_{NIR} - B11_{SWIR1}}{B8_{NIR} + B11_{SWIR1}}$$
*Donde:* $B8$ es la banda de Infrarrojo Cercano (842 nm, resolución 10 m) y $B11$ es la banda de Infrarrojo de Onda Corta (1610 nm, resolución 20 m).

### 2. Índice de Vegetación Ajustado al Suelo (SAVI)
Minimiza las perturbaciones de brillo de suelo en matorrales áridos y chaparrales:
$$SAVI = \frac{(B8 - B4)}{B8 + B4 + L} \times (1 + L)$$
*Donde:* $L = 0.5$ (factor estándar de corrección de brillo de suelo para doseles intermedios) y $B4$ es la banda Roja (665 nm).

### 3. Índice Diferenciado de Quema (NBR)
Sensible al contenido de lignina, agua y restos carbonizados:
$$NBR = \frac{B8_{NIR} - B12_{SWIR2}}{B8_{NIR} + B12_{SWIR2}}$$

### 4. Déficit de Presión de Vapor (VPD)
La fuerza termodinámica principal que extrae el agua de la biomasa hacia la atmósfera:
$$VPD = e_s(T) - e_a(T_{dew})$$
Donde la presión de vapor de saturación $e_s$ se calcula mediante la ecuación de Tetens ($T$ en $^\circ C$):
$$e_s(T) = 0.61078 \exp\left(\frac{17.27 \cdot T}{T + 237.3}\right) \quad [kPa]$$
Y la presión de vapor real $e_a$ se obtiene evaluando la misma función en la temperatura de punto de rocío ($T_{dew}$):
$$e_a = 0.61078 \exp\left(\frac{17.27 \cdot T_{dew}}{T_{dew} + 237.3}\right) \quad [kPa]$$

### 5. Reducción Adiabática de Temperatura por Relieve (Lapse-Rate Downscaling)
Ajuste térmico continuo por altitud sobre la malla DEM:
$$T_{downscaled} = T_{ERA5} + \Gamma \cdot (Z_{DEM} - Z_{ERA5})$$
*Donde:* $\Gamma = -0.0065 \, ^\circ C/m$ (gradiente adiabático ambiental estándar) y $Z$ es la elevación en metros sobre el nivel del mar.

---

## 2. Diccionario de Datos del Esquema `terra_fire_spatiotemporal_matrix_v1.parquet`

```text
Estructura de Particionado en Disco:
s3://terra-fire-lakehouse/features/v1/year=YYYY/month=MM/zone_utm=XX/part-*.parquet
```

| Campo | Tipo Parquet | Nullable | Rango Válido | Descripción Técnica |
| :--- | :--- | :---: | :---: | :--- |
| `voxel_id` | `BYTE_ARRAY (UTF8)` | No | — | Identificador espacial único derivado de la malla UTM/H3. |
| `timestamp` | `INT64 (TIMESTAMP_MILLIS)` | No | — | Marca temporal de la ventana de pronóstico (UTC). |
| `fire_ignition_48h` | `INT32 (INT_8)` | No | $[0, 1]$ | **Variable Objetivo:** $1$ si hubo ignición en 48–72h, $0$ caso contrario. |
| `ndmi` | `FLOAT` | No | $[-1.0, 1.0]$ | Humedad del dosel foliar derivado de Sentinel-2 L2A. |
| `savi` | `FLOAT` | No | $[-1.0, 1.0]$ | Vigor de vegetación ajustado por suelo desnudo. |
| `nbr` | `FLOAT` | No | $[-1.0, 1.0]$ | Índice normalizado de combustibilidad de biomasa. |
| `vpd_kpa` | `FLOAT` | No | $[0.0, 10.0]$ | Déficit de Presión de Vapor en kilopascales. |
| `temp_2m_c` | `FLOAT` | No | $[-20.0, 55.0]$ | Temperatura ambiente ajustada por elevación ($^\circ C$). |
| `wind_u10` | `FLOAT` | No | $[-50.0, 50.0]$ | Componente horizontal zonal del viento ($m/s$). |
| `wind_v10` | `FLOAT` | No | $[-50.0, 50.0]$ | Componente horizontal meridional del viento ($m/s$). |
| `soil_moist_l1` | `FLOAT` | No | $[0.0, 0.6]$ | Fracción de agua volumétrica en suelo ($0–7$ cm). |
| `slope_deg` | `FLOAT` | No | $[0.0, 90.0]$ | Pendiente topográfica en grados sexagesimales. |
| `aspect_rad` | `FLOAT` | No | $[0.0, 2\pi]$ | Orientación de ladera respecto al norte en radianes. |
| `dist_roads_m` | `FLOAT` | No | $[0.0, 100000.0]$ | Distancia euclidiana al camino vehicular más cercano. |
| `dist_agri_m` | `FLOAT` | No | $[0.0, 100000.0]$ | Distancia euclidiana al límite de parcelas agrícolas activas. |
| `days_since_rain`| `INT32 (INT_16)` | No | $[0, 365]$ | Conteo acumulado de días con precipitación $< 1.0$ mm. |

---
*Notas vinculadas:* [[End-to-End System Pipeline]] | [[04 - Feature Taxonomy & Prioritization]] | [[06 - Dataset Specification & Recommendations]]
