---
title: "TERRA-FIRE: Executive Summary"
project: "TERRA-FIRE"
academic_degree: "Ingeniería en Tecnologías de la Información e Innovación Digital"
authors:
  - "Angel Emilio Gutierrez Lozano (4341)"
  - "Emiliano Betanzos Valtierra (4795)"
advisor: "Dr. Sergio Valadez Godínez"
date: "2026-11-10"
status: "TRL 3 Validated -> READY FOR SEGMENTATION & READY FOR TRANSFORMATION (9.43/10)"
tags:
  - executive-summary
  - pitch
  - terra-fire
  - trl-3
  - digital-transformation
  - pattern-discovery
---

# 📄 Resumen Ejecutivo: Proyecto TERRA-FIRE

> [!abstract] Declaración de Propósito
> **TERRA-FIRE** es un ecosistema socio-técnico de pronóstico hiperlocal de incendios forestales (10–20 m) y cartografía táctica 100% offline, concebido para empoderar a ejidatarios, brigadistas comunitarios, CONAFOR y Protección Civil mediante alertas microclimáticas explicables generadas **48 a 72 horas antes de la ignición**.

---

## 1. Diagnóstico Crítico y Evidencia Empírica en México (`matrix_v1.parquet`)

A través del análisis programático de **$N = 18,275$ observaciones diarias vóxel-tiempo** (25 nodos regionales en Aguascalientes y la Reserva Biológica Sierra Fría durante 2023–2024), el proyecto **TERRA-FIRE** demostró estadísticamente las fallas del paradigma reactivo tradicional:

1. **Detección Tardía (3 a 12 Horas Post-Ignición):** Las plataformas oficiales (SPPIF de CONAFOR a resolución de $\ge 10\text{ km}$ y satélites térmicos NASA FIRMS VIIRS/MODIS) alertan cuando el fuego ya escapó hacia cañadas escarpadas.
2. **Gatillo Antrópico Agrícola Probado ($p < 10^{-30}$):** Las ventanas de ignición ocurren a una distancia mediana de **$420.0\text{ m}$** de bordes agrícolas ($\Delta = -60.53\%$ frente a $1,200.0\text{ m}$ en condiciones base) y **$150.0\text{ m}$** de caminos rurales ($\Delta = -62.32\%$). El **63.58% de todos los incendios** ($557 / 876$) inician en **Pastizal Inducido** por escapes de *roza y quema*.
3. **Pre-Acondicionamiento Termodinámico y Desecación:** Previo a la ignición, el Déficit de Presión de Vapor ($VPD_{max}$) se incrementa **+16.38%** (superando el umbral crítico de $2.0\text{ kPa}$), la humedad relativa mínima cae a una mediana de **18.0%** y el índice de humedad foliar ($NDMI$) se desploma **-42.50%**.
4. **Convergencia Piro-Antropogénica en el Cuadrante IV de PCA ($28.1\times$ Riesgo):** Al comprimir las 12 variables de alto y mediano impacto en **3 Componentes Principales ortogonales (`PC1`, `PC2`, `PC3`)** que retienen el **87.87% de la varianza total**, el **Cuadrante IV ($\text{PC1} > 0 \land \text{PC2} \le 0$: Interfaz Agrícola Seca)** concentra el **68.61% de todos los incendios forestales** ($601 / 876$) con una tasa de ignición de **11.54%** (y **23.34%** en el Ápice Extremo).
5. **Brecha de Conectividad de Última Milla:** Más del **85% de los corredores montañosos carecen de cobertura 4G/5G**, inutilizando las aplicaciones web convencionales en el frente de combate.

---

## 2. La Propuesta de Valor y Transformación Digital de TERRA-FIRE

```text
Copernicus Sentinel-2 (Reflectancia 10–20m) + Sentinel-1 SAR (Todo Clima)
                                + 
ECMWF ERA5-Land (VPD Downscaled Adiabáticamente a -0.0065 °C/m)
                                + 
Motor Predictivo XGBoost + Cédulas Explicables TreeSHAP (< 5 ms)
                                + 
PWA Táctica Offline (Teselas Vectoriales Tippecanoe .pbf < 12 MB)
                                +
Gobernanza Socio-Técnica (Protocolo SOP-72H + Carta Ejidal No Punitiva)
                                = 
PREVENCIÓN HIPERLOCAL 48–72H PRE-IGNICIÓN A COSTE CERO DE SENSORES (ZERO-CAPEX)
```

### Pilares del Blueprint de Transformación Digital (Actividad 4 — Tecnologías Disruptivas):
- **Semáforo Visual de Quema Segura (NOM-015) y Carta No Punitiva:** Interfaz de 3 colores (Verde / Amarillo / Rojo) respaldada por acuerdos de *Asamblea Ejidal* que garantizan **cero multas**, logrando que el campesino difiera quemas voluntariamente cuando $VPD > 2.0\text{ kPa}$.
- **Protocolo de Despacho Preventivo (`SOP-72H`):** Boletín automatizado a las 06:00 AM con **Cédulas de Riesgo Local TreeSHAP** que permite a CONAFOR y Protección Civil pre-posicionar brigadas y pipas 48 horas antes en bordes del Cuadrante IV.
- **Red de *"Promotores Digitales Forestales"* y Kioscos Wi-Fi:** Jóvenes locales acreditados y puntos de sincronización comunitaria que actualizan el mapa offline en `< 15 segundos`.
- **Cero Inversión en Hardware (Zero-CapEx):** Operación estatal completa en la nube por `< $15 USD/mes`, proyectando una **reducción de 30%–50% en escapes agrícolas** y un **ahorro de 25%–40% en horas de vuelo de helicópteros**.

---

## 3. Estado Actual de Madurez y Dictámenes Oficiales (Noviembre 2026)

> [!tip] Veredictos Formales Alcanzados
> 1. **Ciencia de Datos (Actividades 3, 4, 5 y 6 Completadas):** Estatus **`READY FOR SEGMENTATION`** (TRL 3 Validado; Feature Store Parquet 100% íntegro, 12 regresiones OLS validadas y espacio latente 3D `['PC1', 'PC2', 'PC3']` listo para clustering no supervisado).
> 2. **Tecnologías Disruptivas (Actividad 4 Completada):** Estatus **`READY FOR TRANSFORMATION`** (**Puntaje compuesto: 9.43 / 10.0**), con estrategia de adopción de stakeholders, plan de gestión del cambio **Prosci ADKAR + Kotter** y hoja de ruta de implementación en 5 etapas (12 meses).

*Para detalles exhaustivos, consultar:* [[00 - TERRA-FIRE Central Dashboard]] | [[07 - Digital Transformation Blueprint]] | [[Activity 6. Pattern Discovery Challenge]]
