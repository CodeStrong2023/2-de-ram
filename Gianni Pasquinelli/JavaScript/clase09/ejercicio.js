// ej. comprobar si el padre puede asisitir al juego de su hijo

let vacaciones = false;
let diaDescanso = false;

if (vacaciones || diaDescanso) {
    console.log("El padre puede asistir al juego");
} else {
    console.log("El padre no puede asistir al juego");
}

// operador ternario
let resultado = 3 > 2 ? "verdadero" : "falso";
console.log(resultado)
let numero = 9;
resultado = numero % 2 == 0 ? "par" : "impar";
console.log(resultado)

// convertir un string a número
let miNumero = "10";
console.log(typeof miNumero);
let edad = Number(miNumero);
console.log(typeof edad);

if (edad >= 18) {
    console.log("Puede votar");
} else {
    console.log("No puede votar");
}

let resultado3 = edad >= 18 ? "Puede votar" : "No puede votar";


// isNaN = is Not a Number 

if (isNaN(edad)) {
    console.log("No es un número");
} else {
    if (edad >= 18) {
        console.log("Puede votar");
    } else {
        console.log("No puede votar");
    }
}
