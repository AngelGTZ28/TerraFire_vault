---
title: "Candidate Dataset Inventory"
project: "TERRA-FIRE"
tags:
  - data-acquisition
  - terra-fire
  - datasets
---

## 2. Candidate Dataset Inventory

To satisfy the technical specifications formulated in Section 1, an extensive search across national government portals, planetary Earth Observation archives, and atmospheric reanalysis repositories was conducted. Five primary candidate datasets were located, inspected, and acquired.

### Detailed Candidate Dataset Profiles

#### 1. CONAFOR - Registro Histórico de Incendios Forestales (2012–2025)
- **Provider**: Comisión Nacional Forestal (CONAFOR), Secretaría de Medio Ambiente y Recursos Naturales (SEMARNAT), Gobierno de México.
- **Discovered via**: Sistema Nacional de Información Forestal (SNIF) and Infraestructura de Datos Espaciales Forestales (IDEFOR) Open Data repository (https://idefor.cnf.gob.mx/documents/3249/download).
- **Format**: Microsoft Excel OpenXML Spreadsheet (.xlsx) containing 101,004 individual fire records, accompanied by the official User Manual and Data Dictionary (Manual_de_usuario_historico_incendios.pdf, Document ID: 3287).
- **Coverage**: National (all 32 Federal Entities of Mexico), covering January 1, 2012 to December 31, 2025.
- **Size**: 17.75 MB (uncompressed table >100,000 rows \times 35 tabular attributes).
- **Update Cadence**: Annual official consolidation with preliminary monthly updates during peak fire season.
- **Access Method**: Direct HTTPS programmatic retrieval from IDEFOR repository.
- **Potential Use**: Primary ground-truth supervisory dataset providing historical ignition coordinates, initiation dates, detection dates, extinguishment dates, total affected surface (hectares of tree, shrub, and herbaceous stratum), and physical fire causes.

#### 2. NASA FIRMS - VIIRS Active Fire Detections (375 m S-NPP)
- **Provider**: National Aeronautics and Space Administration (NASA) / Land, Atmosphere Near real-time Capability for EOS (LANCE) / Fire Information for Resource Management System (FIRMS).
- **Discovered via**: NASA Earthdata FIRMS Country Summary Download Portal (https://firms.modaps.eosdis.nasa.gov/data/country/viirs-snpp/).
- **Format**: Comma-Separated Values (.csv).
- **Coverage**: National territorial bounding box of Mexico; verified files acquired for calendar years 2023 (327,657 detections) and 2024 (331,180 detections).
- **Size**: 24.91 MB (2023 file) + 25.08 MB (2024 file).
- **Update Cadence**: Near-Real-Time (NRT) updated within 3 hours of orbital pass; archived science-quality releases validated semi-annually.
- **Access Method**: Public HTTPS direct repository download and RESTful API (/api/area/ or country summaries).
- **Potential Use**: Independent spatial-temporal ground-truth validation; anchors exact satellite thermal detection timestamps (to within 12 hours) eliminating bureaucratic logging latency in CONAFOR records; provides Fire Radiative Power (FRP in Megawatts) and Brightness Temperature (Band I-4 and I-5).

#### 3. ECMWF ERA5-Land - Surface Reanalysis Climate Data
- **Provider**: European Centre for Medium-Range Weather Forecasts (ECMWF) under the European Union's Copernicus Climate Change Service (C3S).
- **Discovered via**: Copernicus Climate Data Store (CDS) API and verified via Open-Meteo High-Resolution Historical Reanalysis API (https://archive-api.open-meteo.com/v1/archive).
- **Format**: Comma-Separated Values (.csv) and NetCDF-4 multidimensional raster grids.
- **Coverage**: Global land coverage at 0.1^\circ resolution (~9 km grid); complete continuous hourly dataset acquired for the regional testbed of Sierra Fría (22.18°N, -102.60°W, elevation 2,595 m) for 2023–2024 (17,544 continuous hourly time-steps).
- **Size**: 0.89 MB (regional pilot CSV); multi-gigabyte coverage available for full national extent via CDS NetCDF.
- **Update Cadence**: Hourly reanalysis data published with a 5-day latency behind real time.
- **Access Method**: Programmatic REST API queries and CDS API tokens (cdsapi).
- **Potential Use**: Hourly thermodynamic baseline to compute Vapor Pressure Deficit (VPD in kPa) from 2m air temperature and dew point; provides surface wind vectors (U10, V10), volumetric soil water (0–7 cm Layer 1), and antecedent drought indices (days without measurable precipitation).

#### 4. Copernicus DEM (GLO-30) - High-Resolution Global Digital Elevation Model
- **Provider**: European Space Agency (ESA), Airbus Defence and Space, and Copernicus Programme.
- **Discovered via**: AWS Open Data Registry (s3://copernicus-dem-30m/) and Copernicus Data Space Ecosystem.
- **Format**: Cloud-Optimized GeoTIFF (COG), 32-bit floating point elevation values in meters relative to the EGM2008 geoid.
- **Coverage**: Tile Copernicus_DSM_COG_10_N22_00_W103_00_DEM covering 22^\circ\text{N}–23^\circ\text{N}, 103^\circ\text{W}–102^\circ\text{W} (embracing the Sierra Fría biological corridor and central-western volcanic plateau).
- **Size**: 35.44 MB per 1^\circ \times 1^\circ tile.
- **Update Cadence**: Static baseline release (Version 2021/2022).
- **Access Method**: Public HTTPS download from AWS Open Data S3 endpoints without authentication.
- **Potential Use**: High-precision derivation of terrain slope (0°–90°), aspect (solar radiation accumulation angle), topographic wetness index (TWI), and physical elevation for atmospheric lapse-rate temperature downscaling.

#### 5. Copernicus Sentinel-2 MSI - Multispectral Surface Reflectance (Level-2A)
- **Provider**: European Space Agency (ESA) / European Commission Copernicus Programme.
- **Discovered via**: Microsoft Planetary Computer STAC API and ESA Copernicus Data Space Ecosystem (https://planetarycomputer.microsoft.com/api/stac/v1/search).
- **Format**: Cloud-Optimized GeoTIFF (COG) rasters accessed via SpatioTemporal Asset Catalog (STAC) metadata JSON items.
- **Coverage**: 100 km \times 100 km MGRS tile T13QGE (Sierra Fría / Aguascalientes / Zacatecas border), captured during peak dry season (e.g., April 11, 2024, Cloud Cover 3.53%).
- **Size**: ~500 MB per full multispectral granule; individual index layers (B8 NIR, B11 SWIR-1, B4 Red) extracted on-demand via range requests.
- **Update Cadence**: 5-day revisit frequency (combining Sentinel-2A and Sentinel-2B).
- **Access Method**: STAC API programmatic catalog queries with direct HTTPS streaming of COG assets.
- **Potential Use**: Derivation of Live Fuel Moisture Content (LFMC) proxy through Normalized Difference Moisture Index (NDMI = [B8 - B11] / [B8 + B11]), Soil-Adjusted Vegetation Index (SAVI), and Normalized Burn Ratio (NBR).
