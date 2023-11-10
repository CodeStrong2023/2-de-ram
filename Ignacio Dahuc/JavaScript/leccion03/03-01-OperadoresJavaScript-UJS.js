//Ejercicio para encontrar números pares e impares

let parImpar = 10;
if(parImpar % 2 == 0){
    console.log("Es un número PAR");
}
else{
    console.log("Es un número IMPAR");
}

//Ejercicio: es mayor de edad

let edad = 14, adulto = 18;
if(edad >= adulto){
    console.log('Usted es una persona adulta');
}
else{
    console.log('Usted es una persona menor de edad');
}

//Ejercicio: dentro de un rango
let dentroRango = 10; //Aquí vamos a ir cambiando el valor
let valMin = 0, valMax = 10;
if(dentroRango >= valMin && dentroRango <= valMax){
    console.log('Esta dentro del rango establecido');
}
else{
    console.log('Esta fuera del rango establecido');
}

// Ejercicio: si el padre puede asistir al juego de su hijo
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
let miNumero = "12"; 
console.log(typeof miNumero);

let edad1 = Number(miNumero); // Función Number() tranforma los string a tipo number
console.log(typeof edad);

if(edad >= 18) {
        console.log("Puede votar");
    } else {
    console.log("No puede votar");
}

let resultado3 = edad >= 18 ? "Puede votar" : "No puede votar";
console.log(resultado2);

// Función isNaN
let edad2 = "10x"
if(isNaN(edad2)) { // El número puede venir en un string, solo verifica que no tenga letras
    console.log("La variable edad2 no son solo números");
} else {
    console.log("La variable edad2 es un número");
}