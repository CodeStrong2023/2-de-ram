//Ejercicio para encontrar numeros pares e impares

let numero = 10;

if(numero % 2 == 0) {
    console.log("Es un número par");
} else {
    console.log("Es un número impar");
}
//Ejercicio es mayor de edad


let edad = 420, adulto =18;

if (edad >= adulto) {
    console.log("Es una persona adulta");
} else {
    console.log("Usted es una persona menor de edad");
}

// Ejercicio Dentro del rango
let detroRango = 5;
let valMin = 0;
let valMax = 10;

if(detroRango >= valMin && detroRango <= valMax) {
    console.log("Estas dentro del rango establecido");
} else {
    console.log("Estas fuera del rango establecido");
}
// Ejercicio si el padre puede asistir al juego de su hijo
let vacaciones = false;
let diaDescanso = false;

if (vacaciones || diaDescanso) {
  console.log("El padre puede asistir al juego de su hijo");
} else {
  console.log("El padre puede asistir al juego de su hijo");
}

// Operador ternario 
let resultado2 = vacaciones || diaDescanso ? "El padre puede asistir al juego de su hijo" : "El padre puede asistir al juego de su hijo";

// Operador ternario 
let resultado = 3 > 2 ? "Verdadero" : "Falso";
console.log(resultado);

// Convertir string a number
let miNumero = "21"; //es una cadena
console.log(typeof miNumero);

let edad1 = Number(miNumero); // Función 
console.log(typeof edad);


// Función isNaN
let edad2 = "10x"
if(isNaN(edad2)) { // El número puede venir en un string, solo verifica que no tenga letras
    console.log("La variable edad2 no son solo números");
} else {
    console.log("La variable edad2 es un número");
}

if(edad >= 18) {
    console.log("Puede votar");
} else {
    console.log("No puede votar");
}
//operador ternario
let resultado3 = edad >= 18 ? "Puede votar" : "No puede votar";
console.log(resultado2);