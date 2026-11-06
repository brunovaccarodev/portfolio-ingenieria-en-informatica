# 📊 Calculadora de Estadísticas en Tiempo Real (JS + DOM)

Aplicación web interactiva desarrollada en **JavaScript Vanilla (ES6+)** que permite registrar series numéricas dinámicamente y calcular métricas estadísticas descriptivas en tiempo real.

---

## 🚀 Funcionalidades y Lógica Implementada

* **Validación de Datos:** Conversión de entradas mediante `parseFloat()` y verificación estricta con `!isNaN()` para prevenir errores de cálculo por entradas vacías o no numéricas.
* **Cálculo Estadístico Funcional:**
  * **Cantidad de muestras:** Conteo dinámico mediante la propiedad `.length` del arreglo de estado.
  * **Valores Extremos (Máximo y Mínimo):** Evaluación del conjunto de datos implementando el operador de propagación (*Spread Operator* `...`) sobre `Math.max()` y `Math.min()`.
  * **Promedio Aritmético:** Sumatoria acumulada de elementos mediante el método de orden superior `Array.prototype.reduce()`.
* **Gestión de Estado y Eventos:** Manejo de eventos del DOM (`addEventListener`) desacoplados para el registro incremental de datos y el reinicio completo del estado en memoria (`valores = []`).

---

## 🛠 Estructura de Archivos

* `index.html`: Interfaz de usuario con controles de entrada y campos de salida para visualización de métricas.
* `app.js`: Lógica de negocio, validación de entradas, cálculo estadístico y manipulación del DOM.

---

## 💻 Cómo ejecutar el proyecto

1. Navega hasta el directorio del proyecto:

       cd 03-desarrollo-web/calculadora-estadisticas

2. Abre el archivo `index.html` en cualquier navegador web moderno o utiliza la extensión **Live Server** en VS Code.