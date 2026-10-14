---
title: "Activity 3 - Data Engineering Lab (Official Report)"
project: "TERRA-FIRE"
institution: "Universidad Tecnológica El Retoño"
course: "Data Science (LITD9A)"
term: "Sep-Dec 2026"
professor: "Dr. Sergio Valadez Godínez"
authors:
  - "Angel Emilio Gutierrez Lozano (4341)"
  - "Emiliano Betanzos Valtierra (4795)"
repository: "https://github.com/AngelGTZ28/TERRA-FIRE"
readiness_decision: "READY FOR ANALYSIS"
status: "TRL 2/3 - Data Engineering Complete"
tags:
  - data-science
  - data-engineering
  - terra-fire
  - etl-pipeline
  - apache-parquet
---

# 🌲 UNIVERSIDAD TECNOLÓGICA EL RETOÑO
### **Engineering in Information Technologies and Digital Innovation**
**Subject:** Data Science (LITD9A)  
**Teacher:** Dr. Sergio Valadez Godínez  
**Term:** September – December 2026  
**Activity:** Activity 3. Data Engineering Lab  
**Students:** Angel Emilio Gutierrez Lozano (ID: 4341) & Emiliano Betanzos Valtierra (ID: 4795)  
**Date:** October 14, 2026  
**Official Repository:** [https://github.com/AngelGTZ28/TERRA-FIRE](https://github.com/AngelGTZ28/TERRA-FIRE)

---

## 1. Raw Data and Storage Structure

### 1.1 Datasets Entering the ETL Pipeline
The Data Engineering pipeline ingests the planetary Earth Observation, meteorological reanalysis, and official administrative wildfire incident datasets approved in the preceding Data Acquisition Strategy:

1. **CONAFOR Historical Forest Fire Registry (2012–2025):** 101,003 official fire incident records across Mexico, detailing ignition timestamps, geographical coordinates, affected strata surface areas, and detected causes (`.xlsx`, 18.6 MB).
2. **NASA FIRMS VIIRS Active Fire Detections (2023–2024):** 657,791 high-resolution (375 m) thermal anomaly detections from the Suomi-NPP VIIRS sensor covering the Mexican territory, capturing Fire Radiative Power (FRP) and brightness temperature (`.csv`, 52.4 MB combined).
3. **ECMWF ERA5-Land Hourly Surface Reanalysis (2023–2024):** 17,544 continuous hourly atmospheric steps for the Sierra Fría biological testbed (22.18°N, -102.63°W), capturing air temperature, dew point, precipitation, wind vectors, and soil moisture (`.csv`, 0.93 MB).
4. **Copernicus DEM (GLO-30):** High-resolution 30-meter elevation raster tile providing terrain altitude, slope gradient, and aspect for atmospheric lapse-rate downscaling (`.tif` Cloud-Optimized GeoTIFF, 35.4 MB).
5. **Copernicus Sentinel-2 MSI Level-2A:** Multispectral surface reflectance scene metadata item capturing NIR (B08), Red (B04), and SWIR (B11, B12) bands to derive canopy moisture dynamics (`.json` STAC Item, 0.03 MB).

### 1.2 Resource Directory Organization
The pipeline enforces strict folder modularity to guarantee that raw data remain immutable, intermediate artifacts remain isolated, and processed products are optimized:

```text
TERRA-FIRE/
├── data/
│   ├── sample/                     # Small representative subsets for rapid testing and git versioning
│   │   ├── conafor_fires_aguascalientes_sample.csv  (282 verified state records)
│   │   ├── era5_hourly_sample.csv                   (1,000 hourly calibration rows)
│   │   ├── firms_viirs_sierra_fria_sample.csv       (2,211 regional active fire detections)
│   │   ├── sentinel2_stac_sample.json               (Planetary STAC scene metadata)
│   │   └── terra_fire_matrix_sample.csv             (2,000 analysis-ready sample rows)
│   ├── raw/                        # Original acquired datasets (unmodified, excluded from Git)
│   │   ├── README.md               # Acquisition provenance, source URLs and cryptographic hashes
│   │   └── .gitkeep
│   ├── intermediate/               # Temporary cache generated during ETL (excluded from Git)
│   │   └── .gitkeep
│   └── processed/                  # Final Analysis-Ready Dataset
│       └── terra_fire_spatiotemporal_matrix_v1.parquet (0.30 MB, Snappy Columnar)
├── metadata/                       # Audit dictionaries, cleaning logs, and validation matrices
├── notebooks/                      # data_engineering_lab.ipynb
├── src/                            # Modular Python packages (extract, clean, transform, integrate, validate)
├── .gitignore                      # Protection against committing large files (>50MB) and raw tables
├── README.md                       # Comprehensive operational execution guide
└── requirements.txt                # Pinned dependencies
```

### 1.3 Repository Storage vs External Storage Allocation
- **Stored in GitHub Repository:** Python source modules (`src/`), interactive notebook (`notebooks/`), metadata dictionaries (`metadata/`), configuration files, `.gitignore`, representative samples (`data/sample/` $\le 5$ MB total), and the optimized analytical Parquet file (`data/processed/` $\approx 0.30$ MB).
- **Stored in External Storage (`TERRAFIRE-db` / Institutional Lakehouse):** Full national raw spreadsheets (CONAFOR 18.6 MB), multi-year national satellite catalogs (NASA FIRMS 52.4 MB), and raw 32-bit floating point elevation GeoTIFF rasters (35.4 MB). This prevents GitHub repository bloat while maintaining full algorithmic reproducibility.

---

## 2. Data Architecture and Storage Decision

### 2.1 The Four-Layer Computing Architecture
In alignment with data engineering principles, four distinct architectural layers are decoupled:
1. **Layer 1: Project Repository (GitHub):** Version control hub holding source code, tests, documentation, configuration, and small reproducible samples.
2. **Layer 2: Development Environment (GitHub Codespaces / VS Code):** Isolated cloud or workstation development container executing Python 3.12, Jupyter, and dependency management without host pollution.
3. **Layer 3: Data Storage:** Tiered storage architecture separating local/cloud raw data from production columnar feature stores.
4. **Layer 4: Data Processing:** Vectorized in-memory compute infrastructure (Python + Pandas/PyArrow) optimized for analytical arrays.

### 2.2 Data Storage Decision Matrix

| Dataset Name | Primary Provider | Size | Fits in RAM? | Classification | Storage Location | Technical Justification |
| :--- | :--- | :---: | :---: | :--- | :--- | :--- |
| **CONAFOR Historic (2012–2025)** | CONAFOR / SEMARNAT | 18.6 MB | Yes | **Sample Only** (Git) / **External** (Full) | `TERRAFIRE-db/` & `data/sample/` | National table has 101,003 rows. Storing in Git adds unnecessary binary weight. A verified regional sample for Aguascalientes (282 rows) is tracked in Git. |
| **NASA FIRMS VIIRS (2023–2024)** | NASA LANCE / FIRMS | 52.4 MB | Yes | **Sample Only** (Git) / **External** (Full) | `TERRAFIRE-db/` & `data/sample/` | Combined file contains 657,791 rows. Excluded via `.gitignore`; regional monitoring sample (2,211 rows) is versioned in Git. |
| **ECMWF ERA5-Land Hourly** | ECMWF / Copernicus C3S | 0.93 MB | Yes | **Repository Suitable** | `data/sample/era5_hourly_sample.csv` | Microclimatic hourly reanalysis (17,544 rows) fits within GitHub limits (<1 MB). |
| **Sentinel-2 L2A STAC Item** | ESA / Microsoft PC | 0.03 MB | Yes | **Repository Suitable** | `data/sample/sentinel2_stac_sample.json` | Lightweight JSON metadata catalog item. Perfectly suited for repository storage. |
| **Copernicus DEM (GLO-30)** | ESA / Airbus | 35.4 MB | Yes | **External Storage Required** | Cloud Object Store / `TERRAFIRE-db/` | High-precision 32-bit floating point raster tile. Stored externally; referenced programmatically. |
| **Processed Parquet Feature Store** | TERRA-FIRE Engine | 0.30 MB | Yes | **Repository Suitable** | `data/processed/terra_fire_*.parquet` | Binary columnar layout with Snappy compression reduces disk footprint by >90%, making it ideal for versioning. |

---

## 3. Data Quality Diagnosis

### 3.1 Profiling Summary & Structural Anomalies
Rigorous inspection across all raw datasets revealed the following empirical quality defects prior to modification:

1. **Structural Metadata Header in ERA5 CSV:** Lines 1–2 of `ERA5_Land_Hourly_SierraFria_2023_2024.csv` contained station metadata (`latitude, longitude, elevation, timezone`), followed by a blank line, causing generic CSV readers to crash (`ParserError: Expected 6 fields in line 4, saw 9`).
2. **Corrupted Encoding in Column Names:** CONAFOR headers contained corrupted Windows-1252 / ISO-8859 characters (`'Ao'`, `'Herbceo'`, `'Rgimen de fuego'`, `'Total hectreas'`). ERA5 contained degree and unit symbols (`(°C)`, `(%)`, `(m³/m³)`).
3. **Temporal Inconsistencies:** NASA FIRMS split temporal coordinates into `acq_date` (`2023-05-12`) and `acq_time` (e.g., integer `820` or `1430`). ERA5 timestamps were local strings (`2023-01-01T00:00`) lacking UTC offset.
4. **Coordinate Sign Inversions:** 48 records in the CONAFOR national table exhibited positive longitude coordinates (e.g., `102.63°` instead of `-102.63°`), mapping fire events to China/Indian Ocean instead of Mexico.
5. **Missing Strata Hectares:** CONAFOR contained missing values in vegetation strata impact fields (`Arbolado Adulto`: 4 nulls, `Renuevo`: 10 nulls, `Arbustivo`: 11 nulls, `Herbáceo`: 7 nulls) and 946 nulls in `Tipo Vegetación`.

### 3.2 Data Processing Scale Assessment

| Dataset | Total Records | In-Memory RAM Size | Processing Strategy | Technical Justification |
| :--- | :---: | :---: | :--- | :--- |
| **CONAFOR Historic** | 101,003 | ~35 MB | **In-Memory Pandas Vectorization** | Entire table fits comfortably into RAM; vectorized string and spatial filtering execute in <1.2 seconds. |
| **NASA FIRMS (2023–2024)** | 657,791 | ~110 MB | **In-Memory Pandas + BBox Indexing** | Conventional memory processing handles 650k rows efficiently; spatial bounding box slicing reduces active records to 2,211. |
| **ECMWF ERA5-Land** | 17,544 | ~5 MB | **In-Memory Pandas Rolling Windows** | Two complete years of continuous hourly records process in <0.3 seconds using vectorized datetime offsets. |
| **Integrated Feature Matrix** | 18,275 | <15 MB | **Scaled Pipeline -> Parquet Output** | Conforms to **Scenario A / Scaled Pipeline**: conventional memory processing is optimal, avoiding unnecessary distributed compute overhead. |

---

## 4. Data Cleaning

### 4.1 Applied Cleaning Rules & Justification
- **Metadata Header Extraction:** Programmatically parsed station coordinates from lines 1–2 of ERA5, skipping the first 3 lines (`skiprows=3`) during tabular loading.
- **Header Standardization:** Converted all 37 CONAFOR columns and 9 ERA5 columns into clean English/ASCII snake_case identifiers.
- **Temporal Alignment:** Formatted `acq_time` with zero-padding to 4 digits (`0820` $\rightarrow$ `08:20:00`), concatenated with `acq_date`, and parsed as `datetime64[ns]` UTC. Converted ERA5 local timestamps to UTC (+6h offset).
- **Longitude Sign Correction:** Inverted positive longitudes in Mexican territory by multiplying by `-1.0`.
- **Transparent Imputation:** Null vegetative strata hectares were set to `0.0` (reflecting zero affected surface area in that stratum). Missing forest vegetation classifications were mapped to the explicit categorical token `'No Especificado'` rather than silently deleting rows.

### 4.2 Data Cleaning Log

| Issue | Original Condition | Cleaning Rule | Records Affected | Result |
| :--- | :--- | :--- | :---: | :--- |
| **ERA5 Header Metadata Rows** | Lines 1–3 contained station coordinates, causing CSV tokenizer failure (`ParserError`). | Extract metadata dictionary from lines 1–2; skip 3 rows (`skiprows=3`) to load table header on line 4. | 17,544 rows | Clean DataFrame loading with separate geospatial station metadata dictionary. |
| **ERA5 Corrupted Column Headers** | Attribute names contained non-ASCII symbols and units (`temperature_2m (°C)`, `soil_moisture_0_to_7cm (m³/m³)`). | Standardize column names into snake_case lowercase identifiers (`temp_2m_c`, `soil_moist_0_to_7cm_m3m3`). | 17,544 rows (9 columns) | 100% ASCII-compliant column schema ready for parquet serialization. |
| **ERA5 Temporal Reference Frame** | Hourly timestamps formatted as ISO-8601 strings without explicit UTC synchronization (`2023-01-01T00:00`). | Cast to `datetime64[ns]`, assign `timestamp_local` (GMT-6), and derive explicit `timestamp_utc` (+6 hours). | 17,544 rows | Synchronized dual-temporal reference frame for satellite fusion. |
| **NASA FIRMS Disconnected Date & Time** | Satellite detection dates (`acq_date`) and scan times (`acq_time` e.g. `820` or `1430`) stored separately. | Zero-pad `acq_time` to 4 digits (`0820`), format as `HH:MM:SS`, concatenate with `acq_date` and cast to `datetime64[ns]` UTC. | 657,791 detections | Single unified `timestamp_utc` column enabling temporal window joins. |
| **NASA FIRMS Categorical Codes** | Confidence and satellite pass flags encoded as cryptic single characters (`confidence: 'l', 'n', 'h'`, `daynight: 'D', 'N'`). | Map values to descriptive categories: `'low', 'nominal', 'high'` and `'Day', 'Night'`. | 657,791 detections | Self-documenting categorical attributes. |
| **NASA FIRMS Outliers & Duplicates** | Repeated orbital scan overlaps and edge detections outside Mexico's sovereign territory. | Filter latitude to $[14.0^\circ\text{N}, 33.5^\circ\text{N}]$ and longitude to $[-118.5^\circ\text{W}, -86.0^\circ\text{W}]$; deduplicate by `(latitude, longitude, timestamp_utc)`. | 3,142 records nationwide | Eliminates unphysical coordinates and artificial duplicate fire detections. |
| **CONAFOR Spanish Encoding Artifacts** | Column headers contained corrupted ISO-8859 characters (`'Ao'`, `'Herbceo'`, `'Rgimen de fuego'`). | Rename all 37 columns to standardized snake_case identifiers (`anio`, `fire_id`, `stratum_herbaceo_ha`, etc.). | 101,003 records (37 columns) | Fully clean columnar identifiers compatible with Parquet and Arrow schemas. |
| **CONAFOR Positive Longitudes** | Longitude coordinates recorded with positive signs (e.g. `102.63` instead of `-102.63`), placing coordinates in Asia. | Check `longitude > 0` condition across Mexican coordinates and multiply by `-1.0`. | 48 records | Restores coordinates to the Western Hemisphere within Mexican territory. |
| **CONAFOR Unmappable Coordinates** | Missing or out-of-range coordinates (`latitude` null or $< 14^\circ$). | Drop unmappable records lacking valid geographic coordinates after logging. | 2 records | 100% of retained historical records are spatially mappable. |
| **CONAFOR Missing Strata Hectares** | Null values present in vegetative stratum impact columns (`stratum_arbolado_adulto_ha`, `stratum_renuevo_ha`). | Explicitly impute `NaN` values to `0.0` ha, reflecting zero affected surface in that stratum. | 32 records | Preserves record integrity without arbitrary statistical bias. |
| **CONAFOR Missing Vegetation Type** | 946 historical fire events lacked categorical forest vegetation classification (`tipo_vegetacion = NaN`). | Impute missing categories with explicit token `'No Especificado'`. | 946 records | Prevents silent record deletion while maintaining audit transparency. |
| **CONAFOR Duplicate Fire Keys** | Duplicate entries sharing identical official `Clave del incendio` (`fire_id`). | Identify duplicates and retain the primary official entry, discarding secondary duplicates. | 14 records | Ensures primary key uniqueness across the ground-truth table. |

---

## 5. Data Transformation and Standardization

### 5.1 Thermodynamic Formulations and Feature Engineering
To capture the physical drivers of wildfire ignition, the cleaned data were transformed into biophysical features:

1. **Vapor Pressure Deficit (VPD in kPa) via Tetens Formulation:**
   $$\begin{aligned}
   e_s(T) &= 0.61078 \exp\left(\frac{17.27 \cdot T}{T + 237.3}\right) \quad [kPa] \\
   e_a(T_{dew}) &= 0.61078 \exp\left(\frac{17.27 \cdot T_{dew}}{T_{dew} + 237.3}\right) \quad [kPa] \\
   VPD &= \max(0.0, e_s(T) - e_a(T_{dew}))
   \end{aligned}$$
2. **Horizontal Wind Vector Decomposition:**
   $$\begin{aligned}
   ws_{ms} &= ws_{kmh} / 3.6 \\
   u_{10} &= -ws_{ms} \cdot \sin(\theta_{rad}) \quad (\text{zonal, west-to-east}) \\
   v_{10} &= -ws_{ms} \cdot \cos(\theta_{rad}) \quad (\text{meridional, south-to-north})
   \end{aligned}$$
3. **Topographic Lapse-Rate Downscaling:**
   $$T_{downscaled} = T_{ref} + \Gamma \cdot (Z_{DEM} - Z_{ref})$$
   where $\Gamma = -0.0065 \, ^\circ C/m$, adjusting temperatures across altitudes from 1,850 m to 2,920 m.
4. **Cumulative Dry Days Counter (`days_since_rain`):** Consecutive daily count where precipitation $< 1.0$ mm.
5. **Biophysical Moisture Proxies (NDMI, SAVI, NBR):** Scaled using calibrated Sentinel-2 multispectral surface reflectance bands.

### 5.2 Storage Format Justification: Apache Parquet vs CSV / JSON
Apache Parquet was evaluated against CSV and JSON across four criteria:
- **Storage Footprint:** CSV (3.8 MB uncompressed) vs JSON (8.5 MB verbose) vs **Parquet (0.30 MB, Snappy compressed, 92% size reduction)**.
- **Type Safety:** Parquet embeds exact bit-width Arrow schemas (`float32`, `int32`, `category`), eliminating type guessing errors on load.
- **Column Projection:** Parquet allows downstream models to read only the required 5 features without deserializing all 22 columns into memory.
- **Read Performance:** Benchmarked loading speed is $8.4\times$ faster in Parquet than parsing raw text CSVs.

---

## 6. Data Integration

### 6.1 Multi-Source Granularity Harmonization
The project fuses datasets with conflicting temporal cadences and spatial representations:
- **Spatial Lattice:** 25 regional monitoring voxels (`AGS_V01` – `AGS_V25`) spanning the Aguascalientes / Sierra Fría fire corridors (21.65°N to 22.35°N, -102.75°W to -102.05°W).
- **Temporal Baseline:** 731 continuous calendar days across 2023 and 2024 (leap year).
- **Cartesian Product:** $25 \text{ voxels} \times 731 \text{ days} = 18,275 \text{ space-time observations}$.
- **Target Formulation (`fire_ignition_48h`):** Fused NASA FIRMS thermal detections (2,211 detections) and CONAFOR validated ignitions (282 records) within a spatial Euclidean radius $r \le 0.08^\circ$ (~8.5 km) and a 48–72h anticipatory window ($t+1$ to $t+3$ days prior).

### 6.2 Data Integration Record Table

| Source Dataset | Integration Key | Integration Method | Records Before | Records After | Identified Granularity Issues | Applied Mitigation Rule |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| **ECMWF ERA5-Land** | `date` (`YYYY-MM-DD`) | Temporal rolling aggregation + Left Join | 17,544 hourly rows | 18,275 space-time rows | Hourly series vs daily risk window | Aggregated hourly readings into daily maximums, minimums, and 72h rolling metrics prior to merge. |
| **Topographic Monitoring Grid** | `voxel_id` (`AGS_V01`–`AGS_V25`) | Cartesian Space-Time Expansion | 25 spatial nodes | 18,275 space-time rows | Continuous elevation raster vs discrete nodes | Sampled 25 representative benchmark voxels covering key forest and shrub strata. |
| **NASA FIRMS VIIRS** | `(lat, lon)` + `timestamp_utc` | Spatiotemporal Radius & Window Match | 2,211 regional detections | 876 positive ignition windows | Satellite pass asynchrony (01:30 & 13:30 local) | Formulated Euclidean buffer ($r \le 0.08^\circ$) and 48–72h forward-looking predictive window ($t+1$ to $t+3$ days). |
| **CONAFOR Fire Registry** | `(lat, lon)` + `date_start` | Spatiotemporal Radius & Window Match | 282 state records | Included in positive ground-truth target flags | Administrative logging delay vs physical ignition | Fused jointly with NASA FIRMS active fire detections to calibrate ground-truth ignition veracity. |

### 6.3 Spatiotemporal Integration Flow Diagram

```mermaid
flowchart TD
    subgraph S1["Raw Climate Stream"]
        ERA5["ECMWF ERA5-Land Hourly<br/>(17,544 rows, 9 cols)"] --> CLN1["Clean & Localize GMT-6<br/>(+ UTC timestamp)"]
        CLN1 --> TRF1["Daily Microclimatic Aggregation<br/>(Max Temp, Min RH, Tetens VPD, 72h Rolling)"]
    end

    subgraph S2["Topographic Lattice"]
        GRID["25 Regional Monitoring Voxels<br/>(AGS_V01 to AGS_V25)<br/>Elevation, Slope, Fuel Type, Distances"]
    end

    subgraph S3["Ground-Truth Incident Streams"]
        FIRMS["NASA FIRMS VIIRS<br/>(2,211 detections)"]
        CONAFOR["CONAFOR Fire Registry<br/>(282 records)"]
        FIRMS & CONAFOR --> SP_BUF["Spatiotemporal Matcher<br/>Radius <= 0.08° (~8.5 km)<br/>Window: 48h to 72h ahead"]
    end

    TRF1 & GRID --> CART["Cartesian Product Expansion<br/>(25 voxels x 731 days = 18,275 rows)"]
    CART --> DOWN["Lapse-Rate Downscaling &<br/>Biophysical Index Modeling (NDMI, SAVI, NBR)"]
    DOWN & SP_BUF --> TARGET["Binary Supervisory Label Assignment<br/>(fire_ignition_48h: 876 positive / 17,399 negative)"]
    TARGET --> PARQ["Apache Parquet Feature Store<br/>(terra_fire_spatiotemporal_matrix_v1.parquet)<br/>0.30 MB, Snappy Encoded"]
```

---

## 7. Analysis-Ready Dataset

### 7.1 Dataset Profile
- **File Name:** `terra_fire_spatiotemporal_matrix_v1.parquet`
- **Location:** `data/processed/terra_fire_spatiotemporal_matrix_v1.parquet`
- **Format:** Apache Parquet (Snappy Compression, Binary Columnar Layout)
- **Total Records:** 18,275 rows
- **Total Variables:** 22 feature attributes
- **Target Distribution:** 876 positive ignition windows (4.79% class prevalence), 17,399 negative baseline windows.
- **Representative CSV Sample:** `data/sample/terra_fire_matrix_sample.csv` (2,000 rows, 0.34 MB).

### 7.2 Complete Data Dictionary

| Variable | Description | Type | Unit / Values | Source Dataset | Applied Transformation |
| :--- | :--- | :---: | :---: | :--- | :--- |
| `voxel_id` | Unique spatial benchmark monitoring node identifier | `string` | `AGS_V01` – `AGS_V25` | Spatial Monitoring Grid | Canonical topographic lattice assignment |
| `timestamp` | Daily observation timestamp (calendar date) | `date` / `timestamp` | `YYYY-MM-DD` | Multi-source Temporal Baseline | Aligned to Mexican Central Time (GMT-6) |
| `fire_ignition_48h` | **Primary Target:** 1 if wildfire ignition occurs within 48–72h, else 0 | `int32` | $\{0, 1\}$ | NASA FIRMS + CONAFOR | Spatiotemporal buffer ($r \le 0.08^\circ$, $t+1$ to $t+3$ days) |
| `ndmi` | Normalized Difference Moisture Index (Canopy water stress proxy) | `float32` | $[-1.0, 1.0]$ | Copernicus Sentinel-2 MSI | $(B08 - B11) / (B08 + B11)$ phenological model |
| `savi` | Soil-Adjusted Vegetation Index (Foliar density corrected for soil brightness) | `float32` | $[-1.0, 1.0]$ | Copernicus Sentinel-2 MSI | $[(B08 - B04)/(B08 + B04 + 0.5)] \times 1.5$ |
| `nbr` | Normalized Burn Ratio (Combustibility and cured biomass proxy) | `float32` | $[-1.0, 1.0]$ | Copernicus Sentinel-2 MSI | $(B08 - B12) / (B08 + B12)$ |
| `vpd_max_kpa` | Maximum daily Vapor Pressure Deficit | `float32` | $kPa$ ($[0.0, 10.0]$) | ECMWF ERA5-Land Hourly | Tetens formulation: $e_s(T_{max}) - e_a(T_{dew})$ |
| `vpd_72h_max_kpa` | 72-hour antecedent rolling maximum VPD | `float32` | $kPa$ | ECMWF ERA5-Land | 3-day backward rolling maximum window |
| `temp_2m_max_c` | Daily maximum air temperature downscaled by topography | `float32` | $^\circ C$ | ERA5-Land + Copernicus DEM | Adiabatic lapse-rate: $T + \Gamma \cdot (Z_{DEM} - Z_{ref})$ |
| `rh_2m_min_pct` | Minimum daily relative humidity | `float32` | $\%$ ($[0, 100]$) | ECMWF ERA5-Land Hourly | Daily minimum aggregation |
| `wind_u10_mean` | Daily mean zonal (west-to-east) wind component | `float32` | $m/s$ | ECMWF ERA5-Land Hourly | $-ws \cdot \sin(\theta)$ from hourly wind vectors |
| `wind_v10_mean` | Daily mean meridional (south-to-north) wind component | `float32` | $m/s$ | ECMWF ERA5-Land Hourly | $-ws \cdot \cos(\theta)$ from hourly wind vectors |
| `wind_speed_max_kmh` | Peak horizontal wind gust / maximum velocity | `float32` | $km/h$ | ECMWF ERA5-Land Hourly | Daily maximum velocity aggregation |
| `soil_moist_mean` | Mean volumetric soil water content (Layer 1: 0–7 cm depth) | `float32` | $m^3/m^3$ ($[0.0, 0.6]$) | ECMWF ERA5-Land Hourly | Daily arithmetic mean aggregation |
| `days_since_rain` | Consecutive days with precipitation $< 1.0$ mm | `int32` | Days ($[0, 365]$) | ECMWF ERA5-Land Hourly | Cumulative dry spell counter |
| `precip_72h_sum_mm` | 72-hour cumulative precipitation | `float32` | $mm$ | ECMWF ERA5-Land Hourly | 3-day backward rolling cumulative sum |
| `elevation_m` | Physical terrain altitude above sea level | `float32` | Meters ($[1850, 2920]$) | Copernicus GLO-30 DEM | 30 m Digital Elevation Model extraction |
| `slope_deg` | Topographic terrain slope gradient | `float32` | Degrees ($[0^\circ, 90^\circ]$) | Copernicus GLO-30 DEM | First-order geospatial gradient derivation |
| `aspect_rad` | Slope orientation relative to true north | `float32` | Radians ($[0, 2\pi]$) | Copernicus GLO-30 DEM | Azimuthal aspect angle derivation |
| `dist_roads_m` | Euclidean distance to nearest road network | `float32` | Meters | OpenStreetMap / INEGI | Geospatial distance calculation |
| `dist_agri_m` | Euclidean distance to active agricultural parcels | `float32` | Meters | SADER / INEGI Land Use | Geospatial distance calculation |
| `fuel_type` | Dominant ecological vegetative fuel classification | `category` | Categorical descriptors | CONAFOR Forest Inventory | Forest stratum typology |

---

## 8. Final Data Validation

### 8.1 Automated Quality Assurance Suite
The analysis-ready dataset was subjected to a programmatic 7-point validation suite implemented in `src/validate.py`. All seven quality gates achieved **100% PASS** status:

| Validation Check | Expected Condition | Empirical Result | Status |
| :--- | :--- | :--- | :---: |
| **1. Record Integrity** | Exactly 18,275 rows produced (25 monitoring voxels $\times$ 731 calendar days in 2023–2024). | 18,275 records verified. No truncation, row drop, or accidental loss occurred during pipeline execution. | **PASS** |
| **2. Duplicate Control** | Primary composite key uniqueness: 0 duplicate `(voxel_id, timestamp)` observations. | Exactly 0 duplicate pairs detected across the entire dataset. 100% key uniqueness guaranteed. | **PASS** |
| **3. Data Types Compliance** | Rigid embedded Arrow bit-width typing: `string`, `int32`, `float32`, `category`. | 22 out of 22 columns match schema specifications exactly without implicit object/string casting. | **PASS** |
| **4. Missing Values Control** | Zero unhandled or silent nulls ($NaN / None$) across all 22 feature attributes. | 0 null cells detected across all $18,275 \times 22 = 402,050$ matrix data points. | **PASS** |
| **5. Physical Range Boundaries** | All variables strictly respect thermodynamic and geospatial boundaries: $VPD \in [0, 10]$ kPa, Indices $\in [-1, 1]$, Slope $\in [0, 90]^\circ$, Target $\in \{0, 1\}$. | 100% of observations reside within physical laws. No negative moisture or out-of-bounds probabilities. | **PASS** |
| **6. Integration Consistency** | Unbroken temporal continuity across all 731 days of 2023 and 2024 leap year. | Seamless daily progression from 2023-01-01 to 2024-12-31 without temporal gaps. | **PASS** |
| **7. Variable Traceability** | Every feature must trace back to an audited primary data provider and explicit formula. | 100% traceability confirmed across 5 primary sources (CONAFOR, FIRMS, ERA5, Copernicus DEM, Sentinel-2). | **PASS** |

### 8.2 Diagnostic Quality Verification Answers
1. **Did records disappear?** No. The Cartesian product of 25 spatial voxels across 731 continuous days yields exactly 18,275 observations, completely preserved in the final Parquet file.
2. **Were records duplicated?** No. Composite key evaluation `(voxel_id, timestamp)` reveals 0 duplicate occurrences.
3. **Did variable types change correctly?** Yes. High-precision `float64` and generic objects were cast to memory-efficient `float32`, `int32`, and categorical encodings.
4. **Did integration introduce unexpected missing values?** No. All spatial and temporal joins were fully resolved. Zero `NaN` values exist in the final matrix.
5. **Are transformation rules correctly reflected?** Yes. The Tetens equation, vector decomposition, and adiabatic lapse-rate adjustments match theoretical physics.
6. **Can every final variable be traced to its source?** Yes. Fully audited in the Data Dictionary and Transformation Dictionary.
7. **Does the complete pipeline apply the same transformation logic validated using the sample?** Yes. Shared functions in `src/clean.py`, `src/transform.py`, and `src/integrate.py` are executed identically on both full and sample data streams.

---

## 9. ETL Pipeline and Reproducibility

### 9.1 Orchestration Architecture
The complete ETL workflow is codified in modular Python scripts inside `src/` and can be reproduced via either command-line execution or the interactive Jupyter Notebook:

```bash
# Automated end-to-end execution
python -m src.pipeline
```

### 9.2 Reproducibility Dependencies
- **Runtime Environment:** Python 3.10+ (tested on Python 3.12.10).
- **Core Libraries:** `pandas>=2.2.0`, `pyarrow>=15.0.0`, `fastparquet>=2024.2.0`, `openpyxl>=3.1.2`, `numpy>=1.26.0`, `scipy>=1.12.0`.
- **Hardware Footprint:** Peak RAM consumption during full extraction and fusion is **< 120 MB**, requiring only a standard single-node workstation or basic GitHub Codespaces tier (2 vCPUs, 8 GB RAM).

---

## 10. Data Architecture and Scalability

### 10.1 Architecture Classification: Scaled Data Pipeline
The TERRA-FIRE engineering pipeline is formally classified as a **SCALED DATA PIPELINE**:
- **Why Standard Python/Pandas is Optimal:** The active regional pilot dataset comprises 18,275 space-time observations (0.30 MB Parquet, ~15 MB working memory). Vectorized NumPy/Pandas operations execute all thermodynamic formulas, spatial buffers, and aggregations in **under 3.5 seconds**.
- **Why Distributed Big Data (Apache Spark / PySpark) is Inappropriate:** In strict adherence to the teacher's instructions (*"Students will not receive additional credit merely for using Big Data technologies. The selected architecture must be technically justified by the problem and data requirements"*), introducing an Apache Spark cluster for a 72 MB raw dataset would introduce massive JVM initialization overhead, network serialization bottlenecks, and cluster infrastructure costs with negative performance ROI.
- **Future Scalability Path (Nationwide Expansion):** If expanding to 10-meter raster cells across all 1.97 million $\text{km}^2$ of Mexico ($> 10^{10}$ voxels), the pipeline scales naturally through **DuckDB spatial range queries** and partitioned Parquet files (`year=YYYY/month=MM/zone_utm=XX/part-*.parquet`), keeping processing costs low and avoiding monolithic clusters until petabyte-scale streaming is required.

---

## 11. Data Security and External Storage

### 11.1 Zero Credentials in Source Code
- In compliance with security standards, **no passwords, API keys, tokens, or cloud connection secrets are committed** to the GitHub repository.
- Access to external satellite catalogs (Copernicus Data Space, NASA Earthdata) utilizes environment variables (`.env`) excluded via `.gitignore`.
- Raw datasets in `TERRAFIRE-db/` operate under fully public open-data licenses (CONAFOR: Libre Uso MX; NASA: Open Data Policy; ESA: Copernicus Open Access; ECMWF: CC-BY 4.0). No personal identifiable information (PII) or confidential defense data is handled.

---

## 12. GitHub Repository and Version Control

### 12.1 Official Project Repository
- **Repository URL:** [https://github.com/AngelGTZ28/TERRA-FIRE](https://github.com/AngelGTZ28/TERRA-FIRE)
- **Branching Workflow:** Development was executed across independent functional branches:
  - `main`: Production release branch containing functional, documented codebase and Parquet artifacts.
  - `data-cleaning`: Feature branch implementing raw data extraction, structural cleaning, and missing value treatment.
  - `data-integration`: Feature branch implementing thermodynamic transformations, spatial grid generation, and target formulation.
  - `validation`: Feature branch implementing automated quality tests, notebook documentation, and README updates.
- **Meaningful Git Commit History:**
  - `87027a8`: `feat: initialize data engineering directory structure and storage configuration`
  - `7703216`: `feat(clean): implement raw data extraction, structural cleaning and missing value treatment`
  - `9a7b69d`: `feat(integrate): implement physical feature transformation and spatiotemporal matrix integration`
  - `5c6502f`: `test(validation): add automated data validation suite, notebook and comprehensive documentation`
  - Merged cleanly into `main` preserving audit traceability.

---

## 13. Data Engineering Readiness Decision

> [!IMPORTANT]
> ### **OFFICIAL READINESS DECISION: READY FOR ANALYSIS**
> 
> **Technical Justification:**
> 1. **Data Quality & Integrity:** 100% of the 7 automated validation assertions passed. Zero unhandled null values or duplicated composite keys exist in the analytical dataset.
> 2. **Physical Consistency:** All thermodynamic (Tetens VPD) and biophysical indices strictly obey theoretical physics boundaries.
> 3. **Spatiotemporal Integration:** 18,275 space-time observations successfully link continuous hourly weather with discrete satellite anomalies and administrative fire occurrences across 2 full years (2023–2024).
> 4. **Storage Optimization:** Apache Parquet with Snappy compression delivers a 92% storage reduction (0.30 MB) and instantaneous column-pruned deserialization.
> 5. **Reproducibility & Governance:** Fully documented Python modules, interactive notebook, and clear open-data licenses allow any authorized researcher to reproduce the matrix from scratch.

---

## 14. Conclusion
Activity 3 successfully designed and executed a robust, reproducible Data Engineering ETL pipeline for project **TERRA-FIRE**. By addressing real-world planetary and administrative data quality challenges—including malformed metadata headers, non-ASCII character corruptions, disconnected orbital scan times, and negative longitude coordinates—the team created a clean, standardized, and fully validated Feature Store.

Rather than relying on ungrounded synthetic assumptions or over-engineering with unnecessary distributed clusters, the solution adopts a pragmatic **Scaled Data Pipeline** using Python, Pandas, and Apache Parquet. The resulting dataset `terra_fire_spatiotemporal_matrix_v1.parquet` provides 18,275 space-time observations with an anticipatory 48–72h wildfire ignition target label (`fire_ignition_48h`), establishing a verified empirical foundation for subsequent Exploratory Data Analysis, Machine Learning, and TRL 3/4 predictive modeling.

---

## 15. References (APA 7th Edition)

1. Airbus Defence and Space, & European Space Agency. (2022). *Copernicus Digital Elevation Model (GLO-30)*. European Space Agency. https://doi.org/10.5270/ESA-c5d3d65
2. Apache Software Foundation. (2024). *Apache Parquet format specification (Version 2.10)*. Apache Software Foundation. https://parquet.apache.org/documentation/
3. Comisión Nacional Forestal [CONAFOR]. (2024). *Manual de usuario del concentrado histórico de incendios forestales* (Doc ID: 3287). SEMARNAT, Gobierno de México. https://idefor.cnf.gob.mx/documents/3287/download
4. Comisión Nacional Forestal [CONAFOR]. (2025). *Concentrado Nacional de Incendios Forestales 2012–2025: Microdatos oficiales*. Infraestructura de Datos Espaciales Forestales (IDEFOR). https://idefor.cnf.gob.mx/documents/3249/download
5. European Centre for Medium-Range Weather Forecasts [ECMWF]. (2024). *ERA5-Land hourly data from 1950 to present*. Copernicus Climate Change Service (C3S) Climate Data Store (CDS). https://doi.org/10.24381/cds.e2161bac
6. European Space Agency [ESA]. (2024). *Copernicus Sentinel-2 MSI Level-2A: Surface Reflectance Granules*. Microsoft Planetary Computer STAC Catalog. https://planetarycomputer.microsoft.com/dataset/sentinel-2-l2a
7. McKinney, W. (2010). Data structures for statistical computing in Python. In *Proceedings of the 9th Python in Science Conference* (pp. 56–61). https://doi.org/10.25080/Majora-92bf1922-00a
8. Monteith, J. L., & Unsworth, M. H. (2013). *Principles of environmental physics: Plants, animals, and the atmosphere* (4th ed.). Academic Press.
9. National Aeronautics and Space Administration [NASA]. (2025). *VIIRS (S-NPP) 375m active fire detections for Mexico (2023–2024)*. Land, Atmosphere Near real-time Capability for EOS (LANCE) / Fire Information for Resource Management System (FIRMS). https://firms.modaps.eosdis.nasa.gov/
10. Schroeder, W., Oliva, P., Giglio, L., & Csiszar, I. A. (2014). The New VIIRS 375 m active fire detection product: Algorithm description and initial assessment. *Remote Sensing of Environment*, 143, 85–96. https://doi.org/10.1016/j.rse.2013.12.008
11. Tetens, O. (1930). Über einige meteorologische Begriffe. *Zeitschrift für Geophysik*, 6, 297–309.
