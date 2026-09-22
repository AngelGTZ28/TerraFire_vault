---
title: "Análisis de Impacto y Consideraciones Éticas"
subject: "Disruptive Technologies"
code: "LITD9A"
authors:
  - "Angel Emilio Gutierrez Lozano (4341)"
  - "Emiliano Betanzos Valtierra (4795)"
advisor: "Dr. Sergio Valadez Godínez"
tags:
  - impact-analysis
  - ethics
  - data-sovereignty
  - disruptive-technologies
---

# ⚖️ Análisis de Impacto y Consideraciones Éticas

Cualquier intervención tecnológica en territorios rurales y ecosistemas forestales debe evaluarse críticamente para maximizar beneficios legítimos y prevenir efectos adversos no intencionados.

---

## 1. Matriz de Impacto Multidimensional

| Dimensión | Impactos Positivos Directos | Riesgos Potenciales o Consecuencias No Deseadas | Estrategia de Mitigación / Gobernanza |
| :--- | :--- | :--- | :--- |
| **Social y Comunitaria** | Empoderamiento de comunidades ejidales; prevención de pérdidas de vidas de combatientes voluntarios; fortalecimiento de la organización comunitaria. | Resistencia al cambio si la tecnología se percibe como una imposición externa o intento de supervisión policial. | Co-diseño participativo con brigadistas; talleres comunitarios prácticos; interfaz no punitiva. |
| **Económica** | Reducción dramática del gasto de emergencia en helicópteros de supresión; protección del patrimonio maderable y agrícola de las familias rurales. | Falsos positivos que cancelen innecesariamente quemas de rastrojo, atrasando el ciclo de siembra de autoconsumo. | Calibración conservadora del umbral de decisión del modelo ML; ventanas de quema alternativas sugeridas. |
| **Ambiental** | Reducción de emisiones masivas de gases de efecto invernadero ($CO_2$, metano y partículas $PM_{2.5}$); protección de cuencas hidrológicas y fauna. | Falsa sensación de seguridad que relaje las medidas físicas básicas (guardarrayas y líneas negras). | La plataforma refuerza que la alerta climática es un apoyo, pero las buenas prácticas físicas de quema siguen siendo obligatorias. |
| **Institucional** | Transición hacia una cultura de decisiones preventivas basadas en datos y evidencia auditable; mayor optimización presupuestal. | Deslinde de responsabilidades institucionales culpando al algoritmo en caso de siniestros imprevistos. | Establecer marcos claros de que el modelo es un sistema de soporte a la decisión (DSS), no un decisor autónomo legal. |

---

## 2. Principios Éticos y Soberanía de Datos

> [!important] Soberanía y Equidad en la Inteligencia Artificial Rural
> 1. **No Criminalización del Campesino:** Los datos de calor o predicción generados por TERRA-FIRE jamás deben utilizarse como herramienta punitiva para multar o perseguir a agricultores que realizan quemas tradicionales de subsistencia. El propósito del sistema es asesorar, proteger y guiar.
> 2. **Soberanía y Datos Abiertos:** TERRA-FIRE se cimienta en datos abiertos de la humanidad (Copernicus, OpenStreetMap, CONAFOR, INEGI). Los algoritmos y modelos desarrollados deben permanecer abiertos y auditables por la comunidad científica y ejidal mexicana, evitando la privatización o monopolización del conocimiento sobre el riesgo ambiental.
> 3. **Transparencia Algorítmica (Anti Caja Negra):** Toda recomendación emitida por el sistema debe poder desglosarse en factores comprensibles (viento, sequedad del aire, pendiente), eliminando predicciones arbitrarias o sesgadas.

---
*Notas vinculadas:* [[04 - Future Scenarios 2026-2036]] | [[02 - Stakeholders & Empathy Maps]] | [[01 - Problem Definition & Context]]
