---
title: "Selection & Integration Feasibility"
project: "TERRA-FIRE"
tags:
  - data-acquisition
  - terra-fire
  - integration
---

## 7. Dataset Selection
A multi-criteria comparative evaluation was performed across the candidate inventory to assign formal integration decisions for the upcoming Data Engineering stage. Each dataset is classified into one of four formal states:
- **SELECTED**: Meets all technical, quality, and governance requirements; approved for primary feature engineering.
- **CONDITIONAL**: Highly valuable, but incorporates a specific technical or data-quality limitation that must be mitigated through software preprocessing before inclusion.
- **BACKUP**: Serves as a secondary, auxiliary, or contingency datasource if a primary stream fails.
- **REJECTED**: Inadequate quality, prohibitive licensing, or insufficient granularity.

## 8. Data Integration Feasibility

### 8.1 Shared Linking Attributes and Resolution Harmonization
To fuse disparate observations into a common analytical voxel (20 X 20 m spatial cells with daily/hourly windows), the following integration mechanisms are established:
1. **Spatial Anomaly Key**: All vector points (CONAFOR, NASA FIRMS) and raster cells (Copernicus DEM 30 m, Sentinel-2 10–20 m, ERA5-Land 9 km) are indexed into Uber H3 Spatial Hexagons (Resolution 9, ~ 0.1 km^2, or UTM 20m bounding voxels).
2. **Temporal Key**: Aligned to Coordinated Universal Time (UTC timestamps) converted to standard Mexican Central Time (GMT-6), rolling into 24-hour observation windows with 48–72h forward-looking predictive horizons.
3. **Downscaling Protocol**: Coarse ERA5-Land atmospheric temperature is interpolated to the 30 m DEM grid through elevation difference adjustments.

### 8.2 Incompatibilities and Mitigations
- **Temporal Frequency Mismatch**: ERA5-Land is hourly; Sentinel-2 is captured every 5 days; CONAFOR is event-driven.
  *Mitigation*: Atmospheric data will be summarized into daily maximums, minimums, and 72-hour rolling averages. Sentinel-2 spectral indices will be propagated forward through 5-day persistence windows.
- **Coordinate Reference System (CRS) Disparity**: CONAFOR is stored in geographic WGS84 (EPSG:4326); Sentinel-2 is in UTM Zone 13N (EPSG:32613); GLO-30 is in EPSG:4326 with EGM2008 heights.
  *Mitigation*: Reproject all spatial features to UTM Zone 13N (EPSG:32613) in GDAL/Rasterio for metric distance calculations, maintaining WGS84 lat/long coordinates for GeoJSON export.
