---
title: "02. Modelo Conceptual de Solución y Flujo de Componentes"
project: "TERRA-FIRE"
academic_degree: "Ingeniería en Tecnologías de la Información e Innovación Digital"
subject: "Integrative Project III"
code: "LITD9A"
term: "Sep-Dec 2026"
institution: "Universidad Tecnológica El Retoño"
authors:
  - "Angel Emilio Gutierrez Lozano (4341)"
  - "Emiliano Betanzos Valtierra (4795)"
advisor: "Dr. Sergio Valadez Godínez"
date: "2026-10-12"
trl_level: "TRL 2 Validated -> Ready for PoC (TRL 3)"
tags:
  - conceptual-model
  - component-flow
  - biophysical-equations
  - downscaling
  - treeshap
  - pwa-edge
---

# ⚙️ 02. Modelo Conceptual de Solución y Flujo de Componentes
## TERRA-FIRE: Transformación de Datos Satelitales en Inteligencia de Campo

---

## 1. Flujo de Información y Recursos de Alto Nivel

El modelo conceptual formaliza cómo los fenómenos físicos crudos del planeta—reflectancia espectral de radiación solar, variables termodinámicas de la capa límite atmosférica y gradientes de elevación topográfica—se transforman de manera sistemática y reproducible en decisiones tácticas comprensibles para un campesino o brigadista en la pantalla de su teléfono móvil.

El límite arquitectónico desacopla tajantemente dos capas operativas:
1. **Capa de Inteligencia Batch en la Nube:** Donde se ejecutan los procesos de cómputo intensivo (ingesta satelital, downscaling microclimático, inferencia ML y cálculo de valores Shapley).
2. **Capa Táctica de Entrega en el Borde (Edge):** Que opera con autonomía absoluta en teléfonos móviles de bajo costo en zonas sin cobertura celular.

```mermaid
flowchart TD
    subgraph S1["1. Entradas Físicas y Satelitales"]
        DEM["Copernicus GLO-30 DEM<br>Malla estática 30m de elevación"]
        S2["Sentinel-2 L2A BOA<br>Bandas B2, B4, B8, B11, B12 (STAC)"]
        ERA["ERA5-Land Reanalysis<br>Temp 2m, Dewpoint, Viento U/V, Humedad Suelo"]
        S1["Sentinel-1 C-SAR (Piloto)<br>Retrodispersión dual-pol VV + VH"]
    end

    subgraph S2_PROC["2. Procesamiento Biofísico y Downscaling Microclimático"]
        VPD_EQ["Demanda Evaporativa Termodinámica<br>VPD = e_s(T) - e_a(T_dew) [kPa]"]
        MASK["Filtrado de Escenas Ópticas<br>Máscaras SCL de Nubes y Sombras"]
        LAPSE["Downscaling Adiabático Ambiental<br>T_downscaled = T_ERA5 - 0.0065 * delta_Z"]
        NDMI_EQ["Proxies de Humedad de Combustible Vivo<br>NDMI = (B8 - B11)/(B8 + B11) y SAVI"]
    end

    subgraph S3_ML["3. Inteligencia de Machine Learning y Explicabilidad Local"]
        PARQUET["Matriz Espaciotemporal Unificada<br><code>terra_fire_spatiotemporal_matrix_v1.parquet</code>"]
        XGB["Motor de Inferencia Supervisada<br>Clasificador XGBoost -> P(Ignición 48-72h)"]
        SHAP["Módulo de IA Explicable<br>TreeSHAP -> Top-3 Factores Locales"]
    end

    subgraph S4_VEC["4. Compresión Vectorial Táctica y Serialización"]
        CARDS["Agregación de Metadatos de Alerta<br>Cédulas Informativas en Español (JSON)"]
        CONTOUR["Extracción de Contornos de Riesgo<br>Iso-polígonos (Bajo, Moderado, Alto, Extremo)"]
        TIPP["Codificación Tippecanoe<br>Teselas Vectoriales (.pbf) < 12 MB"]
    end

    subgraph S5_EDGE["5. Ejecución Táctica en el Borde (PWA Offline)"]
        UI["Interfaz Táctica Móvil<br>Semáforo de Quemas y Rutas de Escape"]
        CACHE["Sincronización Previa en Base Wi-Fi<br>Service Worker -> IndexedDB / SQLite-WASM"]
        MAPL["Motor Vectorial MapLibre GL<br>Renderizado GPU fluido a 60 FPS"]
    end

    S1 --> S2_PROC
    S2_PROC --> S3_ML
    PARQUET --> XGB
    XGB --> SHAP
    S3_ML --> S4_VEC
    S4_VEC --> S5_EDGE
    CACHE --> MAPL
    MAPL --> UI
```

![Diagrama de Flujo Conceptual](assets/activity-3-conceptual-solution-flow.png)

---

## 2. Descripción Detallada de los 5 Subsistemas del Pipeline

### Componente 1: Subsistema de Ingesta Planetaria de Datos
- **Función:** Descarga programada automatizada de gránulos de Observación Terrestre y modelos de clima de superficie.
- **Entradas:** Consultas espaciotemporales mediante APIs STAC dirigidas a *Copernicus Open Access Hub / CDSE*, *Microsoft Planetary Computer* y *ECMWF Climate Data Store (CDS)*.
- **Lógica Operativa:** Ejecución diaria en nube mediante tarea batch programada a las 02:00 UTC. Descarga las escenas Sentinel-2 L2A más recientes con menor nubosidad, cortes Sentinel-1 GRD en órbita descendente y las estimaciones horarias ERA5-Land para la cordillera objetivo.

---

### Componente 2: Subsistema de Calibración Biofísica y Downscaling Microclimático
- **Función:** Armoniza las resoluciones espaciales y temporales dispares hacia una malla común de 20 metros y computa las variables termodinámicas de ignición física.
- **Formulación Matemática Biofísica:**

#### 1. Índice Normalizado de Humedad de Humedales / Combustibles Vivos (NDMI):
Captura el contenido de agua en el mesófilo foliar del dosel mediante el contraste entre la banda de infrarrojo cercano (NIR - B8) y la banda sensible a la absorción de agua en infrarrojo de onda corta (SWIR - B11):
$$\text{NDMI} = \frac{\rho_{\text{B8}} - \rho_{\text{B11}}}{\rho_{\text{B8}} + \rho_{\text{B11}}}$$
*(Valores de NDMI $< 0.15$ señalan estrés hídrico severo y deshidratación foliar crítica).*

#### 2. Déficit de Presión de Vapor Atmosférico (VPD):
Calculado a partir de las ecuaciones psicrométricas termodinámicas de Tetens:
$$e_s(T) = 0.61078 \exp\left(\frac{17.27 \cdot T}{T + 237.3}\right)\quad [\text{kPa}]$$
$$e_a(T_{\text{dew}}) = 0.61078 \exp\left(\frac{17.27 \cdot T_{\text{dew}}}{T_{\text{dew}} + 237.3}\right)\quad [\text{kPa}]$$
$$\text{VPD} = e_s(T) - e_a(T_{\text{dew}})\quad [\text{kPa}]$$

![Fórmulas de Tetens para VPD](assets/activity-3-tetens-vpd-formula.png)

*(Un $\text{VPD} > 2.5\text{ kPa}$ ejerce una succión deshidratante extrema sobre los combustibles finos muertos y la biomasa viva, multiplicando la tasa de propagación).*

#### 3. Downscaling Topográfico por Gradiente Térmico Adiabático:
Ajusta la temperatura atmosférica regional de ERA5-Land (celdas de 9 km) a las cañadas y crestas locales de 20 m utilizando el gradiente ambiental estándar ($\Gamma = -0.0065\text{ }^\circ\text{C/m}$):
$$T_{\text{downscaled}} = T_{\text{ERA5}} - 0.0065 \cdot (Z_{\text{DEM, 20m}} - Z_{\text{ERA5, geopotencial}})$$

---

### Componente 3: Motor de Machine Learning e Inteligencia Explicable (XAI)
- **Función:** Ingiere la matriz tabular unificada `terra_fire_spatiotemporal_matrix_v1.parquet`, evalúa interacciones multivariables no lineales y genera probabilidades calibradas de ignición junto con vectores locales de atribución causal.
- **Mecanismo Central:** Clasificador de árboles aumentados por gradiente (*XGBoost*) configurado con función de pérdida focal para manejar el desbalance extremo de clases ($<0.1\%$ ocurrencia de ignición frente al 99.9% de no-fuego).
- **Explicabilidad Local TreeSHAP:** Para cada vóxel con $P(\text{Ignición}) \ge 0.50$, el algoritmo calcula las atribuciones de Shapley exactas en tiempo polinomial sobre la estructura de árboles:
$$\phi_i(x) = \sum_{S \subseteq F \setminus \{i\}} \frac{|S|!(|F| - |S| - 1)!}{|F|!} \left[ f_x(S \cup \{i\}) - f_x(S) \right]$$
Donde $F$ es el conjunto total de variables y $\phi_i$ representa la contribución marginal de la variable $i$ al incremento sobre el riesgo base.

---

### Componente 4: Módulo de Serialización Vectorial y Compresión
- **Función:** Transforma superficies continuas de ráster en teselas vectoriales ligeras, eliminando la necesidad de transferir pesados GeoTIFF multibanda ($> 100\text{ MB}$) a dispositivos móviles.
- **Mecanismo:** 
  1. Extracción de contornos de riesgo mediante `gdal_contour` en 4 clases operativas: $[0, 0.25)$ (Verde/Bajo), $[0.25, 0.50)$ (Amarillo/Moderado), $[0.50, 0.75)$ (Naranja/Alto) y $[0.75, 1.0]$ (Rojo/Extremo).
  2. Simplificación topológica Douglas-Peucker ($\varepsilon = 0.0001^\circ$).
  3. Empaquetado multizoom (z10 a z15) en teselas Google Protocol Buffer (`.pbf`) con **Tippecanoe**.
  4. El archivo comprimido para un municipio entero de $1,500\text{ km}^2$ pesa **menos de 12 MB** ($>85\%$ de reducción frente al ráster crudo).

---

### Componente 5: Cliente Táctico Desconectado (PWA en el Borde)
- **Función:** Entrega posicionamiento táctico GPS en tiempo real, navegación cartográfica offline, cédulas explicativas de riesgo y rutas de escape topográfico seguras.
- **Mecanismo:** Aplicación Web Progresiva (PWA) con Service Workers. Las teselas `.pbf` y el JSON de metadatos se descargan al sincronizar en cabecera municipal con Wi-Fi y se almacenan en `IndexedDB` / `SQLite-WASM`. En campo y en **modo avión (100% offline)**, MapLibre GL renderiza las capas vectoriales directamente sobre la GPU móvil a 60 FPS.

---
*Documentos relacionados:* [[01 - Solution Concept & System Architecture]] | [[03 - Critical Assumptions & Research Questions]] | [[06 - Experimental Design & Validation Protocols]] | [[End-to-End System Pipeline]]
