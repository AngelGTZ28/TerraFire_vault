---
title: "Acquisition Plan & Readiness Decision"
project: "TERRA-FIRE"
tags:
  - data-acquisition
  - terra-fire
  - readiness
---

## 9. Data Acquisition Plan
The operational protocol defines continuous acquisition, automated ingestion cadences, team responsibilities, and contingency strategies to guarantee pipeline survivability.

## 10. Data Readiness Decision

### 10.1 Quantitative Readiness Evaluation
The results across all five operational phases demonstrate that the technical prerequisites to advance into Data Engineering have been satisfied:
1. **Physical Availability**: 100% of candidate datasets are downloaded, verified on disk, and cryptographically hashed.
2. **Variable Coverage**: 100% of the critical predictive variables (VPD, NDMI, Slope, Aspect, Soil Moisture, Wind Speed, and Ground-Truth Ignition) are either directly available or mathematically derivable from acquired files.
3. **Data Quality**: The candidate inventory achieved a weighted average quality score of 4.53 / 5.0, with no insurmountable quality defects.
4. **Data Governance**: All datasets operate under unrestricted open-data frameworks (Public Domain, Creative Commons, Libre Uso MX, Copernicus Open Licence), presenting zero commercial or academic licensing barriers.
5. **Integration Feasibility**: A clear spatiotemporal linkage (H3 hexagonal tessellation and UTM Zone 13N projection) resolves all coordinate, temporal, and resolution discrepancies.

## 11. Conclusion
This activity successfully designed and implemented an empirical, reproducible Data Acquisition Strategy for project TERRA-FIRE. Rather than relying on simulated or hypothetical values, the team identified, evaluated, and downloaded over 100 MB of real planetary datasets from prestigious national and international bodies: CONAFOR, NASA FIRMS, the European Space Agency, and ECMWF.

The evaluation revealed that while raw datasets exhibit heterogeneity in spatial resolution (from 10 m to 9 km) and temporal cadence (from hourly to 5 days), these differences can be harmonized into a unified spatiotemporal feature matrix through established geospatial downscaling and hexagonal indexing protocols. With all raw data secured and verified, project TERRA-FIRE is fully equipped to enter the Data Engineering phase, where raw data will be transformed into the production feature store that will power anticipatory wildfire predictive intelligence in Mexico.

## 12. References and Dataset Sources
1. Airbus Defence and Space, & European Space Agency. (2022). Copernicus Digital Elevation Model (GLO-30). https://doi.org/10.5270/ESA-c5d3d65
2. Comisión Nacional Forestal [CONAFOR]. (2025). Concentrado Nacional de Incendios Forestales 2012–2025: Microdatos oficiales. https://idefor.cnf.gob.mx/documents/3249/download
3. Comisión Nacional Forestal [CONAFOR]. (2024). Manual de usuario del concentrado histórico de incendios forestales. https://idefor.cnf.gob.mx/documents/3287/download
4. European Centre for Medium-Range Weather Forecasts [ECMWF]. (2024). ERA5-Land hourly data from 1950 to present. https://doi.org/10.24381/cds.e2161bac
5. European Space Agency [ESA]. (2024). Copernicus Sentinel-2 MSI Level-2A: Surface Reflectance Granules. https://planetarycomputer.microsoft.com/dataset/sentinel-2-l2a
6. National Aeronautics and Space Administration [NASA]. (2025). VIIRS (S-NPP) 375m active fire detections for Mexico. https://firms.modaps.eosdis.nasa.gov/data/country/viirs-snpp/
7. Schroeder, W., Oliva, P., Giglio, L., & Csiszar, I. A. (2014). Remote Sensing of Environment. https://doi.org/10.1016/j.rse.2013.12.008
8. Yebra, M., et al. (2013). Remote Sensing of Environment. https://doi.org/10.1016/j.rse.2013.05.029
