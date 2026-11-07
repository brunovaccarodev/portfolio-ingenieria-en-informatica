# 🔌 Comunicación Cliente-Servidor con Sockets en Java

Implementación de una arquitectura cliente-servidor utilizando sockets TCP en Java, diseñada para gestionar la comunicación bidireccional y el intercambio de datos en red.

---

## 🚀 Tecnologías y Conceptos
* **Lenguaje:** Java (Programación Orientada a Objetos).
* **Librerías / APIs:** `java.net.*` (Sockets, ServerSocket), `java.io.*` (I/O streams), Concurrencia (Hilos / Threads).

---

## 🛠 Cómo ejecutarlo

1. **Compila los archivos fuente:**
   Abre una terminal en la carpeta del proyecto y compila ambas clases:

       javac MiServidor.java MiCliente.java

2. **Inicia el Servidor:**
   Ejecuta primero el servidor para que quede a la escucha de conexiones entrantes:

       java MiServidor

3. **Ejecuta el Cliente:**
   En otra pestaña o ventana de la terminal, inicia el cliente para conectarte al servidor:

       java MiCliente