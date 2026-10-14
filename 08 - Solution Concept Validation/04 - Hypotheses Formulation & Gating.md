---
title: "04. Formulación de Hipótesis y Criterios de Falsabilidad"
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
  - hypotheses
  - scientific-method
  - falsifiability
  - variables
  - metrics-gating
---

# 🎯 04. Formulación de Hipótesis y Criterios de Falsabilidad
## TERRA-FIRE: Hipótesis Científicas Formales para el Proof of Concept (TRL 3)

---

## 1. Rigor Metodológico en la Formulación de Hipótesis

Siguiendo el método científico para investigación aplicada en ingeniería, las preguntas enfocadas se traducen en **cuatro hipótesis formales y comprobables**. Cada hipótesis identifica explícitamente:
- **Variables Independientes (VI):** Aquellas manipuladas de forma controlada en el entorno experimental.
- **Variables Dependientes (VD):** Las respuestas y métricas cuantitativas medidas empíricamente.
- **Variables de Control (VC):** Factores ambientales, arquitectónicos o computacionales mantenidos constantes.
- **Relaciones Esperadas y Umbrales Matemáticos:** Criterios numéricos que definen si la hipótesis se sostiene o se rechaza.

---

## 2. Matriz Formal de Hipótesis (Deliverable 4)

![Deliverable 4: Hypothesis Matrix](assets/activity-3-hypothesis-matrix.png)

| ID | Declaración Formal de la Hipótesis | Variable(s) Independiente(s) | Variable(s) Dependiente(s) | Variables de Control | Resultado Matemático Esperado |
| :---: | :--- | :--- | :--- | :--- | :--- |
| **H1** | Un modelo de clasificación XGBoost entrenado con variables ambientales multimodales espacialmente bloqueadas (Sentinel-2 NDMI/SAVI, ERA5-Land VPD con downscaling, pendiente Copernicus DEM y proximidad a fronteras agrícolas) alcanzará un Área Bajo la Curva Precision-Recall espacial ($\text{PR-AUC} \ge 0.75$) y un $\text{F1-Score} \ge 0.70$ en bloques espaciales no vistos, superando estadísticamente al SPPIF ($\text{PR-AUC} \le 0.45$) en al menos un 60%. | **Pila de características multimodal** (NDMI, VPD con downscaling, pendiente/orientación DEM, agua en suelo, distancia a caminos/parcelas) vs. línea base meteorológica de fuente única. | **Métricas de Clasificación** sobre el target 48–72h ($Y \in \{0, 1\}$):<br>• Spatial Block PR-AUC<br>• Macro F1-Score<br>• Brier Reliability Score | • Límites de validación cruzada por bloques espaciales ($> 25\text{ km}$ buffer)<br>• Partición temporal (2018–22 train, 2023–24 test)<br>• Razón de muestreo de desbalance (1:100) | • Spatial $\text{PR-AUC} \ge 0.75$<br>• $\text{F1-Score} \ge 0.70$<br>• Brier Score $\le 0.12$<br>• **Ganancia estadísticamente significativa** sobre SPPIF ($p < 0.001$, prueba DeLong) |
| **H2** | La atribución local de características TreeSHAP aplicada a predicciones de alto riesgo ($P(\text{Ignición}) \ge 0.50$) calculará los vectores exactos de Shapley en una latencia media de $\le 5.0\text{ ms}$ por vóxel en un procesador de un solo núcleo estándar, con los top-3 factores causales mostrando 100% de concordancia determinista entre ejecuciones repetidas y 0% de contradicciones físicas con las reglas de combustión ($\text{VPD} > 2.5\text{ kPa}$, $\text{NDMI} < 0.15$). | **Algoritmo explicador TreeSHAP** ejecutado sobre el ensamble de árboles serializado de XGBoost; tamaño de muestra de fondo ($N=100$ clusters K-means). | **Rendimiento de Atribución:**<br>• Latencia de reloj CPU (ms/vóxel)<br>• Correlación de rango Spearman ($\rho$) de top-3 valores Shapley<br>• Cumplimiento de reglas físicas de combustión (%) | • Ejecución en un solo hilo de CPU (Intel i5 / Ryzen 5 @ 2.4 GHz)<br>• Profundidad máxima de árbol fija ($\text{max\_depth} = 6$)<br>• Tamaño del ensamble ($n_{\text{trees}} = 300$) | • Latencia media $\le 3.5\text{ ms}$<br>• Desv. Est. $\sigma < 0.8\text{ ms}$<br>• Concordancia de rango $\rho = 1.0$<br>• **100% de alineación física** con umbrales de combustión |
| **H3** | El empaquetado de superficies continuas de riesgo pre-ignición a escala municipal ($1,500\text{ km}^2$, $> 100,000$ vóxeles) en polígonos simplificados codificados vía Tippecanoe en teselas Protocol Buffer (`.pbf`) logrará un tamaño de archivo $\le 12.0\text{ MB}$ (reducción $> 85\%$ vs. GeoTIFF crudo), habilitando renderizado interactivo offline vía MapLibre GL a $\ge 45\text{ FPS}$ con carga inicial $\le 1.5\text{ s}$ en hardware Android de gama baja en modo avión. | **Tolerancia de contorno** de vectorización ($\Delta p = 0.25$); simplificación Douglas-Peucker ($\varepsilon = 0.0001^\circ$); rango de zooms Tippecanoe (z10–z15). | **Métricas Móviles en el Borde:**<br>• Tamaño de paquete serializado (MB)<br>• Huella en disco IndexedDB (MB)<br>• Tiempo de render inicial en canvas (s)<br>• Cuadros por segundo (FPS) en paneo/zoom continuo | • Extensión municipal ($1,500\text{ km}^2$)<br>• Perfil del dispositivo: Android 11, 3–4GB RAM, CPU ARMv8<br>• Motor gráfico WebGL 2.0<br>• Modo avión estrictamente activado | • Tamaño total de teselas $\le 12.0\text{ MB}$<br>• Carga inicial $\le 1.2\text{ s}$<br>• Tasa sostenida $\ge 45\text{ FPS}$<br>• **Cero caídas de contexto WebGL** durante prueba de estrés de 60s |
| **H4** | Bajo condiciones de oscurecimiento óptico severo (máscara SCL de nubes $> 70\%$), un modelo XGBoost de doble rama que incorpore retrodispersión Sentinel-1 C-SAR dual-pol (VV, VH y razón cruzada VH/VV) emparejada con splines de decaimiento acumulado de VPD alcanzará un $\text{PR-AUC} \ge 0.70$, reteniendo al menos el 90% del desempeño en cielo despejado y superando a la persistencia óptica hacia adelante ($\text{PR-AUC} \le 0.54$) en $\ge 25\%$. | **Modalidad de censado bajo nubes:** Sentinel-1 C-SAR + spline de VPD de ERA5 vs. persistencia óptica hacia adelante (forward-fill NDMI). | **Confiabilidad Todo-Clima:**<br>• PR-AUC en subconjunto nublado<br>• Razón de retención de rendimiento ($\text{PR-AUC}_{\text{Nublado}} / \text{PR-AUC}_{\text{Despejado}}$)<br>• Calibración Brier en nubes | • Corrección radiométrica de terreno SNAP con DEM Copernicus<br>• Pasadas orbitales descendentes<br>• Muestra de prueba de incendios históricos nublados ($N \ge 150$) | • $\text{PR-AUC}$ en nubes $\ge 0.70$<br>• Razón de retención $\ge 92\%$<br>• Brier Score en nubes $\le 0.15$<br>• **Supera con significancia estadística** a la persistencia ($p < 0.01$) |

---

## 3. Principio de Falsabilidad Científica (Karl Popper)

> [!important] Criterio de Falsabilidad y Evaluación sin Ambigüedades
> Ninguna de las hipótesis planteadas utiliza adjetivos vagos como *"el sistema será eficiente"* o *"la IA mejorará la detección"*. Cada hipótesis define:
> 1. El valor numérico exacto de éxito (p. ej., $\text{PR-AUC} \ge 0.75$, latencia $\le 5.0\text{ ms}$, peso $\le 12\text{ MB}$, retención $\ge 90\%$).
> 2. La condición de hipótesis nula ($H_0$) bajo la cual el concepto sería considerado experimentalmente refutado.
> 3. La prueba estadística requerida (DeLong paired test, test de rangos Spearman, mediciones de reloj en hardware físico).

Esto garantiza que el proyecto TERRA-FIRE pueda auditarse de manera totalmente reproducible durante la fase empírica del Proof of Concept (TRL 3).

---
*Documentos relacionados:* [[03 - Critical Assumptions & Research Questions]] | [[05 - Validation Criteria & Performance Metrics]] | [[06 - Experimental Design & Validation Protocols]] | [[08 - PoC Readiness Decision & Experimental Scope]]
