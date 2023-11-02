
// Operador ternario 
let resultado = 3 > 2 ? "Verdadero" : "Falso";
console.log(resultado);

// Convertir string a number
let miNumero = "12"; 
console.log(typeof miNumero);

let edad = Number(miNumero); // Función Number() tranforma los string a tipo number
console.log(typeof edad);

if(edad >= 18) {
    console.log("Puede votar");
} else {
    console.log("No puede votar");
}

let resultado2 = edad >= 18 ? "Puede votar" : "No puede votar";
console.log(resultado2);

// Función isNaN
let edad2 = "10x"
if(isNaN(edad2)) { // El número puede venir en un string, solo verifica que no tenga letras
    console.log("La variable edad2 no son solo números");
} else {
    console.log("La variable edad2 es un número");
}

