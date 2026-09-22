---
title: "Las 5Vs de Big Data y Arquitectura del Ecosistema"
subject: "Data Science"
code: "LITD9A"
authors:
  - "Angel Emilio Gutierrez Lozano (4341)"
  - "Emiliano Betanzos Valtierra (4795)"
advisor: "Dr. Sergio Valadez Godínez"
tags:
  - big-data-5vs
  - architecture
  - pipeline
  - data-science
---

# 🌪️ Las 5Vs de Big Data y Arquitectura del Ecosistema

---

## 1. Análisis de las 5 Dimensiones de Big Data (5Vs)

![[assets/big-data-5vs-analysis.png]]
*Figura 1: Evaluación de las 5Vs en la Infraestructura de TERRA-FIRE (Sección 4 DOM).*

| Dimensión "V" | Análisis en TERRA-FIRE | Impacto en la Arquitectura y Estrategia Analítica |
| :--- | :--- | :--- |
| **VOLUMEN** <br> *(Terabytes de Ráster)* | Múltiples gigabytes por escena de Sentinel-2 (13 bandas a 10–20 m) sumados a cubos multianuales de reanálisis ERA5-Land para todo el territorio mexicano. | - Almacenamiento en nube de objetos (AWS S3 / GEE) en lugar de discos locales. <br> - Uso de Cloud-Optimized GeoTIFFs (COGs) y extracción de sub-regiones (*bounding boxes*). <br> - Transformación de rásters pesados a muestras tabulares compactas en **Apache Parquet**. |
| **VELOCIDAD** <br> *(Cadencia de 5 Días a Horaria)* | Sentinel-2 revisita la misma región cada 5 días; ERA5-Land produce actualizaciones horarias continuas. Las inferencias requieren lotes diarios a 48–72h. | - Flujos programados (*cron*) en Apache Airflow o Cloud Functions. <br> - Disparadores de ETL incremental al confirmarse nueva escena satelital libre de nubes. <br> - Rutinas de inferencia masiva ejecutadas en horarios de baja demanda (02:00 UTC). |
| **VARIEDAD** <br> *(Multiformato Espacial y Tabular)* | Fusión de rásters GeoTIFF de 16 bits, tensores climáticos NetCDF-4/GRIB2, vectores de caminos (OSM) y registros tabulares relacionales (CONAFOR). | - Capa de armonización y reproyección unificada a mallas métricas UTM. <br> - Mínimo común espacial: vóxeles regulares de $20\times20$ m. <br> - Conversión a matrices columnares unificadas en formato Parquet. |
| **VERACIDAD** <br> *(Ruido Atmosférico y Errores)* | Oclusión por nubes densas y sombras de relieve. Errores de registro humano en coordenadas de inicio de incendio en bitácoras oficiales. | - Filtrado por máscara de calidad espectral (*Scene Classification Layer - SCL*). <br> - Respaldo de humedad con radar SAR de microondas (Sentinel-1). <br> - Cruce de coordenadas CONAFOR con detecciones de calor térmico NASA FIRMS. |
| **VALOR** <br> *(Ventana Operativa de 72 Horas)* | Transformación de terabytes de ruido planetario en teselas de riesgo de 10 m y explicabilidad clara en campo. | - Alto retorno de inversión: cero gasto en compra o reposición de sensores físicos. <br> - Ventana de acción preventiva de 48–72h para salvaguardar vidas y bosques. <br> - Entrega ultraligera (<15 MB) de teselas vectoriales en Progressive Web App. |

---

## 2. Arquitectura del Ecosistema de Datos TERRA-FIRE

![[assets/data-ecosystem-architecture.png]]
*Figura 2: Flujo de Datos Extremo a Extremo de TERRA-FIRE (Sección 5 DOM).*

```mermaid
flowchart TD
    subgraph L1["1. GENERACIÓN E INGESTA EXTERNA"]
        S1["Copernicus Sentinel-2 & 1
Multiespectral 10-20m + SAR"]
        S2["ECMWF ERA5-Land
Reanálisis Horario 2m Temp, VPD, Viento"]
        S3["Copernicus DEM & CONAFOR
Topografía 30m + Registros Históricos"]
    end

    subgraph L2["2. PROCESAMIENTO EN NUBE, CALIBRACIÓN Y DOWNSCALING"]
        P1["Control Óptico QA & Fusión SAR
Filtrado SCL y Moteado"]
        P2["Downscaling Microclimático
Gradiente adiabático DEM (-6.5°C/km) + VPD"]
        P3["Alineación Espacial
Malla métrica UTM en vóxeles de 20x20m"]
    end

    subgraph L3["3. FEATURE STORE ESPACIOTEMPORAL Y MOTOR ML"]
        F1["Feature Store Tabular (.parquet)
NDMI, SAVI, VPD, Viento, Pendiente, Dist_Agri"]
        M1["Clasificador XGBoost + Kernel TreeSHAP
Predicción P(Fuego en 48-72h) + Explicabilidad"]
    end

    subgraph L4["4. ENTREGA TÁCTICA EDGE Y PWA OFFLINE"]
        T1["Generación de Teselas Vectoriales
Tippecanoe (.pbf) <15MB"]
        W1["Almacenamiento Cliente PWA
Service Workers + SQLite/WASM"]
        U1["Decisiones Tácticas en Brigada
Semáforo de quema y corredores de escape sin internet"]
    end

    L1 --> L2
    L2 --> L3
    L3 --> L4
```

---
*Notas vinculadas:* [[02 - Data Source Catalog & Ingestion]] | [[04 - Feature Taxonomy & Prioritization]] | [[End-to-End System Pipeline]]
