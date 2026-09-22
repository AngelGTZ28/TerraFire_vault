---
title: "Catálogo de Fuentes de Datos y Protocolos de Ingesta"
subject: "Data Science"
code: "LITD9A"
authors:
  - "Angel Emilio Gutierrez Lozano (4341)"
  - "Emiliano Betanzos Valtierra (4795)"
advisor: "Dr. Sergio Valadez Godínez"
tags:
  - data-catalog
  - earth-observation
  - sentinel
  - era5
  - data-opportunity-mapping
---

# 🛰️ Catálogo de Fuentes de Datos y Protocolos de Ingesta

---

## 1. Taxonomía Estructural de Fuentes de Datos

![[assets/data-sources-taxonomy.png]]
*Figura 1: Clasificación de Fuentes según Origen, Estructura y Protocolo (Sección 3 DOM).*

| Fuente de Datos | Origen | Tipo de Estructura | Formato y Protocolo de Acceso | Uso Potencial en TERRA-FIRE |
| :--- | :---: | :---: | :--- | :--- |
| **Sentinel-2 MSI** | Externo (ESA / Copernicus) | Semiestructurado *(Ráster Geoespacial)* | COG / GeoTIFF vía STAC API en Microsoft Planetary Computer o Google Earth Engine. | Cálculo de índices biofísicos de humedad del follaje: NDMI, SAVI, NBR y NDVI. |
| **Sentinel-1 C-SAR** | Externo (ESA / Copernicus) | Semiestructurado *(Arreglos Polares)* | SAFE / GRD GeoTIFF vía Copernicus Data Space Ecosystem. | Monitoreo de humedad superficial a través de nubes densas mediante relación cruzada VH/VV. |
| **ERA5-Land Reanalysis** | Externo (ECMWF / C3S) | Estructurado *(Arreglos Multidimensionales)* | NetCDF-4 / GRIB2 vía CDS API / Open-Meteo. | Cálculo continuo de Déficit de Presión de Vapor (VPD en kPa), temperatura, viento y humedad de suelo. |
| **Copernicus GLO-30 DEM** | Externo (ESA / OpenTopo) | Estructurado *(Malla Ráster de Elevación)* | Cloud-Optimized GeoTIFF (COG) en AWS S3 / Planetary Computer. | Cálculo estático de pendiente/orientación y gradiente adiabático para downscaling climático. |
| **Registros Históricos CONAFOR** | Externo (CONAFOR / SNIF) | Estructurado *(Vectores Relacionales)* | CSV / Shapefile en Portal de Datos Abiertos de México. | Conjunto de datos objetivo para entrenamiento supervisado de clasificación de ignición ($0/1$). |
| **NASA FIRMS VIIRS** | Externo (NASA Earthdata) | Semiestructurado *(Puntos de Coordenadas)* | REST API / GeoJSON / CSV Near-Real-Time. | Validación espaciotemporal de puntos calientes activos y referencia temporal de ignición. |
| **CONABIO / OpenStreetMap** | Externo (INEGI / Comunidad) | Estructurado *(Vectores Poligonales y Líneas)* | Geopackage / Shapefile vía Overpass API / Descarga directa. | Estratificación de tipos de combustible y cálculo de distancias a caminos y parcelas agrícolas. |

---

## 2. Análisis de Disponibilidad, Licenciamiento y Fricción

![[assets/data-availability-licensing.png]]
*Figura 2: Auditoría de Accesibilidad, Restricciones y Dificultad de Ingesta (Sección 3 DOM).*

| Fuente de Datos | Estatus de Disponibilidad | Régimen de Licencia | Dificultad Técnica Estimada | Evaluación Técnica y Cuellos de Botella |
| :--- | :---: | :--- | :---: | :--- |
| **Sentinel-2 MSI** | Totalmente Disponible | Mandato de Acceso Abierto (CC BY-SA 3.0 IGO) | **Media** | Ingesta automatizada vía STAC; requiere enmascaramiento de nubes (SCL) y manejo de pesados GeoTIFF. |
| **Sentinel-1 C-SAR** | Totalmente Disponible | Política Abierta de Copernicus (Sin restricciones) | **Media-Alta** | Requiere remoción de ruido térmico, calibración radiométrica de terreno y filtrado de moteado (*speckle*). |
| **ERA5-Land Climate** | Totalmente Disponible | Datos Abiertos ECMWF (Acceso libre vía API) | **Media** | Cuadrícula tosca de 9 km exige downscaling por lapse-rate DEM y descompresión de NetCDF multidimensional. |
| **Copernicus DEM** | Totalmente Disponible | Dominio Público / Acceso Abierto | **Baja** | Capa estática; requiere una única descarga y extracción local de pendientes en GDAL/Python. |
| **Registros CONAFOR** | **Acceso Condicional** | Datos Abiertos México (Sujeto a liberación anual) | **Media** | Coordenadas truncadas, registros duplicados, marcas de tiempo de reporte imprecisas; exige limpieza exhaustiva. |
| **NASA FIRMS** | Totalmente Disponible | Política de Datos Abiertos de NASA (REST API) | **Baja** | Consultas HTTP directas a endpoints REST; parseo inmediato de CSV/GeoJSON de latitud/longitud. |
| **OSM / INEGI** | Totalmente Disponible | ODbL / Libre Uso INEGI | **Baja** | Alta disponibilidad; transformaciones de distancia euclidiana calculadas estáticamente en Python/GIS. |

---
*Notas vinculadas:* [[01 - Data Formulation & Decision Requirements]] | [[03 - Big Data 5Vs & Ecosystem Architecture]] | [[Feature Store & Parquet Schema]]
