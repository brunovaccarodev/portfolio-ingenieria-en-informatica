# 📄 Maquetación Semántica: Perfil Profesional en HTML5

Implementación de una página de perfil y biografía profesional aplicando los estándares de **HTML5 semántico**, priorizando la jerarquía documental, accesibilidad y buenas prácticas de seguridad web.

---

## 🎯 Objetivos Técnicos

* **Estructura Semántica (W3C):** Uso de etiquetas con significado estructural (`article`, `header`, `section`) en lugar de contenedores genéricos (`div`), facilitando la indexación y la lectura por tecnologías de asistencia.
* **Codificación y Adaptabilidad:** Configuración de metadatos (`charset="UTF-8"` y `viewport`) para garantizar la correcta visualización de caracteres en español y el escalado en dispositivos móviles.
* **Seguridad en Enlaces Externos:** Implementación del atributo `rel="noopener noreferrer"` junto con `target="_blank"` para prevenir vulnerabilidades de tipo *reverse tabnabbing* al abrir enlaces hacia perfiles externos.

---

## 🏗 Arquitectura del Documento

El árbol del DOM está organizado bajo la siguiente jerarquía lógica:

* `article.biografia`: Contenedor principal independiente que encapsula toda la ficha profesional.
  * `header`: Encabezado principal con el nombre (`h1`) y el título profesional destacado.
  * `section` (Sobre mí): Párrafos descriptivos del perfil actual y ubicación.
  * `section` (Educación): Lista desordenada (`ul` / `li`) detallando la formación universitaria.
  * `section` (Contacto): Canales de comunicación profesional con esquemas `mailto:` e hipervínculos externos seguros.

---

## 🚀 Cómo visualizar el proyecto

No requiere instalación de dependencias ni servidores externos:

1. Navega hasta el directorio del proyecto:

       cd 03-desarrollo-web/biografia

2. Abre el archivo `index.html` directamente en cualquier navegador web moderno, o ejecútalo mediante la extensión **Live Server** en VS Code.