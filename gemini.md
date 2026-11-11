# 🧠 TERRA-FIRE: Master Project Memory & Context (`gemini.md`)
> **AI Assistant Reference Manual & Technical Knowledge Base**  
> **Last Updated:** November 10, 2026 | **Project Status:** TRL 3 Validated ➔ **READY FOR SEGMENTATION** (Data Science Act. 3–6 Complete) & **READY FOR TRANSFORMATION** (Disruptive Technologies Act. 4 Blueprint Complete — Score 9.43/10)

---

## 📌 1. Project Identity & Governance
* **Project Name:** **TERRA-FIRE** (Predictive Wildfire Intelligence & Offline Tactical Cartography Engine)
* **Mission:** Transition Mexico's forest fire management from reactive suppression to anticipatory, micro-territorial (10–20 m) mitigation **48 to 72 hours prior to ignition**.
* **Target Users:** 
  1. *Rural ejidatarios & farmers:* Safe agricultural burn advisories (NOM-015-SEMARNAT/AGRICULTURA-2023) via a 3-color Visual Semaphore.
  2. *Community fire brigades:* 100% offline tactical risk cartography and escape route navigation in remote mountain corridors (`< 12 MB` `.pbf` vector tiles).
  3. *CONAFOR & Civil Protection dispatchers:* Anticipatory territorial resource pre-allocation (`SOP-72H`) and **TreeSHAP** Local Risk Cards.
* **Institution:** Universidad Tecnológica El Retoño (UTR BIS) — Aguascalientes, México.
* **Academic Program:** Information Technologies and Digital Innovation Engineering (`LITD9A`).
* **Courses:** Data Science, Disruptive Technologies & Integrative Project III (Sep–Dec 2026).
* **Advising Professor:** Dr. Sergio Valadez Godínez.
* **Engineering Team:** 
  - Angel Emilio Gutierrez Lozano (ID: 4341)
  - Emiliano Betanzos Valtierra (ID: 4795)

---

## 🏛️ 2. Architectural Ecosystem & Workspace Directories
The project ecosystem is organized across peer directories in `/home/angel/Workspace/TERRA-FIRE-PROJECT/`:

```text
TERRA-FIRE-PROJECT/
├── TERRA-FIRE/             # 🛠️ Primary GitHub Code Repository (ETL, EDA, Regression, PCA, Notebooks, docs/)
├── TERRA-FIRE-DATABASES/   # 📦 External Raw Datasets Storage (>72 MB)
└── TerraFire_vault/        # 📚 Obsidian Knowledge Vault & Official Academic Reports
```

### The 4 Decoupled Computing Layers:
1. **Layer 1: Project Repository (GitHub):** Source code (`src/`), executable notebooks (`notebooks/`), metadata dictionaries (`metadata/`), visual analytics (`reports/figures/`), transformation strategy (`docs/transformation/`), deliverable reports (`work/`), `.gitignore`, `requirements.txt`, small representative samples (`data/sample/`), and compressed Parquet artifacts (`data/processed/`).
2. **Layer 2: Development Environment (VS Code / Linux Workstation):** Python 3.12+ virtual environment (`.venv`) with pinned scientific dependencies (`pandas`, `pyarrow`, `numpy`, `scipy`, `statsmodels`, `scikit-learn`, `matplotlib`, `seaborn`, `plotly`).
3. **Layer 3: Data Storage:** Heavy raw tables (>72 MB) stored externally in `TERRA-FIRE-DATABASES/` (excluded from Git).
4. **Layer 4: Data Processing:** Vectorized in-memory compute infrastructure (Python + Pandas/PyArrow/Statsmodels/Scikit-Learn) using a **Scaled Data Pipeline** architecture (executing full ETL, descriptive statistics, 12-model regression suites, and 12-to-3 PCA dimensionality reduction in `< 4.0 s`).

---

## 🛰️ 3. Primary Datasets & Ingestion Peculiarities

| Dataset | Provider | Records & Size | Storage Path | Ingestion Peculiarities & Mitigations |
| :--- | :--- | :---: | :--- | :--- |
| **CONAFOR Historical Fires (2012–2025)** | CONAFOR / SEMARNAT | 101,003 rows<br>(18.6 MB `.xlsx`) | `TERRA-FIRE-DATABASES/CONAFOR_Incendios_2012_2025.xlsx` | • Headers contain corrupted non-ASCII accents (`'Ao'`, `'Herbceo'`).<br>• 48 records have positive longitudes (inverted by $\times -1.0$).<br>• 946 null vegetation rows imputed as `'No Especificado'`.<br>• Strata hectares nulls imputed as `0.0` ha. |
| **NASA FIRMS VIIRS S-NPP (2023–2024)** | NASA LANCE / FIRMS | 657,791 rows<br>(52.4 MB `.csv`) | `TERRA-FIRE-DATABASES/NASA_FIRMS_VIIRS_SNPP_*.csv` | • `acq_time` is integer (e.g. `820`); zero-padded to `08:20:00` and concatenated with `acq_date` to form UTC timestamp.<br>• Filtered to Mexico bounding box $[14.0, 33.5]^\circ\text{N}, [-118.5, -86.0]^\circ\text{W}$. |
| **ECMWF ERA5-Land Hourly** | Copernicus C3S | 17,544 rows<br>(0.93 MB `.csv`) | `TERRA-FIRE-DATABASES/ERA5_Land_Hourly_SierraFria_2023_2024.csv` | • **Crucial:** Lines 1–2 contain station metadata; line 3 is blank; table header is at line 4. Must be loaded using `skiprows=3`.<br>• Local time is GMT-6; UTC offset (+6h) added for satellite alignment. |
| **Copernicus DEM (GLO-30)** | ESA / Airbus | 1°x1° Tile<br>(35.4 MB `.tif`) | `TERRA-FIRE-DATABASES/Copernicus_DEM_GLO30_N22_W103.tif` | • 32-bit float elevation values relative to EGM2008.<br>• Used to compute slope ($0^\circ–90^\circ$), aspect, and lapse-rate thermal downscaling. |
| **Copernicus Sentinel-2 MSI L2A** | ESA / Microsoft PC | Scene Item<br>(0.03 MB `.json`) | `TERRA-FIRE-DATABASES/Sentinel2_L2A_STAC_Item_*.json` | • Multispectral surface reflectance metadata (B04 Red, B08 NIR, B11 SWIR-1, B12 SWIR-2).<br>• Precomputed tabular biophysical indices (`ndmi`, `savi`, `nbr`) integrated in the Parquet feature store. |

---

## ⚗️ 4. Mathematical Formulations & Feature Engineering

### 1. Tetens Equation for Vapor Pressure Deficit ($VPD$)
Evaporative atmospheric suction desiccation force:
$$e_s(T) = 0.61078 \exp\left(\frac{17.27 \cdot T}{T + 237.3}\right) \quad [kPa]$$
$$e_a(T_{dew}) = 0.61078 \exp\left(\frac{17.27 \cdot T_{dew}}{T_{dew} + 237.3}\right) \quad [kPa]$$
$$VPD = \max(0.0, e_s(T) - e_a(T_{dew})) \quad [kPa]$$

### 2. Environmental Lapse-Rate Topographic Downscaling
Correcting coarse 9 km reanalysis temperature to microtopographic elevations:
$$T_{downscaled} = T_{ref} + \Gamma \cdot (Z_{DEM} - Z_{ref})$$
Where $\Gamma = -0.0065 \, ^\circ C/m$, $Z_{ref} = 2595$ m (Sierra Fría station elevation).

### 3. Horizontal Wind Vector Decomposition
Resolves 360° circular discontinuity into continuous Euclidean forces:
$$u_{10} = -(ws_{kmh} / 3.6) \cdot \sin(\theta_{rad}) \quad (\text{zonal, west-to-east})$$
$$v_{10} = -(ws_{kmh} / 3.6) \cdot \cos(\theta_{rad}) \quad (\text{meridional, south-to-north})$$

### 4. Biophysical Indices (Sentinel-2 MSI)
- **Normalized Difference Moisture Index (NDMI):** $NDMI = \frac{B08 - B11}{B08 + B11}$ (Canopy water stress proxy).
- **Soil-Adjusted Vegetation Index (SAVI):** $SAVI = \frac{B08 - B04}{B08 + B04 + 0.5} \times 1.5$ (Foliar density adjusted for bright soil).
- **Normalized Burn Ratio (NBR):** $NBR = \frac{B08 - B12}{B08 + B12}$ (Biomass combustibility proxy; pruned in Activity 5 & 6 due to $\text{VIF} > 100$ collinearity with `ndmi`).

---

## 📊 5. Analysis-Ready Dataset (`matrix_v1.parquet`) Specification

* **Path:** `data/processed/terra_fire_spatiotemporal_matrix_v1.parquet` (Immutable; do not modify)
* **Format:** Apache Parquet with Snappy compression (0.30 MB, 92% compression vs CSV).
* **Dimensions:** 18,275 rows $\times$ 22 columns (25 regional monitoring nodes $\times$ 731 continuous days across 2023–2024).
* **Missing Values:** 0 across all 402,050 cells (100% complete).
* **Target Label (`fire_ignition_48h`):** Binary $\{0, 1\}$. Evaluated via spatial buffer ($r \le 0.08^\circ \approx 8.5$ km) and 48–72h forward-looking predictive window ($t+1$ to $t+3$ days).
  - Positive ignition windows: **876** (4.79% class prevalence; imbalance ratio $1 : 19.86$).
  - Negative baseline windows: **17,399** (95.21%).

### Summary Data Dictionary:
`voxel_id` (string), `timestamp` (date), `fire_ignition_48h` (int32), `ndmi` (float32), `savi` (float32), `nbr` (float32), `vpd_max_kpa` (float32), `vpd_72h_max_kpa` (float32), `temp_2m_max_c` (float32), `rh_2m_min_pct` (float32), `wind_u10_mean` (float32), `wind_v10_mean` (float32), `wind_speed_max_kmh` (float32), `soil_moist_mean` (float32), `days_since_rain` (int32), `precip_72h_sum_mm` (float32), `elevation_m` (float32), `slope_deg` (float32), `aspect_rad` (float32), `dist_roads_m` (float32), `dist_agri_m` (float32), `fuel_type` (category).

---

## 🔬 6. Empirical Intelligence & Variable Impact Reference (Data Science Activities 4, 5 & 6)

### A. Key Group Contrasts (Activity 4 — Data Intelligence Lab)
- **Anthropogenic Proximity Shift:** `dist_agri_m` drops from a baseline mean of $1,650.7\text{ m}$ (median $1,200\text{ m}$) to **$651.6\text{ m}$** (median **$420\text{ m}$**, $\Delta = -60.53\%, p < 10^{-30}$) during ignitions; `dist_roads_m` drops from median $480\text{ m}$ to **$150\text{ m}$** ($\Delta = -62.32\%$).
- **Ecological Combustible Dominance:** *Pastizal Inducido* accounts for **63.58%** of all statewide ignitions (557 / 876 positive events, 15.24% internal fire rate), followed by *Matorral Xerófilo* (**17.92%**, 157 fires) and *Matorral Submontano* (**13.47%**, 118 fires). Pure temperate forests (*Bosque de Pino* & *Encino*) contribute $< 2.1\%$ combined.
- **Thermodynamic Pre-Conditioning:** In ignition windows, `vpd_max_kpa` surges by **+16.38%** (mean $2.21\text{ kPa}$, median $2.09\text{ kPa}$), `temp_2m_max_c` rises by **+11.33%** ($26.29^\circ\text{C}$ vs $23.61^\circ\text{C}$), `rh_2m_min_pct` plunges by **-25.78%** (median **$18.0\%$** vs $26.0\%$), and `ndmi` drops by **-42.50%** ($0.0760$ vs $0.1322$).

### B. Correlation & Regression Benchmark Reference (Activity 5 — Variable Impact Analysis)
1. **Top Target Correlations with `fire_ignition_48h` ($N = 18,275$):**
   - `dist_agri_m`: Pearson $r = -0.1619$, Spearman $\rho = -0.2155$ ($p = 6.36 \times 10^{-191}$, Cohen's $d = -0.993$)
   - `slope_deg`: Pearson $r = -0.1891$, Spearman $\rho = -0.2109$ ($p = 7.83 \times 10^{-183}$, Confounded)
   - `elevation_m`: Pearson $r = -0.1866$, Spearman $\rho = -0.2070$ ($p = 5.20 \times 10^{-176}$, Confounded)
   - `dist_roads_m`: Pearson $r = -0.1519$, Spearman $\rho = -0.2063$ ($p = 7.89 \times 10^{-175}$, Cohen's $d = -0.922$)
   - `temp_2m_max_c`: Pearson $r = +0.1325$, Spearman $\rho = +0.1281$ ($p = 2.09 \times 10^{-72}$, Cohen's $d = +0.648$)
   - `rh_2m_min_pct`: Pearson $r = -0.0992$, Spearman $\rho = -0.1035$ ($p = 9.62 \times 10^{-45}$, Cohen's $d = -0.507$)
   - `soil_moist_mean`: Pearson $r = -0.0936$, Spearman $\rho = -0.0941$ ($p = 3.20 \times 10^{-37}$, Cohen's $d = -0.475$)
   - `vpd_max_kpa`: Pearson $r = +0.0853$, Spearman $\rho = +0.0857$ ($p = 3.57 \times 10^{-31}$, Cohen's $d = +0.396$)
   - `ndmi`: Pearson $r = -0.0673$, Spearman $\rho = -0.0702$ ($p = 2.18 \times 10^{-21}$, Cohen's $d = -0.331$)
   - `wind_v10_mean`: Pearson $r = -0.0037$, Spearman $\rho = +0.0007$ ($p = 0.621$, **Statistically Non-Significant Noise**)

2. **Validated OLS Regression Equations (`statsmodels.api.OLS`):**
   - **M1 (RH $\to$ VPD):** $\widehat{VPD}_{max} = 3.0514 - 0.03929 \cdot RH_{min}$ ($R^2 = 0.6802, t = -197.13$)
   - **M2 (Temp $\to$ VPD):** $\widehat{VPD}_{max} = -1.4209 + 0.14033 \cdot T_{max}$ ($R^2 = 0.6058, t = +167.56$)
   - **M3 (VPD $\to$ Soil Moisture):** $\hat{\theta}_{soil} = 0.3852 - 0.07682 \cdot VPD_{max}$ ($R^2 = 0.5240, t = -141.83$)
   - **M4 (Soil Moisture $\to$ NDMI):** $\widehat{NDMI} = -0.1767 + 1.28466 \cdot \theta_{soil}$ ($R^2 = 0.3528, t = +99.80$)
   - **M5 (Orographic Lapse Rate):** $\hat{T}_{max} = 38.4385 - 0.00650 \cdot Z_{elev}$ ($R^2 = 0.2155, t = -70.84$, recovers exact $\Gamma = -6.50^\circ\text{C/km}$)
   - **M6 (Valley Spatial Confounding):** $\widehat{\text{Dist}}_{agri} = -7580.90 + 4.06179 \cdot Z_{elev}$ ($R^2 = 0.9000, r = +0.9487, t = +405.51$)
   - **M9–M12 (20-Quantile Binned Ignition Probability % Regressions):**
     - `temp_2m_max_c`: $\hat{P}_{ign}(\%) = -10.6620 + 0.65092 \cdot T_{max}$ ($R^2 = 0.8930, p = 3.59 \times 10^{-10}$)
     - `rh_2m_min_pct`: $\hat{P}_{ign}(\%) = 8.5265 - 0.12904 \cdot RH_{min}$ ($R^2 = 0.8232, p = 3.41 \times 10^{-8}$)
     - `vpd_max_kpa`: $\hat{P}_{ign}(\%) = 0.3326 + 2.33775 \cdot VPD_{max}$ ($R^2 = 0.7816, p = 2.34 \times 10^{-7}$)
     - `soil_moist_mean`: $\hat{P}_{ign}(\%) = 10.5973 - 24.33603 \cdot \theta_{soil}$ ($R^2 = 0.7803, p = 2.47 \times 10^{-7}$)

3. **Variable Impact Classification & Feature Pruning Rules:**
   - **High Impact (7 Quantitative + 1 Categorical — Primary Modeling Core):** `dist_agri_m`, `dist_roads_m`, `temp_2m_max_c`, `rh_2m_min_pct`, `soil_moist_mean`, `vpd_max_kpa`, `ndmi`, and `fuel_type`.
   - **Medium Impact (6 — Include with Spatial Blocking / Non-Linear Trees):** `slope_deg`, `elevation_m`, `vpd_72h_max_kpa`, `precip_72h_sum_mm`, `days_since_rain`, `savi`.
   - **Low Impact / Prune Candidates (5):** Prune `nbr` ($\text{VIF} > 100$) and `wind_v10_mean` ($p = 0.621$); transform `aspect_rad` to solar southness $-\cos(\text{aspect\_rad})$; reserve `wind_speed_max_kmh` & `wind_u10_mean` for post-ignition spread modeling.

### C. Principal Component Analysis & Pattern Discovery Reference (Activity 6 — Pattern Discovery Challenge)
1. **Unified 12-to-3 Spatiotemporal PCA Dimensionality Reduction (`StandardScaler` + `PCA(n_components=3)`):**
   - Compresses the 12 standardized High & Medium-Impact variables into `X_pca_reduced` ($18,275 \times 3$ `['PC1', 'PC2', 'PC3']`), achieving **75.0% dimensionality reduction while retaining 87.87% of total variance** ($\text{VIF} = 1.000$) under the Kaiser Criterion ($\lambda_k \ge 1.0$).
   - **$\text{PC1}$ ($\lambda_1 = 4.8918, 40.76\%$ variance):** *Atmospheric-Edaphic Desiccation & Drought Stress Continuum* (`vpd_max_kpa` $+0.3900$, `vpd_72h_max_kpa` $+0.3685$, `temp_2m_max_c` $+0.3304$, `days_since_rain` $+0.3033$ vs. `rh_2m_min_pct` $-0.3896$, `soil_moist_mean` $-0.3829$). Cohen's $d = +0.760$.
   - **$\text{PC2}$ ($\lambda_2 = 4.0088, 33.41\%$ variance):** *Orographic Altitude vs. Anthropogenic Agricultural Valley Interface* (`slope_deg` $+0.4592$, `dist_agri_m` $+0.4587$, `elevation_m` $+0.4560$, `dist_roads_m` $+0.4558$). Cohen's $d = -0.738$.
   - **$\text{PC3}$ ($\lambda_3 = 1.6440, 13.70\%$ variance):** *Vegetative Canopy Phenology & Warm Monsoon Hydration Regime* (`ndmi` $+0.6389$, `temp_2m_max_c` $+0.4598$, `vpd_72h_max_kpa` $+0.3409$, `precip_72h_sum_mm` $+0.3325$).
2. **Hidden Patterns & Separation Zones Discovered (`fig21`–`fig27`):**
   - **Quadrant IV Pyro-Anthropogenic Convergence ($\text{PC1} > 0 \land \text{PC2} \le 0$):** Contains $28.50\%$ of observations ($5,208\text{ rows}$) but captures **68.61% of all wildfires ($601 / 876$)** at an **11.54% ignition rate** ($28.1\times$ higher than Quadrant II's $0.41\%$).
   - **Extreme Pyro-Anthropogenic Apex ($\text{PC1} > +2.5 \land \text{PC2} < -1.0, N = 604$):** Reaches a **23.34% wildfire ignition rate** ($141\text{ fires}$, $56.9\times$ Quadrant II).
   - **Composite Latent Super-Feature ($\text{Pyro\_PC\_Index} = \text{PC1} - \text{PC2}$):** Achieves Cohen's $d = +1.0586$ ($t = +35.80, p = 1.29 \times 10^{-195}$).

---

## 🚀 7. Digital Transformation Blueprint Reference (Disruptive Technologies — Activity 4)

### 1. Paradigm Shift: Digitization $\to$ Digitalization $\to$ Digital Transformation
- **Digitization:** Paper historical logs and NOM-015 permits converted to static spreadsheets.
- **Digitalization:** Displaying post-ignition NASA FIRMS thermal hotspots on urban dashboards without altering the 3–12h reactive workflow.
- **Digital Transformation (TERRA-FIRE):** Reconfiguring people, processes, technology, and culture to transition from **3–12h post-ignition reactive suppression** to **48–72h pre-ignition anticipatory prevention**, decentralizing spatial intelligence to disconnected *ejidos* and community brigades.

### 2. Core Socio-Technical Mechanisms & Governance Innovations
- **Non-Punitive Ejidal Data Charter:** Formal agreement signed in *Asambleas Ejidales* guaranteeing that the TERRA-FIRE Burn Semaphore is read-only and never used to issue SEMARNAT fines, neutralizing rural surveillance resistance.
- **3-Color NOM-015 Burn Semaphore:** Intuitive visual traffic light (Green / Yellow / Red) advising farmers to defer *roza y quema* for 48 hours when $VPD_{max} > 2.0\text{ kPa}$ and $RH_{min} < 20\%$.
- **Preventive Dispatch Protocol (`SOP-72H`):** Institutional standard operating procedure triggered by the daily 06:00 AM TreeSHAP Intelligence Briefing to pre-position CONAFOR/Civil Protection brigades and water tankers in **PCA Quadrant IV** borders 48–72h before peak desiccation.
- **Network of *"Promotores Digitales Forestales"* & Wi-Fi Sync Kiosks:** Local rural youth champions and QR-enabled municipal/ejidal Wi-Fi access points enabling `< 15 second` offline synchronization of `< 12 MB` `.pbf` vector tiles into `IndexedDB`.

### 3. Prosci ADKAR & Change Management KPIs
- **Weekly Offline Tile Sync Rate Target:** $\ge 85\%$ of active brigade devices and *Comisariados*.
- **Red-Alert Burn Deferral Compliance Target:** $\ge 75\%$ voluntary deferral of agricultural burns during Red Alert windows.
- **Preventive Pre-Allocation Lead Time Target:** $\ge 48\text{ hours}$ prior to peak hazard window.
- **System Usability Scale (SUS) Target:** $\ge 80 / 100$.
- **Expected Socio-Ecological Impact:** **30%–50% reduction** in pasture-to-forest fire escapes (*Pastizal Inducido*), **25%–40% savings** in reactive helicopter suppression costs, and **Zero Hardware CapEx** (`< $15 USD/month` cloud batch compute).

### 4. Five-Stage Implementation Roadmap (12-Month Horizon) & Readiness Decision
1. **Stage 1 — Preparation (Months 1–2):** Steering Committee formation, Non-Punitive Charter signing, `SOP-72H` drafting, and 5 Municipal Wi-Fi Sync Kiosks audit.
2. **Stage 2 — Capability Development (Months 3–4):** 02:00 UTC automated cloud-to-edge pipeline deployment, Offline MapLibre PWA launch, accreditation of 15 *Promotores Digitales*, and Tier 1–3 training workshops.
3. **Stage 3 — Pilot Implementation (Months 5–7 | Spring Dry Season):** Live field pilot in Sierra Fría & Quadrant IV nodes, parallel shadow operations alongside SPPIF, and bi-weekly UX sprints.
4. **Stage 4 — Deployment (Months 8–10):** Full statewide rollout across all 25 monitoring nodes in Aguascalientes, formal `SOP-72H` institutionalization, and *"Ejido Preventivo Certificado"* awards.
5. **Stage 5 — Continuous Improvement (Months 11–12+):** Post-season XGBoost retraining (`matrix_v2.parquet`), **Sentinel-1 C-SAR** microwave cloud-penetration fusion, and multi-state scaling kit (Jalisco, Zacatecas, Durango).
- **Official Transformation Assessment Verdict:** **`READY FOR TRANSFORMATION`** (**Composite Score: 9.43 / 10.0**).

---

## 💻 8. Quick Execution & Command Reference

### Run Standalone Analytical Engines
```bash
# Activity 3 (Data Science): Full ETL Pipeline & 7-Gate QA Validation
python -m src.pipeline

# Activity 4 (Data Science): Descriptive Statistics & Visual Dashboards (fig01 - fig12)
python src/data_intelligence_analysis.py

# Activity 5 (Data Science): Correlation, OLS Regressions, VIF & Impact Ranking (fig13 - fig20)
python src/variable_impact_analysis.py

# Activity 6 (Data Science): Multivariate PCA (12 -> 3 Dimensions) & Pattern Discovery (fig21 - fig27)
python src/pattern_discovery_challenge.py
```

---

## 🗺️ 9. Project Roadmap & Upcoming Steps
1. **Data Science Act. 3 (Completed):** Data Engineering Lab — ETL pipeline, Parquet Feature Store, and 7-gate validation suite (**READY FOR ANALYSIS**).
2. **Data Science Act. 4 (Completed):** Data Intelligence Lab — Central tendency, dispersion, Welch's $t$-tests, and 12 visual dashboards (**READY FOR ADVANCED ANALYSIS**).
3. **Data Science Act. 5 (Completed):** Variable Impact Analysis — Pearson/Spearman correlations, 12 OLS regressions, VIF multicollinearity diagnostics, confounding proof, and Variable Impact Ranking (**READY FOR PATTERN DISCOVERY**).
4. **Data Science Act. 6 (Completed):** Pattern Discovery Challenge — Unified 12-to-3 Spatiotemporal PCA (`PCA(n_components=3)` retaining $87.87\%$ variance in `['PC1', 'PC2', 'PC3']`), Quadrant IV discovery ($68.61\%$ of fires), seasonal hysteresis loop, and Hotelling's $T^2$ outlier diagnostics (`fig21`–`fig27`, **READY FOR SEGMENTATION**).
5. **Disruptive Technologies Act. 4 (Completed):** Digital Transformation Blueprint — Current State Assessment, Opportunity Matrix, Future-State Blueprint (`SOP-72H`, Non-Punitive Ejido Charter, TreeSHAP Risk Cards, Offline PWA), Capability Gap Analysis, Stakeholder Adoption Strategy, Prosci ADKAR Change Management Plan, and 5-Stage Implementation Roadmap (**READY FOR TRANSFORMATION — 9.43/10**).
6. **Next Data Science Activity (Intelligent Segmentation Lab):** Unsupervised clustering ($K$-Means, Gaussian Mixture Models, DBSCAN) in the orthogonal 3D PCA subspace (`['PC1', 'PC2', 'PC3']`) evaluated via Silhouette Score and Davies-Bouldin Index.
7. **Subsequent Activities (Machine Learning Challenge & Model Performance Validation):** 5-Fold Spatially Blocked Cross-Validation (`GroupKFold` by `voxel_id`) with XGBoost & LightGBM (`scale_pos_weight = 19.86`); PR-AUC, Brier Score calibration, and TreeSHAP explainability.
