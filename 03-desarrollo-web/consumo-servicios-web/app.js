const contenedor = document.getElementById("contenedor-resultados");

// 1. Petición GET utilizando Promesas (.then / .catch)
const obtenerPersonajes = () => {
    fetch("https://swapi.info/api/people")
        .then((res) => {
            if (!res.ok) {
                throw new Error(`Error HTTP: ${res.status}`);
            }
            return res.json();
        })
        .then((json) => {
            let itemsHTML = "";

            // Obtenemos solo los primeros 4 personajes de forma eficiente
            json.slice(0, 4).forEach((personaje) => {
                itemsHTML += `
                    <li>
                        <strong>Nombre: ${personaje.name}</strong>
                        <ul>
                            <li>Altura: ${personaje.height} cm</li>
                            <li>Peso: ${personaje.mass} kg</li>
                            <li>Año de nacimiento: ${personaje.birth_year}</li>
                        </ul>
                    </li>
                `;
            });

            contenedor.innerHTML = `<ul>${itemsHTML}</ul>`;
        })
        .catch((error) => {
            console.error("Error al obtener personajes:", error);
            contenedor.innerHTML = "<p>Hubo un error al cargar los datos.</p>";
        });
};

// 2. Petición POST utilizando Async / Await
const enviarDatos = async () => {
    const payload = {
        nombre: "Luke Skywalker",
        rango: "Jedi",
        planetaOrigen: "Tatooine",
        activo: true
    };

    try {
        const respuesta = await fetch("https://httpbin.org/post", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(payload)
        });

        if (!respuesta.ok) {
            throw new Error(`Error HTTP: ${respuesta.status}`);
        }

        const datos = await respuesta.json();
        console.log("Respuesta recibida del servidor (POST):", datos);
    } catch (error) {
        console.error("Error al enviar la solicitud:", error);
    }
};

obtenerPersonajes();
enviarDatos();