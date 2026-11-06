let valores = [];
const valorDeEntrada = document.getElementById("valorDeEntrada");
const botonRegistrar = document.getElementById("botonRegistrar");
const botonReset = document.getElementById("botonReset");
const cantidad = document.getElementById("cantidad");
const promedio = document.getElementById("promedio");
const mayor = document.getElementById("mayor");
const menor = document.getElementById("menor");

// Evento 1: Registrar (Independiente)
botonRegistrar.addEventListener("click", () => {
    const valor = parseFloat(valorDeEntrada.value);

    if (!isNaN(valor)) {
        valores.push(valor);
        
        cantidad.value = valores.length;
        mayor.value = Math.max(...valores);
        menor.value = Math.min(...valores);
        promedio.value = valores.reduce((a, b) => a + b, 0) / valores.length;
        
        valorDeEntrada.value = "";
    } else {
        alert("Por favor, ingresa un número válido.");
    }
}); // <-- Aquí se cierra el evento de Registrar, aislando su lógica.

// Evento 2: Reset (Independiente y al mismo nivel estructural)
botonReset.addEventListener("click", () => {
    valores = []; // Vaciamos el arreglo correctamente
    valorDeEntrada.value = "";
    cantidad.value = "";
    promedio.value = "";
    mayor.value = "";
    menor.value = "";
});