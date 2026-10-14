---
title: "Glosario Técnico de Términos"
project: "TERRA-FIRE"
category: "References"
tags:
  - glossary
  - terminology
  - definitions
---

# 📖 Glosario Técnico de Términos

---

- **Brier Score (Puntaje de Confiabilidad de Brier):** Medida de error cuadrático medio entre probabilidades calibradas ($[0, 1]$) y resultados observados ($Y \in \{0, 1\}$). Valores cercanos a cero indican alta fidelidad empírica.
- **Cédula Informativa de Riesgo Local:** Componente de comunicación ciudadana de TERRA-FIRE que traduce las atribuciones locales de TreeSHAP en advertencias operativas en lenguaje cotidiano para comunidades y brigadas.
- **CONAFOR:** *Comisión Nacional Forestal*. Organismo público descentralizado del gobierno mexicano encargado de la administración, fomento y protección de los recursos forestales.
- **DEM (Digital Elevation Model):** Modelo Digital de Elevación. Representación ráster matricial de los valores de altitud del relieve topográfico de la Tierra.
- **dNBR (Differenced Normalized Burn Ratio):** Índice obtenido restando el NBR posterior al incendio del NBR previo al incendio; mide cuantitativamente la severidad del daño en el dosel.
- **Douglas-Peucker (Algoritmo de):** Algoritmo de simplificación topológica que reduce el número de vértices de curvas y polígonos dentro de una tolerancia $\varepsilon$, indispensable para comprimir isolíneas en teselas `.pbf`.
- **ERA5-Land:** Conjunto de reanálisis atmosférico y terrestre global producido por el Centro Europeo de Previsiones Meteorológicas a Plazo Medio (ECMWF), con resolución de ~9 km y frecuencia horaria.
- **FWI (Forest Fire Weather Index):** Índice canadiense de peligro de incendios que integra temperatura, humedad relativa, viento y lluvia acumulada en subíndices de combustibilidad.
- **LFMC (Live Fuel Moisture Content):** Contenido de Humedad del Combustible Vivo. Porcentaje de masa de agua contenida en el follaje y ramas vivas respecto a su peso seco.
- **NASA FIRMS:** *Fire Information for Resource Management System*. Sistema de NASA que distribuye detecciones activas de calor de los radiómetros VIIRS y MODIS.
- **NBR (Normalized Burn Ratio):** Índice espectral que relaciona el infrarrojo cercano (NIR) y el infrarrojo de onda corta (SWIR-2) para identificar biomasa calcinada o deshidratada.
- **NDMI (Normalized Difference Moisture Index):** Índice espectral calculado a partir de NIR y SWIR-1 ($B8$ y $B11$ en Sentinel-2), altamente sensible al agua intracelular de la vegetación.
- **NOM-015-SEMARNAT/AGRICULTURA-2023:** Norma Oficial Mexicana que establece los lineamientos técnicos obligatorios para el uso del fuego y quemas controladas en terrenos forestales y agropecuarios en México.
- **PR-AUC (Precision-Recall Area Under Curve):** Área bajo la curva de Precisión-Exhaustividad. Métrica estándar de evaluación para problemas con desbalance espacial extremo (>1,000:1) que evalúa el compromiso entre falsas alarmas y detecciones reales sin sesgo por verdaderos negativos.
- **PWA (Progressive Web Application):** Aplicación web desarrollada con estándares modernos (Service Workers, Web App Manifest) que permite instalación nativa y funcionamiento 100% desconectado.
- **SAR (Synthetic Aperture Radar):** Radar de Apertura Sintética. Sistema activo de teledetección en microondas (Sentinel-1 banda C) capaz de penetrar nubes, humo y oscuridad para registrar retrodispersión de humedad y estructura de biomasa.
- **SAVI (Soil-Adjusted Vegetation Index):** Índice de vegetación que incorpora un factor constante $L$ para neutralizar la distorsión del suelo desnudo en zonas semiáridas.
- **SHAP (SHapley Additive exPlanations):** Método fundamentado en teoría de juegos para atribuir la contribución individual de cada variable predictiva al resultado de un modelo de Machine Learning.
- **Spatial Block Cross-Validation:** Validación cruzada por bloques espaciales. Técnica de evaluación que aísla pliegues mediante búferes geográficos disjuntos (>25 km) para evitar fuga de información por autocorrelación espacial.
- **SPPIF:** *Sistema de Predicción de Peligro de Incendios Forestales*. Plataforma operativa de CONAFOR que calcula diariamente el riesgo de fuego en México.
- **STAC (SpatioTemporal Asset Catalog):** Especificación estándar para catalogar y consultar metadatos geoespaciales mediante APIs web abiertas.
- **Tippecanoe:** Herramienta de compilación de geometrías geoespaciales desarrollada por Mapbox para generar teselas vectoriales `.pbf` con filtrado inteligente por niveles de zoom.
- **TreeSHAP:** Algoritmo rápido de cálculo de valores Shapley exactos para árboles de decisión que reduce la complejidad computacional a escala de milisegundos en CPU.
- **TRL (Technology Readiness Level):** Escala de 9 niveles desarrollada por NASA para evaluar la madurez de una tecnología, desde la observación de principios básicos (TRL 1) hasta el despliegue operacional (TRL 9).
- **VPD (Vapor Pressure Deficit):** Déficit de Presión de Vapor. Diferencia entre la cantidad de humedad que el aire puede retener cuando está saturado y la cantidad real que retiene a cierta temperatura; principal indicador de secado atmosférico de la biomasa.
- **XGBoost:** *eXtreme Gradient Boosting*. Algoritmo de ensamble supervisado basado en árboles de decisión optimizados por gradiente, líder en velocidad y precisión sobre datos tabulares densos.

