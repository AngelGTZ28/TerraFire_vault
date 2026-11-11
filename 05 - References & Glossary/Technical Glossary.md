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

*Vinculado a:* [[00 - TERRA-FIRE Central Dashboard]] | [[07 - Digital Transformation Blueprint]] | [[Activity 6. Pattern Discovery Challenge]]

---

- **ADKAR (Modelo Prosci):** Marco de gestión del cambio individual compuesto por cinco etapas secuenciales: *Awareness* (Conciencia), *Desire* (Deseo), *Knowledge* (Conocimiento), *Ability* (Habilidad) y *Reinforcement* (Refuerzo), aplicado en TERRA-FIRE para guiar la adopción en ejidos y brigadas.
- **Brier Score (Puntaje de Confiabilidad de Brier):** Medida de error cuadrático medio entre probabilidades calibradas ($[0, 1]$) y resultados observados ($Y \in \{0, 1\}$). Valores cercanos a cero indican alta fidelidad empírica.
- **Carta de Datos No Punitiva (Non-Punitive Data Charter):** Acuerdo de gobernanza comunitaria firmado en *Asamblea Ejidal* que garantiza que el uso del Semáforo de Quema de TERRA-FIRE es estrictamente preventivo e informativo, sin rastreo personal ni aplicación de multas de SEMARNAT.
- **Cédula Informativa de Riesgo Local (Local Risk Card):** Componente de comunicación ciudadana y técnica de TERRA-FIRE que traduce las atribuciones locales de TreeSHAP en advertencias operativas con los 3 factores físicos principales de riesgo.
- **CONAFOR:** *Comisión Nacional Forestal*. Organismo público descentralizado del gobierno mexicano encargado de la administración, fomento y protección de los recursos forestales.
- **Cuadrante IV Piro-Antropogénico ($\text{PC1} > 0 \land \text{PC2} \le 0$):** Zona crítica descubierta mediante PCA en la Actividad 6 que representa valles agrícolas secos de baja altitud; concentra el **68.61% de todos los incendios forestales** con una amplificación de riesgo de $28.1\times$ respecto al núcleo montañoso húmedo.
- **DEM (Digital Elevation Model):** Modelo Digital de Elevación. Representación ráster matricial de los valores de altitud del relieve topográfico de la Tierra (Copernicus GLO-30 a 30 m).
- **Digital Transformation (Transformación Digital):** Reconfiguración sistémica de personas, procesos, tecnología y cultura organizacional para crear nuevo valor (en TERRA-FIRE: pasar de la supresión reactiva 3–12h post-ignición a la prevención anticipatoria 48–72h pre-ignición), diferenciándose de la simple *Digitization* (pasar papel a digital) y *Digitalization* (digitalizar flujos existentes sin cambiar el paradigma).
- **dNBR (Differenced Normalized Burn Ratio):** Índice obtenido restando el NBR posterior al incendio del NBR previo al incendio; mide cuantitativamente la severidad del daño en el dosel.
- **Douglas-Peucker (Algoritmo de):** Algoritmo de simplificación topológica que reduce el número de vértices de curvas y polígonos dentro de una tolerancia $\varepsilon$, indispensable para comprimir isolíneas en teselas `.pbf`.
- **Dynamic Capabilities (Capacidades Dinámicas — Teece et al., 1997):** Habilidad organizacional para integrar, construir y reconfigurar competencias internas y externas frente a entornos cambiantes mediante tres procesos: *Sensing* (detección satelital), *Seizing* (pre-asignación 48–72h) y *Transforming* (co-gobernanza preventiva).
- **ERA5-Land:** Conjunto de reanálisis atmosférico y terrestre global producido por el Centro Europeo de Previsiones Meteorológicas a Plazo Medio (ECMWF), con resolución de ~9 km y frecuencia horaria.
- **FWI (Forest Fire Weather Index):** Índice canadiense de peligro de incendios que integra temperatura, humedad relativa, viento y lluvia acumulada en subíndices de combustibilidad.
- **Hotelling's $T^2$ y Estadístico $Q$ (SPE):** Métricas multivariadas en el subespacio PCA que cuantifican variaciones extremas dentro del modelo ($T^2$) y errores de reconstrucción ortogonales fuera del modelo ($Q$), utilizadas para aislar tormentas convectivas del monzón.
- **Kaiser Criterion (Criterio de Kaiser):** Regla estadística en PCA que retiene únicamente los componentes principales con autovalores $\lambda_k \ge 1.0$ (en TERRA-FIRE: `PC1`, `PC2` y `PC3`, reteniendo el $87.87\%$ de la varianza total).
- **LFMC (Live Fuel Moisture Content):** Contenido de Humedad del Combustible Vivo. Porcentaje de masa de agua contenida en el follaje y ramas vivas respecto a su peso seco.
- **NASA FIRMS:** *Fire Information for Resource Management System*. Sistema de NASA que distribuye detecciones activas de calor de los radiómetros VIIRS (375 m) y MODIS (1 km).
- **NBR (Normalized Burn Ratio):** Índice espectral que relaciona el infrarrojo cercano (NIR) y el infrarrojo de onda corta (SWIR-2); podado en la Actividad 5 por multicolinealidad extrema ($\text{VIF} > 100$) con `ndmi`.
- **NDMI (Normalized Difference Moisture Index):** Índice espectral calculado a partir de NIR y SWIR-1 ($B08$ y $B11$ en Sentinel-2), altamente sensible al estrés hídrico del dosel arbóreo.
- **NOM-015-SEMARNAT/AGRICULTURA-2023:** Norma Oficial Mexicana que establece los lineamientos técnicos obligatorios para el uso del fuego y quemas controladas en terrenos forestales y agropecuarios en México.
- **PCA (Principal Component Analysis):** Transformación lineal ortogonal que proyecta variables correlacionadas en ejes incorrelacionados de varianza máxima ($\text{VIF} = 1.00$). En TERRA-FIRE comprime 12 variables a 3 componentes (`PC1`, `PC2`, `PC3`).
- **PR-AUC (Precision-Recall Area Under Curve):** Área bajo la curva de Precisión-Exhaustividad. Métrica estándar de evaluación para problemas con desbalance de clases severo ($1 : 19.86$).
- **Promotores Digitales Forestales:** Red de jóvenes rurales capacitados en cada ejido para acompañar a campesinos mayores en la sincronización Wi-Fi y lectura del Semáforo de Quema.
- **PWA (Progressive Web Application):** Aplicación web desarrollada con estándares modernos (Service Workers, `IndexedDB`, Web App Manifest) que permite instalación en teléfonos económicos y funcionamiento 100% desconectado.
- **SAR (Synthetic Aperture Radar):** Radar de Apertura Sintética. Sistema activo de teledetección en microondas (Sentinel-1 banda C) capaz de penetrar nubes y humo.
- **SAVI (Soil-Adjusted Vegetation Index):** Índice de vegetación que incorpora un factor constante $L = 0.5$ para neutralizar la distorsión del suelo desnudo en zonas semiáridas.
- **SHAP (SHapley Additive exPlanations):** Método fundamentado en teoría de juegos para atribuir la contribución individual de cada variable predictiva al resultado de un modelo de Machine Learning.
- **SOP-72H (Preventive Dispatch Protocol):** Procedimiento Operativo Estándar diseñado en el Blueprint de Transformación Digital que institucionaliza el pre-posicionamiento de brigadas y pipas con 48 a 72 horas de anticipación en zonas rojas del Cuadrante IV.
- **Spatial Block Cross-Validation:** Validación cruzada por bloques espaciales (`GroupKFold` por `voxel_id`) para evitar fuga de información por autocorrelación espacial.
- **SPPIF:** *Sistema de Predicción de Peligro de Incendios Forestales*. Plataforma operativa de CONAFOR que calcula diariamente el riesgo de fuego en México a escala regional.
- **STAC (SpatioTemporal Asset Catalog):** Especificación estándar para catalogar y consultar metadatos geoespaciales mediante APIs web abiertas.
- **TAM / UTAUT:** Modelos teóricos de adopción tecnológica (*Technology Acceptance Model* / *Unified Theory of Acceptance and Use of Technology*) centrados en la Utilidad Percibida y la Facilidad de Uso Percibida.
- **Tippecanoe:** Herramienta de compilación de geometrías geoespaciales desarrollada por Mapbox para generar teselas vectoriales `.pbf` ultraligeras (`< 12 MB`).
- **TreeSHAP:** Algoritmo exacto de cálculo de valores Shapley para árboles de decisión que opera en `< 5 ms`.
- **TRL (Technology Readiness Level):** Escala de 9 niveles (ISO 16290:2013) para evaluar la madurez tecnológica.
- **VIF (Variance Inflation Factor):** Factor de Inflación de la Varianza ($\text{VIF}_j = \frac{1}{1 - R_j^2}$), utilizado para diagnosticar y eliminar multicolinealidad severa ($\text{VIF} > 10$).
- **VPD (Vapor Pressure Deficit):** Déficit de Presión de Vapor (ecuación de Tetens, en $\text{kPa}$). Principal indicador termodinámico de succión evaporativa atmosférica y secado del combustible.
- **XGBoost:** *eXtreme Gradient Boosting*. Algoritmo de ensamble supervisado basado en árboles de decisión optimizados por gradiente.
