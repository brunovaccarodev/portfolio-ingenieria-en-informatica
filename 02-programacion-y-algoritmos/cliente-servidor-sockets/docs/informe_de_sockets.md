# Informe de Resultados: Validación e Integración de Sockets (Java / Python)

## 1. Resumen Ejecutivo
Este documento detalla el análisis comparativo del estado operativo del sistema de comunicación cliente-servidor basado en Sockets TCP (desarrollado en Java) **antes** y **después** de la implementación de una suite de pruebas automatizadas utilizando `pytest` y la librería de serialización binaria `struct` en Python. El objetivo principal fue garantizar la robustez, el acoplamiento correcto del protocolo binario (`writeUTF` y `writeInt`) y la estabilidad frente a interacciones concurrentes.

---

## 2. Escenario 1: Estado Inicial (Antes del Cambio)
* **Condición del sistema:** Desarrollo aislado de la lógica de sockets (`MiServidor.java` y `MiCliente.java`).
* **Metodología de prueba:** Pruebas manuales mediante ejecución directa en terminal y entradas por consola (`Scanner`), sin validación automatizada.
* **Observaciones y Limitaciones:**
  * **Ausencia de automatización:** Cada modificación en la lógica exigía levantar manualmente los procesos y verificar visualmente las respuestas en consola, elevando el margen de error humano.
  * **Vulnerabilidad a desajustes de protocolo:** No existía una verificación estricta sobre el tamaño de los paquetes leídos (`DataInputStream`), lo que podía provocar bloqueos (*deadlocks*) o excepciones ante variaciones mínimas en la cabecera de 2 bytes de las cadenas UTF.
  * **Falta de métricas de tiempo:** Imposibilidad de medir la latencia o la tasa de éxito de las peticiones de manera repetible.

---

## 3. Escenario 2: Estado Actual (Después del Cambio)
* **Condición del sistema:** Integración de una suite de pruebas automatizadas con `pytest` que abarca tanto pruebas de caja negra al servidor como un entorno simulado (*mock server*) para el cliente.
* **Implementaciones realizadas:**
  * **Empaquetado binario homólogo:** Uso del módulo `struct` en Python para emular exactamente el comportamiento big-endian de Java (`>H` para cadenas UTF-8 y `>ii` para enteros de 4 bytes).
  * **Pruebas de Integración del Servidor (`test_servidor_java.py`):** Validación exitosa de la comunicación mediante sockets conectados al puerto `8080`, verificando tanto la recepción correcta de la suma aritmética como la selección aleatoria de frases.
  * **Pruebas del Cliente vía Subprocesos (`test_cliente_java.py`):** Simulación automática del comportamiento de usuario mediante la inyección de entradas (`stdin`) y levantamiento de un hilo servidor TCP local en Python.
* **Resultados Obtenidos:**
  * **Cobertura de ejecución:** 100% de las pruebas automatizadas superadas de forma exitosa (`2 passed in 0.39s`).
  * **Confiabilidad:** Sincronización exacta del protocolo de red, garantizando que la estructura de datos enviada y recibida sea idéntica en ambos lenguajes.

---

## 4. Tabla Comparativa de Resultados

| Métrica / Componente | Antes del Cambio (Manual) | Después del Cambio (Automatizado con Pytest) |
| :--- | :--- | :--- |
| **Tiempo de Validación** | Variable y dependiente de la interacción manual (~minutos por ciclo). | Instantáneo (~0.39 segundos para la suite completa). |
| **Detección de Errores** | Tardía (se descubrían en ejecución en tiempo real). | Inmediata (ante cualquier alteración en el protocolo binario). |
| **Reproducibilidad** | Baja (sujeta a tipeo manual y estado del entorno). | Alta (ejecución estandarizada mediante `python3 -m pytest`). |
| **Simulación de Clientes** | Limitada a pruebas interactivas de consola una por una. | Automatizada mediante hilos concurrentes y subprocesos. |

---

## 5. Aclaración sobre la Utilización de la IA
Para la conceptualización, diseño de los scripts de prueba en `pytest`, modelado de los flujos de bytes con `struct` y la redacción final de este informe técnico, se contó con la asistencia del modelo de lenguaje grande **Google Gemini** (Google, 2026). 

* **Rol del modelo:** Colaborador técnico en la depuración de la lógica de red, estructuración de consultas (*prompts*) orientadas a la interoperabilidad entre Java y Python, y documentación formal de los resultados.
* **Cita bibliográfica:** 
  > Google. (2026). *Gemini* [Modelo de inteligencia artificial]. https://gemini.google.com

---

## 6. Conclusiones y Próximos Pasos
La transición hacia un esquema de pruebas automatizadas permitió validar formalmente la interoperabilidad entre Java y Python a nivel de sockets de bajo nivel. Como próximos pasos, se sugiere:
1. Integrar la ejecución de los tests dentro de un flujo de integración continua (CI).
2. Ampliar los casos de prueba para contemplar escenarios de estrés con múltiples conexiones concurrentes.