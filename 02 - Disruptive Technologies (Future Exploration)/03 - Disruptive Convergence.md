---
title: "Convergencia Tecnológica Disruptiva"
subject: "Disruptive Technologies"
code: "LITD9A"
authors:
  - "Angel Emilio Gutierrez Lozano (4341)"
  - "Emiliano Betanzos Valtierra (4795)"
advisor: "Dr. Sergio Valadez Godínez"
tags:
  - convergence
  - ai-gis
  - edge-computing
  - disruptive-technologies
---

# 🌀 Convergencia Tecnológica Disruptiva en TERRA-FIRE

> [!tip] Concepto de Convergencia
> La verdadera innovación no reside en una tecnología aislada, sino en la **convergencia sinérgica** de disciplinas que históricamente operaban en silos: Teledetección Espacial, Computación Científica en la Nube, Aprendizaje Automático y Arquitecturas Web Offline.

---

## 1. El Triángulo de Convergencia de TERRA-FIRE

```mermaid
graph TD
    subgraph SATELLITE["🌍 Teledetección y Datos Abiertos"]
        S1["Copernicus Sentinel-2 (10-20m)"]
        S2["Sentinel-1 SAR (Radar C-Band)"]
        S3["ECMWF ERA5-Land Reanalysis"]
    end

    subgraph AI["🧠 Inteligencia Artificial y Big Data"]
        A1["XGBoost Classifier"]
        A2["TreeSHAP Explainability"]
        A3["Matriz Espaciotemporal Parquet"]
    end

    subgraph EDGE["📱 Computación Edge y Entrega Táctica"]
        E1["Progressive Web App (PWA)"]
        E2["Teselas Vectoriales Mapbox (.pbf)"]
        E3["Motor SQLite / WASM en Navegador"]
    end

    SATELLITE -->|Pipelines Automatizados STAC| AI
    AI -->|Serialización Ligera de Polígonos| EDGE
    EDGE -->|Decisiones Preventivas en Campo| USERS["👨‍🌾 Ejidatarios & 🚒 Brigadistas"]
```

---

## 2. Análisis de Sinergias y Fricciones Superadas

### Sinergia 1: Satélites Ópticos + Reanálisis Atmosférico
- *El problema tradicional:* Las imágenes ópticas de Sentinel-2 miden la humedad del follaje cada 5 días, pero no miden las ráfagas horarias de viento ni la sequedad del aire. El reanálisis climático ERA5 mide la atmósfera pero a una resolución tosca de 9 km.
- *La convergencia:* Mediante **downscaling topográfico adiabático**, TERRA-FIRE acopla la demanda atmosférica (VPD) horaria a la malla espacial de 10 m de Sentinel-2 y a las curvas de nivel del DEM GLO-30.

### Sinergia 2: Machine Learning Pesado + Dispositivos Móviles Económicos
- *El problema tradicional:* Los modelos de Inteligencia Artificial requieren servidores potentes con GPUs o CPUs multihilo; los teléfonos de los ejidatarios rurales son de gama baja y carecen de conexión en la sierra.
- *La convergencia:* El modelo XGBoost corre **enteramente en la nube** (batch nocturno diario a las 02:00 UTC). Lo que se envía al dispositivo móvil no es el modelo ni pesadas imágenes ráster GeoTIFF, sino una **capa vectorial altamente comprimida** (`.pbf`) de menos de 15 MB por municipio.

### Sinergia 3: IA Explicable (XAI) + Sabiduría Comunitaria
- *El problema tradicional:* Los modelos de "caja negra" son rechazados por campesinos experimentados y por analistas de Protección Civil que no entienden por qué el sistema marca una alerta roja.
- *La convergencia:* Mediante valores **SHAP**, la plataforma desglosa los motivos exactos de la advertencia: *"Alerta roja porque el viento superará 35 km/h a las 14:00 hrs y la humedad del dosel está 40% por debajo de lo normal"*. Esto valida la experiencia del agricultor y construye confianza mutua.

---
*Notas vinculadas:* [[02 - Industrial Evolution & Tech Radar]] | [[04 - Future Scenarios 2026-2036]] | [[End-to-End System Pipeline]]
