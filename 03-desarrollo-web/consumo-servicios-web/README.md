    # 🌐 Consumo de Servicios Web REST (GET & POST con Fetch API)

Práctica de integración con servicios web externos utilizando **JavaScript (ES6+)** y la API nativa `fetch()`, combinando el manejo de Promesas (`.then/.catch`) y funciones asíncronas (`async/await`).

---

## 🚀 Funcionalidades y Arquitectura

1. **Consulta de Datos (`GET` - SWAPI):**
   * Consumo del endpoint público `https://swapi.info/api/people`.
   * Filtrado del conjunto de resultados mediante `Array.prototype.slice()` y renderizado dinámico de listas anidadas semánticas en el DOM con *Template Literals*.
2. **Envío de Datos (`POST` - HTTPBin):**
   * Envío asíncrono de un *payload* estructurado hacia `https://httpbin.org/post`.
   * Configuración de cabeceras HTTP (`Content-Type: application/json`) y serialización del objeto mediante `JSON.stringify()`.
3. **Control de Errores:**
   * Validación de códigos de estado HTTP (`response.ok`) y captura de excepciones de red tanto en cadenas de promesas como en bloques `try/catch`.

---

## 💻 Cómo ejecutar el proyecto

1. Navega hasta el directorio del proyecto:

       cd 03-desarrollo-web/consumo-servicios-web

2. Abre `index.html` con **Live Server** en VS Code o directamente en el navegador.
3. Abre la **Consola de Desarrollador** (`F12` o `Cmd + Option + I` en macOS) para inspeccionar la respuesta JSON devuelta por el servidor tras la petición `POST`.