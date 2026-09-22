---
title: "Taxonomía de Variables y Matriz de Priorización"
subject: "Data Science"
code: "LITD9A"
authors:
  - "Angel Emilio Gutierrez Lozano (4341)"
  - "Emiliano Betanzos Valtierra (4795)"
advisor: "Dr. Sergio Valadez Godínez"
tags:
  - feature-engineering
  - feature-store
  - machine-learning
  - data-science
---

# 🧬 Taxonomía de Variables y Matriz de Priorización

---

## 1. Inventario de Variables por Dominios de Riesgo Pre-Ignición

![[assets/variable-taxonomy-domains.png]]
*Figura 1: Taxonomía de Variables Predictivas y de Supervisión (Sección 6 DOM).*

- **1. Combustible Biofísico (Estado del Dosel y Estrato Arbóreo):**
  - `NDMI (Normalized Difference Moisture Index):` $(B8 - B11) / (B8 + B11)$ — Refleja directamente el contenido de agua en las hojas.
  - `SAVI (Soil-Adjusted Vegetation Index):` Corrección de reflectancia de suelo en matorrales áridos.
  - `NBR (Normalized Burn Ratio):` Sensible a material carbonizado y desecación extrema.
  - `SAR Polarimetric Ratio (VH/VV):` Medición por radar de microondas de humedad superficial.
- **2. Termodinámico (Fuerza Evaporativa Atmosférica):**
  - `VPD (Déficit de Presión de Vapor en kPa):` Presión de succión atmosférica que deshidrata hojas y ramas.
  - `Temperatura del Aire a 2m (°C):` Reducida a escala local mediante el gradiente térmico del terreno.
  - `Velocidad y Vectores de Viento (U10, V10):` Oxigenación potencial y dirección de dispersión.
  - `Humedad Volumétrica del Suelo (0–7 cm):` Estrato de combustible fino superficial (hojarasca).
- **3. Topográfico (Física del Terreno y Relieve):**
  - `Inclinación de Pendiente (Grados 0°–90°):` Aceleración convectiva precalentando la ladera superior.
  - `Orientación / Aspecto (Radianes):` Radiación solar acumulada (las laderas sur/suroeste son las más secas).
  - `Elevación (Metros SNM):` Estratificación bioclimática y térmica.
  - `Índice Topográfico de Humedad (TWI):` Proxy de acumulación de agua por escorrentía en cañadas.
- **4. Humano y Temporal (Presiones Antrópicas y Estacionalidad):**
  - `Distancia a Caminos (Metros):` Proxy de chispas accidentales por tránsito vehicular.
  - `Distancia a Parcelas Agrícolas (Metros):` Proximidad a zonas de quema de rastrojo (roza y quema).
  - `Día del Año (DOY) y Mes de Estiaje:` Codificación cíclica $\sin/\cos$ para capturar el pico de secas.
  - `Días sin Lluvia Medible:` Serie temporal acumulada de déficit de precipitación.
- **5. Variable Objetivo Supervisada (Ground-Truth):**
  - `Fire_Ignition_48h:` Bandera binaria $\in \{0, 1\}$ que indica si en el vóxel de $20\times20$ m ocurrirá una ignición en las próximas 48–72 horas.

---

## 2. Clasificación Estadística y Taxonomía para Machine Learning

![[assets/variable-classification-ml.png]]
*Figura 2: Clasificación de Variables según Naturaleza Estadística y Fuente (Sección 6 DOM).*

| Variable | Tipo (Indep / Dep) | Escala (Categ / Num) | Unidad de Medida | Fuente del Pipeline |
| :--- | :---: | :---: | :--- | :--- |
| **`fire_ignition_48h`** | **Dependiente** | Categórica (Binaria) | Bandera $\in \{0, 1\}$ | CONAFOR SNIF / NASA FIRMS |
| **`ndmi`** | Independiente | Numérica (Continua) | Ratio $[-1.0, 1.0]$ | Sentinel-2 MSI (B8/B11) |
| **`vpd_kpa`** | Independiente | Numérica (Continua) | Kilopascales ($kPa$) | Derivado de ERA5-Land |
| **`temp_2m`** | Independiente | Numérica (Continua) | Grados Celsius ($^\circ C$) | ERA5-Land (Downscaling DEM) |
| **`wind_speed_10m`** | Independiente | Numérica (Continua) | Metros por segundo ($m/s$) | ERA5-Land (Vectores U, V) |
| **`soil_moist_l1`** | Independiente | Numérica (Continua) | $m^3/m^3$ ($0.0$ a $0.6$) | ERA5-Land Capa 1 |
| **`slope_deg`** | Independiente | Numérica (Continua) | Grados ($0^\circ$ a $90^\circ$) | Copernicus GLO-30 DEM |
| **`aspect_rad`** | Independiente | Numérica (Continua) | Radianes ($[0, 2\pi]$) | Copernicus GLO-30 DEM |
| **`land_cover_type`** | Independiente | Categórica (Nominal) | Código entero de bioma | INEGI Serie VII / CONABIO |
| **`dist_roads_m`** | Independiente | Numérica (Continua) | Metros ($m$) | OpenStreetMap Vectors |
| **`dist_agri_m`** | Independiente | Numérica (Continua) | Metros ($m$) | INEGI Uso de Suelo / CONABIO |
| **`days_since_rain`** | Independiente | Numérica (Discreta) | Días enteros | Serie precipitación ERA5 |

---

## 3. Matriz de Priorización de Variables Predictivas

![[assets/feature-prioritization-matrix.png]]
*Figura 3: Jerarquización de Variables según Razón Biofísica y Viabilidad (Sección 6 DOM).*

```mermaid
quadrantChart
    title Priorización de Variables Predictivas
    x-axis Baja Factibilidad Técnica --> Alta Factibilidad Técnica
    y-axis Bajo Impacto Físico --> Alto Impacto Físico
    quadrant-1 PRIORIDAD 1: CRÍTICAS
    quadrant-2 APUESTAS ESTRATÉGICAS
    quadrant-3 DEPRIORIZAR
    quadrant-4 CONTEXTUALES / FÁCILES
    "VPD_kPa (Déficit Vapor)": [0.85, 0.95]
    "NDMI (Humedad Dosel)": [0.80, 0.92]
    "Fire_Ignition_48h": [0.75, 0.98]
    "Slope & Aspect (Topografía)": [0.95, 0.78]
    "Soil_Moist_L1 (Suelo)": [0.88, 0.75]
    "Wind_Speed_10m (Viento)": [0.82, 0.72]
    "Dist_Roads & Agri": [0.92, 0.45]
    "Radar SAR Sentinel-1": [0.45, 0.65]
```

- **Críticas (P1):** `vpd_kpa`, `ndmi`, `fire_ignition_48h` — Representan los detonantes físicos indiscutibles de ignición.
- **Altas (P2):** `slope_deg`, `aspect_rad`, `soil_moist_l1`, `wind_speed_10m` — Gobiernan la velocidad de precalentamiento y desecación del suelo.
- **Contextuales (P3):** `dist_roads_m`, `dist_agri_m` — Proxies directos de actividad y origen humano.

---
*Notas vinculadas:* [[03 - Big Data 5Vs & Ecosystem Architecture]] | [[05 - Gap & Risk Analysis]] | [[Feature Store & Parquet Schema]]
