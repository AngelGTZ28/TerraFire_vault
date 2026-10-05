---
title: "Data Requirements"
project: "TERRA-FIRE"
tags:
  - data-acquisition
  - terra-fire
  - requirements
---

## 1. Data Requirements

### 1.1 Context and Continuity from Data Opportunity Mapping (DOM)
In the previous stage (Data Opportunity Mapping), project TERRA-FIRE established that wildfire management in Mexico suffers from an operational time lag: civil protection and emergency brigades act reactively between 3 and 12 hours after ignition detection. To achieve an anticipatory model capable of generating 48-to-72-hour pre-ignition risk surfaces at 10–20 m spatial resolution, the machine learning model (supervised Gradient Boosted Decision Trees / XGBoost) requires three physical pillars:

1. **Target Historical Ground-Truth (Y in {0, 1})**: Precise coordinates, timestamps, and burned areas of verified wildfires.
2. **Dynamic Biophysical & Atmospheric Predictors (X_{dynamic})**: Canopy moisture desiccation proxies (NDMI, SAVI), atmospheric evaporative suction (Vapor Pressure Deficit - VPD), ambient temperature, surface wind speed/direction, and root-zone/subsurface soil moisture.
3. **Static Biophysical & Topographic Modifiers (X_{static})**: Terrain slope, solar aspect (radiation accumulation), elevation, and proximity to anthropogenic ignition sources (roads, agricultural borders).

### 1.2 Operational Decisions Supported by Data
The data acquisition strategy is strictly dictated by four operational decisions formulated in the project architecture:

- **DEC-01: Preventive Resource Staging (Protección Civil & CONAFOR)**: Daily morning dispatch (06:00 AM) based on 48–72h ignition probability maps. Requires daily atmospheric updates and weekly vegetation moisture indices.
- **DEC-02: Moratoria on Agricultural Burns (Roza y Quema)**: Issued by municipal authorities and ejido commissariats when atmospheric VPD exceeds 2.5 kPa and Dead Fuel Moisture Content drops below 8%. Requires high-frequency weather reanalysis.
- **DEC-03: Tactical Fireline Safety Routing**: Real-time offline navigation for front-line brigades identifying convective chimney canyons and unburned escape paths. Requires fine-grained 30 m topography and offline vector tiles.
- **DEC-04: Burn Perimeter and Severity Audit**: CONAFOR post-incident verification comparing pre- and post-fire Normalized Burn Ratio (dNBR). Requires multispectral imagery with <5 days orbital latency.
