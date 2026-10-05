---
title: "Governance & Traceability"
project: "TERRA-FIRE"
tags:
  - data-acquisition
  - terra-fire
  - governance
---

## 5. Data Governance and Responsible Use
Responsible data stewardship requires analyzing legal ownership, licensing restrictions, terms of use, privacy implications, and redistributive covenants before incorporating datasets into the modeling pipeline.

### 5.1 Privacy and Ethical Risk Analysis
Wildfire databases can carry unintended social and legal risks:
1. **Property Stigmatization Risk**: CONAFOR microdata contains the field Predio (property name) and ejido names. In rural Mexico, identifying private landowners or specific ejidos as origin points of fires can lead to social conflicts or criminal accusations of environmental crimes (Article 420 Bis of the Federal Penal Code).
   *Protocol*: All cadastral and property names (Predio) will be stripped and masked during Data Engineering. Machine learning models will operate exclusively on anonymous spatial coordinates and H3 hexagon indices.
2. **Algorithmic Bias Against Peasant Communities**: Rural agricultural burns (roza y quema) are legitimate subsistence farming practices. Predictive algorithms must not be tuned to automatically classify rural indigenous territories as "criminal zones," but rather as zones requiring municipal support, firebreak construction, and optimal meteorological burn windows.

## 6. Data Provenance and Traceability
To satisfy the requirements of scientific reproducibility and data integrity, all candidate datasets were acquired directly from authoritative source endpoints, hashed with SHA-256 cryptographic algorithms, and cataloged into an automated acquisition manifest.

### 6.1 Storage Hierarchy and Preservation Protocol
- **Write-Protection**: Raw datasets are treated as read-only (chmod 444 in production). Under no circumstances will source files be modified, edited, or transformed in-place.
