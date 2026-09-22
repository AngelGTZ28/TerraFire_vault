---
title: "Actores, Personas y Mapas de Empatía"
subject: "Integrative Project III"
code: "LITD9A"
authors:
  - "Angel Emilio Gutierrez Lozano (4341)"
  - "Emiliano Betanzos Valtierra (4795)"
advisor: "Dr. Sergio Valadez Godínez"
tags:
  - empathy-map
  - user-personas
  - stakeholders
  - integrative-project
---

# 👥 Actores, Personas y Mapas de Empatía

El éxito de TERRA-FIRE radica en diseñar una herramienta tecnológica adaptada a los usuarios que viven y combaten el fuego en los bosques mexicanos.

---

## 1. Tabla de Identificación de Usuarios

![[assets/user-identification-table.png]]
*Figura 1: Clasificación de Grupos de Usuario para TERRA-FIRE (Sección 4 PDL).*

| Grupo de Usuario | Perfil y Características | Necesidades Operativas Centrales |
| :--- | :--- | :--- |
| **Primario: Ejidatarios y Líderes de Brigadas Comunitarias** <br> `[SELECCIONADO]` | Agricultores rurales y voluntarios de primera línea. Vasta experiencia empírica en campo pero baja alfabetización digital. Operan en áreas montañosas con cero cobertura móvil. | Saber **cuándo y dónde** patrullar preventivamente. Requerimiento de alertas visuales muy simples (semáforos verde/rojo) accesibles sin internet para programar quemas agrícolas seguras. |
| **Secundario: Despachadores Operativos CONAFOR** | Coordinadores tácticos regionales certificados en el Sistema de Comando de Incidentes (ICS). Administran presupuestos y despliegues de cuadrillas oficiales. | Mapas de probabilidad de ignición a 48–72 horas a resolución de 10–20 m para pre-posicionar camiones cisterna y brigadas oficiales. |
| **Terciario: Analistas de Riesgo de Protección Civil** | Oficiales de gobierno encargados de emitir declaratorias de emergencia y evacuaciones en la Interfaz Urbano-Forestal. | Modelos transparentes y explicables (XAI / SHAP) que justifiquen técnicamente órdenes de moratoria o evacuación preventiva ante la población. |

---

## 2. Arquetipos de Usuario (Personas)

### Persona Primaria: Don Manuel (52 años)
- **Rol:** Comisariado Ejidal y Jefe de Brigada Forestal Voluntaria en la Sierra Madre.
- **Contexto:** Cultiva maíz y frijol; organiza la limpieza de rastrojo previo a la temporada de siembra. Su teléfono es un Android de gama de entrada con batería limitada y sin señal celular en el bosque.
- **Frustración Mayor:** *"Nos enteramos de que una quema se salió de control cuando ya vemos el humo elevarse en la cañada; si supiéramos que el aire va a cambiar en la tarde, no prenderíamos fuego."*
- **Meta:** Proteger las parcelas del ejido, evitar multas o tragedias y asegurar que sus brigadistas regresen a salvo a casa.

### Persona Secundaria: Ing. Claudia (38 años)
- **Rol:** Despachadora Operativa en el Centro de Control de Incendios de CONAFOR.
- **Contexto:** Coordina 6 brigadas oficiales y 2 helicópteros cisterna sobre un área de más de 400,000 hectáreas con escasez de estaciones meteorológicas terrestres.
- **Frustración Mayor:** *"Los reportes satelitales de calor nos llegan con horas de retraso. Enviamos a la brigada y cuando llegan 3 horas después, el fuego saltó de 1 hectárea a 50 hectáreas."*
- **Meta:** Disponer de un mapa predictivo 72 horas antes que le permita decir: *"Mañana concentraremos los recursos en esta cañada específica."*

---

## 3. Mapa de Empatía (Ejidatario / Brigadista Rural)

![[assets/empathy-map-ejidatario.png]]
*Figura 2: Mapa de Empatía centrado en el usuario primario de campo (Sección 5 PDL).*

```mermaid
mindmap
  root((Ejidatario / Brigadista))
    ¿Qué Piensa?
      "¿Será realmente seguro quemar el rastrojo hoy?"
      "Las alertas de satélite solo avisan cuando el bosque ya arde"
      "Si supiera cómo vendrá el viento, colocaría mejor a mis hombres"
      "Los calendarios antiguos de quema ya no funcionan con este calor"
    ¿Qué Siente?
      Angustia de que una quema de rastrojo destruya el monte
      Abrumado por lo impredecible de la temporada de estiaje
      Frustración por no contar con pronósticos meteorológicos hiperlocales
      Inmensa responsabilidad por la vida de su cuadrilla voluntaria
    ¿Qué Dice?
      "No podemos parar el fuego una vez que entra al cañón seco"
      "Denme una luz verde o roja sencilla para saber si quemamos"
      "Para cuando llega el helicóptero, el daño ya está hecho"
      "Mi teléfono no tiene señal en la sierra; necesito la información guardada"
    ¿Qué Hace?
      Se guía por intuición visual para calcular la sequedad de las hojas
      Patrulla a ciegas grandes extensiones de monte esperando ver humo
      Intenta abrir apps del clima pero fallan por falta de datos móviles
      Toma decisiones críticas de combate con herramientas manuales
```

---
*Notas vinculadas:* [[01 - Problem Definition & Context]] | [[03 - User Journey & Pain Points]] | [[Offline-First Edge Architecture]]
