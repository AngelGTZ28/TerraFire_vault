---
title: "Definición del Problema y Análisis de Contexto"
subject: "Integrative Project III"
code: "LITD9A"
authors:
  - "Angel Emilio Gutierrez Lozano (4341)"
  - "Emiliano Betanzos Valtierra (4795)"
advisor: "Dr. Sergio Valadez Godínez"
tags:
  - problem-discovery
  - context-analysis
  - conafor
  - integrative-project
---

# 🎯 Definición del Problema y Análisis de Contexto

> [!important] Declaración Central del Problema
> El marco operativo actual de manejo de incendios forestales en México descansa sobre un **paradigma estrictamente reactivo**. Los protocolos de combate solo se activan tras la confirmación de una columna de humo o una anomalía térmica orbital (NASA FIRMS), existiendo una ausencia crítica de inteligencia predictiva a nivel micro-territorial (10–20 m) con 48–72 horas de anticipación.

---

## 1. Desglose Estructurado del Problema

- **¿Cuál es el problema?** La falta de predicción anticipada de la probabilidad de ignición espacial. Cuando las brigadas son despachadas, el fuego ya ha cobrado fuerza en terrenos escarpados e inaccesibles.
- **¿Por qué existe?** Las herramientas institucionales actuales (como el SPPIF de CONAFOR) interpolan variables climáticas a escalas regionales sumamente toscas (~10 a 25 km) y no integran algoritmos modernos de aprendizaje automático (XGBoost) capaces de detectar patrones no lineales entre deshidratación del dosel (NDMI), demanda atmosférica de vapor (VPD) y relieve topográfico.
- **¿Por qué es importante?** Trasladar la estrategia de la "supresión reactiva" a la "prevención predictiva" permite emitir moratorias precisas a los ejidos para suspender quemas agrícolas en días de alto riesgo, pre-desplegar brigadas y ahorrar millones de pesos en combate aéreo, salvando vidas y biomas forestales.
- **¿Quiénes son los afectados directos?**
  1. *Brigadistas de primera línea y combatientes voluntarios:* Expuestos a atrapamientos mortales en cañadas.
  2. *Productores ejidales y comunidades rurales:* Quienes pierden cosechas, patrimonio y masa forestal por quemas agropecuarias que escapan a su control.
  3. *Despachadores y mandos de Protección Civil/CONAFOR:* Quienes desgastan recursos limitados apagando incendios masivos en lugar de prevenirlos.

---

## 2. Matriz de Análisis de Contexto (5 Dimensiones)

![[assets/context-analysis-matrix.png]]
*Figura 1: Matriz de Análisis de Contexto del Reto de Incendios Forestales (Sección 2 PDL).*

| Dimensión | Factores Críticos y Dinámicas Operativas | Impacto Operativo en el Reto |
| :--- | :--- | :--- |
| **Social** | Las comunidades rurales dependen de señales visuales directas (columnas de humo) para notar un fuego. Dependencia arraigada del fuego tradicional para limpieza de parcelas agrícolas. | La solución debe traducir complejas probabilidades numéricas de Machine Learning en alertas comprensibles y accionables (ej. semáforos Verde/Amarillo/Rojo). |
| **Económica** | La supresión reactiva (horas de helicóptero, combustible, maquinaria pesada y logística) drena el presupuesto de municipios y CONAFOR. | Un modelo predictivo ofrece un altísimo retorno de inversión (ROI) al permitir patrullajes terrestres preventivos baratos antes de la conflagración. |
| **Tecnológica** | La computación en la nube y las APIs satelitales (Copernicus, ECMWF) están maduras a nivel global, pero rara vez llegan a los brigadistas rurales en México. | Oportunidad de aplicar algoritmos supervisados de ensamble para predecir comportamiento del fuego a 10 m con 48–72h de anticipación. |
| **Ambiental** | El cambio climático extiende las temporadas de estiaje y altera los patrones de viento, volviendo obsoletos los calendarios tradicionales de quema agrícola. | El pronóstico debe nutrirse de variables dinámicas continuas (Déficit de Presión de Vapor - VPD, viento, humedad del combustible) y no de fechas estáticas. |
| **Organizacional** | CONAFOR y Protección Civil operan bajo el Sistema de Comando de Incidentes (ICS), optimizado para responder a siniestros reportados, no para prevención activa. | Se requiere evolucionar los Procedimientos Operativos Estandarizados (SOPs) para construir confianza en scores predictivos generados por IA. |

---

## 3. Portafolio de Evidencia y Validación Empírica

1. **Estadísticas Oficiales de CONAFOR:**
   Los registros históricos del Sistema Nacional de Información Forestal (SNIF) reportan consistentemente que más del **80% de los incendios forestales catastróficos** se originan por quemas agrícolas que escapan por cambios súbitos vespertinos en la humedad relativa y velocidad del viento.
   *Fuente:* [SNIF - Estadísticas de Incendios Forestales](https://snif.cnf.gob.mx/estadisticas-de-incendios/)
2. **Eficacia de Modelos de Machine Learning:**
   Revisiones científicas internacionales (*Jain et al., 2020*) demuestran que algoritmos de gradient boosting como XGBoost superan el 85% de precisión espacial en la predicción de ignición al combinar topografía, clima y humedad de la vegetación viva (LFMC).
   *Fuente:* [Jain et al., 2020 - Environmental Reviews](https://doi.org/10.1139/er-2020-0019)
3. **Latencia Inasumible de Sensores Térmicos:**
   Aunque la red NASA FIRMS (VIIRS/MODIS) es excelente para monitorear anomalías térmicas activas, su latencia de notificación oscila entre **3 y 12 horas**. Para cuando se detecta el píxel térmico, el incendio ya ha consumido decenas o cientos de hectáreas.
   *Fuente:* [NASA FIRMS Earth Observation Data](https://earthdata.nasa.gov/earth-observation-data/near-real-time/firms)

---

## 4. Declaración Refinada del Problema

> [!quote] Declaración Formal Refinada
> *"Las brigadas comunitarias rurales, los agricultores ejidales y los coordinadores tácticos de incidentes (CONAFOR) operan bajo un déficit crítico de información en campo, al carecer de inteligencia predictiva guiada por machine learning para pronosticar la probabilidad de ignición a escala micro-territorial antes de que el fuego comience."*

---
*Notas vinculadas:* [[02 - Stakeholders & Empathy Maps]] | [[03 - User Journey & Pain Points]] | [[01 - National Challenge & Strategic Context]]
