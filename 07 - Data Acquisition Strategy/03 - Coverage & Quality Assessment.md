---
title: "Coverage & Quality Assessment"
project: "TERRA-FIRE"
tags:
  - data-acquisition
  - terra-fire
  - data-quality
---

## 3. Dataset Coverage Analysis
To verify whether the candidate datasets collectively satisfy the biophysical and machine learning requirements of the project, an attribute-level mapping was conducted. Each required variable was inspected against the schema of the real acquired data files.

### 3.1 Variable Matching and Status Classification
- **Available**: The exact physical metric exists directly in the dataset without mathematical conversion.
- **Partially Available**: The variable exists but exhibits a limitation in spatial or temporal resolution, requiring interpolation.
- **Derivable**: The physical metric can be rigorously calculated through deterministic mathematical or physical formulas from existing raw bands/fields.
- **Unavailable**: The attribute is completely absent from the candidate dataset.

### 3.2 Critical Data Gaps and Engineering Mitigations
1. **The Canopy Moisture Gap**: No direct ground sensor network measures Live Fuel Moisture Content (LFMC) across Mexican forests.
   *Mitigation*: Handled via Sentinel-2 Band Ratio Derivation (NDMI = [B8 - B11] / [B8 + B11]), which peer-reviewed forestry science confirms correlates with foliar moisture (R^2 > 0.82).
2. **The Micro-Meteorological Scale Disparity**: ERA5-Land outputs meteorological metrics on a 9 km grid, which misses convective heating inside steep mountain ravines.
   *Mitigation*: Handled via Topographic Lapse-Rate Downscaling, applying an adiabatic lapse rate (-6.5°C/km) using the 30 m Copernicus DEM elevations.
3. **The Temporal Reporting Bias in CONAFOR**: CONAFOR records note the calendar date a fire was reported by local landowners or brigades, often 12 to 48 hours after actual ignition.
   *Mitigation*: Handled via Spatiotemporal Cross-Matching with NASA FIRMS VIIRS, anchoring the true ignition time to the first orbital thermal pixel detection within a 2 km radius.

## 4. Data Quality Assessment
A rigorous, quantitative evaluation of data quality was performed across six recognized data engineering dimensions:
- **Completeness**: Absence of missing values, nulls, or truncated records in essential fields.
- **Consistency**: Internal structural harmony of data types, naming conventions, formats, and physical units.
- **Validity**: Adherence of values to expected ranges, geographic coordinate bounds, and domain definitions.
- **Timeliness**: Currency, latency between physical event and digital ingestion, and historical continuity.
- **Accuracy**: Representativeness of real physical phenomena and precision of instruments.
- **Relevance**: Direct empirical utility of the dataset toward predicting 48–72h wildfire ignition.

Each candidate dataset was rated from 1 (Very Poor) to 5 (Very Good) based on the empirical inspection of the downloaded files.

### 4.1 Detailed Analysis of Quality Findings
- **CONAFOR Incident Data Inspection**: Analysis of CONAFOR_Incendios_2012_2025.xlsx reveals that while columns like Latitud, Longitud, Fecha Inicio, and Total hectareas are >99% populated, certain contextual columns such as Causa especifica and Predio contain unstandardized text and trailing spaces. This necessitates a string-stripping and categorical encoding step in Data Engineering.
- **NASA FIRMS VIIRS Data Inspection**: Analysis of NASA_FIRMS_VIIRS_SNPP_2023_Mexico.csv demonstrates strict schema compliance. The confidence column categorizes detections into categorical bins (l = low, n = nominal, h = high), allowing the pipeline to filter out low-confidence detections and retain high-fidelity thermal triggers.
- **ERA5-Land Continuous Integrity**: The acquired 17,544-row series from Open-Meteo exhibits zero temporal gaps from January 1, 2023 00:00 to December 31, 2024 23:00. Thermodynamic calculations for Vapor Pressure Deficit (VPD) can be derived without filling artificial values.
