---
title: "TERRA-FIRE: Executive Summary"
project: "TERRA-FIRE"
academic_degree: "Ingeniería en Tecnologías de la Información e Innovación Digital"
authors:
  - "Angel Emilio Gutierrez Lozano (4341)"
  - "Emiliano Betanzos Valtierra (4795)"
advisor: "Dr. Sergio Valadez Godínez"
date: "2026-09-21"
status: "TRL 2"
tags:
  - executive-summary
  - pitch
  - terra-fire
---

# 📄 Resumen Ejecutivo: Proyecto TERRA-FIRE

> [!abstract] Declaración de Propósito
> **TERRA-FIRE** es un sistema inteligente de pronóstico de riesgo de incendios forestales e interfaces tácticas sin conexión a internet, concebido para empoderar a ejidatarios y brigadistas comunitarios en México mediante alertas microclimáticas hiperlocales generadas 48 a 72 horas antes de la ignición.

---

## 1. El Diagnóstico Crítico de la Realidad Mexicana

En México, la gestión gubernamental del fuego opera históricamente bajo un **paradigma reactivo**:
1. **Detección Tardía:** Las plataformas oficiales (como el sistema SPPIF de CONAFOR o los satélites térmicos NASA FIRMS) detectan el fuego entre 3 y 12 horas después de que ya inició, cuando las llamas ya consumieron hectáreas y cobraron fuerza en cañadas empinadas.
2. **Causa Raíz Desatendida:** Más del **80% de los incendios forestales catastróficos** se originan en quemas agrícolas tradicionales (roza y quema) que se salen de control debido a ráfagas imprevistas de viento y deshidratación súbita de la vegetación.
3. **Ceguera de Datos en Campo:** En los ecosistemas forestales y montañosos de México existe menos de 1 estación meteorológica por cada 2,500 km². Los campesinos y brigadistas deben tomar decisiones de vida o muerte basándose en la intuición visual o en calendarios ancestrales que el cambio climático ha vuelto obsoletos.
4. **La Brecha de Conectividad:** Las zonas con mayor riesgo forestal carecen por completo de cobertura celular o red 4G/5G. Las aplicaciones web convencionales colapsan en el campo.

---

## 2. La Propuesta de Valor Disruptiva de TERRA-FIRE

TERRA-FIRE resuelve esta fricción mediante la convergencia de tecnologías abiertas y maduras:

```text
Copernicus Sentinel-2 (Reflectancia Óptica 10m) 
            + 
ECMWF ERA5-Land (Déficit de Presión de Vapor - VPD)
            + 
Modelo Predictivo XGBoost (Calibrado para desbalance extremo)
            + 
PWA Táctica Offline (MapLibre Vector Tiles + SQLite/WASM)
            = 
PREVENCIÓN HIPERLOCAL PRE-IGNICIÓN A COSTE CERO DE SENSORES
```

### Principales Diferenciadores:
- **Cero Inversión en Hardware (Zero CapEx):** No requiere instalar ni mantener costosas redes de sensores físicos en la sierra (las cuales sufren vandalismo, fallas de batería y desconexión). Aprovecha la flota satelital de acceso abierto Copernicus y reanálisis global ECMWF.
- **Granularidad de 10 a 20 Metros:** En lugar de predicciones climáticas regionales toscas de 10 km, evalúa la humedad del dosel arbóreo (NDMI) y la evaporación a nivel de cañada o parcela.
- **Ventana Preventiva Real (48–72 Horas):** Permite emitir moratorias comunitarias de quema agrícola antes de que se produzca una chispa y pre-posicionar brigadas y pipas en puntos neurálgicos.
- **Arquitectura Offline-First:** La Progressive Web App permite almacenar en caché municipal las teselas vectoriales ligeras (`.pbf`) y scores de riesgo, permitiendo navegación GPS en campo sin señal de red.
- **Inteligencia Artificial Explicable (XAI):** Uso de algoritmos TreeSHAP para explicar al despachador técnico el porqué de cada nivel de alerta (ejemplo: pendiente pronunciada + anomalía de VPD + deshidratación de biomasa).

---

## 3. Impacto Socioecológico Esperado

- **Protección de Vidas:** Disminución drástica del atrapamiento fatal de brigadistas en cañadas al ofrecer mapas de corredores de escape seguros.
- **Conservación Ecosistémica:** Protección de servicios ambientales críticos (captación de agua, biodiversidad y secuestro de carbono) alineados al **Eje Estratégico 4 de SECIHTI**.
- **Ahorro Presupuestal:** Reducción sustancial del gasto municipal y federal en horas de vuelo de helicópteros de supresión y maquinaria pesada, reorientando el presupuesto hacia el equipamiento preventivo comunitario.
- **Gobernanza Comunitaria:** Fortalecimiento del tejido ejidal sin criminalizar la actividad agrícola tradicional, transformando al campesino en el primer vigía preventivo del territorio.
