---
title: "07. Evaluación Conceptual Multidimensional"
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
  - conceptual-assessment
  - trl-2
  - engineering-dimensions
  - feasibility
  - gap-analysis
---

# 📐 07. Evaluación Conceptual Multidimensional
## TERRA-FIRE: Auditoría de Coherencia Tecnológica para Transición de TRL 2 a TRL 3

---

## 1. Metodología de Evaluación por Dimensiones de Ingeniería

Para determinar formalmente si el proyecto **TERRA-FIRE** posee la solidez teórica, científica y metodológica indispensable para evolucionar desde el nivel **TRL 2 (Concepto Tecnológico Formulado)** hacia **TRL 3 (Prueba de Concepto Experimental en Laboratorio)**, la propuesta se sometió a una evaluación estandarizada a través de **seis dimensiones críticas de ingeniería**.

Cada dimensión se califica bajo una escala rigurosa:
- **STRONG (Fuerte):** Respaldo empírico y teórico completo, sin bloqueos técnicos ni incertidumbres críticas no mitigadas.
- **ACCEPTABLE (Aceptable):** Viable pero requiere ajustes menores en la fase de prototipado.
- **WEAK (Débil):** Presenta brechas fundamentales o supuestos no contrastados que impiden la inversión de recursos.

---

## 2. Matriz de Validación Conceptual (Deliverable 7)

![Deliverable 7: Conceptual Validation Matrix](assets/activity-3-conceptual-validation-matrix.png)

| Dimensión de Validación | Calificación | Evaluación Fundamentada y Evidencia Arquitectónica Concreta | Brecha Conceptual Remanente (Objetivo de Experimentación TRL 3) |
| :--- | :---: | :--- | :--- |
| **1. Problem-Solution Fit**<br>*Alineación operativa con brigadas rurales* | **STRONG** | El concepto ataca directamente la causa raíz documentada de los desastres por incendios en México: la latencia de información y la desconexión rural. Al reemplazar la detección orbital post-ignición (retraso de 3 a 12 horas) por un pronóstico anticipatorio de 48 a 72 horas entregado offline a ejidatarios y brigadistas, la solución interviene antes de que las quemas agrícolas escapen de control. Los dolores de usuario y mapas de empatía (Actividad 1) se resuelven explícitamente. | • Validar la comprensión textual y el apego conductual de las Cédulas Informativas en español mediante entrevistas participativas con ejidatarios durante TRL 3. |
| **2. Scientific Foundation**<br>*Física biofísica y teoría termodinámica* | **STRONG** | Respaldado por literatura exhaustiva revisada por pares (Chuvieco et al., 2020; Seager et al., 2015; Jain et al., 2020). El acoplamiento biofísico entre el agotamiento de humedad vegetal (NDMI/LFMC) y la demanda evaporativa atmosférica (VPD) está gobernado por leyes termodinámicas comprobadas. La superioridad algorítmica de los árboles aumentados por gradiente en datos tabulares geoespaciales está matemáticamente probada. | • Calibración empírica del gradiente térmico adiabático ambiental ($\Gamma = -0.0065\text{ }^\circ\text{C/m}$) en cañadas montañosas profundas sujetas a inversiones térmicas micro-locales. |
| **3. Technology Fit**<br>*Compatibilidad del stack y viabilidad edge* | **STRONG** | La pila tecnológica (XGBoost, TreeSHAP, Sentinel-2/1, ERA5-Land, MapLibre GL) empata perfectamente con los requisitos operativos sin desajustes de arquitectura. XGBoost procesa matrices tabulares con máxima eficiencia en CPU; TreeSHAP genera explicaciones exactas en $< 5\text{ ms}$; y la vectorización con Tippecanoe resuelve el cuello de botella del ancho de banda móvil. Se descartaron tecnologías desproporcionadas (como Vision Transformers gigantes o costosas mallas IoT). | • Calibración fina de la tolerancia de simplificación Douglas-Peucker en Tippecanoe para garantizar que la orografía abrupta de las cañadas no se suavice excesivamente. |
| **4. Data / Resource Fit**<br>*Datos abiertos y presupuesto Zero-CapEx* | **STRONG** | El 100% de las fuentes de datos esenciales (Copernicus Sentinel-2 MSI, Sentinel-1 SAR, ECMWF ERA5-Land, Copernicus GLO-30 DEM, históricos de CONAFOR y NASA FIRMS) son de acceso abierto, gratuitas y fueron verificadas en la Actividad 2. La infraestructura de cómputo requiere únicamente CPUs estándar en la nube, garantizando un presupuesto de inversión en hardware cero (**Zero-CapEx**) y costos operativos marginales ($< \$10\text{ USD/mes}$ para reentrenamientos batch). | • Administrar las cuotas de tasa de transferencia y latencia de descarga al ingerir lotes masivos de gránulos Sentinel-2 históricos desde el Copernicus Data Space Ecosystem. |
| **5. Testability**<br>*Rigor empírico y diseño falsable* | **STRONG** | Todos los supuestos clave están formulados como hipótesis falsables ($H_1$ a $H_4$) equipadas con procedimientos experimentales controlados. Ningún componente se apoya en fenómenos especulativos o inmedibles. Existen datasets históricos completos (2018–2024) para ejecutar validaciones cruzadas por bloques espaciales realistas. | • Establecer agrupamientos geográficos disjuntos (*spatial holdouts*) que garanticen cero fuga de información espacial entre microcuencas contiguas. |
| **6. Measurability**<br>*Métricas cuantitativas y líneas base concretas* | **STRONG** | Se definieron y justificaron métricas cuantitativas objetivas: Spatial Block PR-AUC, Macro F1-Score, Brier Calibration Score, latencia de CPU (ms/vóxel), tamaño de archivo vectorial (MB) y tasa de cuadros por segundo en WebGL (FPS). Los criterios subjetivos (*\"el sistema funciona bien\"*) quedaron totalmente erradicados del marco experimental. | • Definir el umbral operativo óptimo de decisión de probabilidad ($\tau \in [0.5, 0.7]$) que equilibre la prevención de escapes con la mitigación de la fatiga de alertas en brigadistas. |

---

## 3. Síntesis y Conclusión de Madurez Tecnológica

> [!tip] Veredicto de la Evaluación Conceptual
> El proyecto **TERRA-FIRE** obtiene una calificación unánime de **STRONG** en las seis dimensiones de ingeniería. 
> 
> La arquitectura conceptual está completamente blindada contra los modos de falla típicos de proyectos de IA geoespacial (desbalance ciego, fuga espacial, opacidad algorítmica y saturación de red en campo). Las brechas identificadas no son barreras arquitectónicas bloqueantes, sino parámetros empíricos a calibrar durante la experimentación de laboratorio en TRL 3.

---
*Documentos relacionados:* [[02 - Conceptual Solution Model & Component Flow]] | [[05 - Validation Criteria & Performance Metrics]] | [[06 - Experimental Design & Validation Protocols]] | [[08 - PoC Readiness Decision & Experimental Scope]]
