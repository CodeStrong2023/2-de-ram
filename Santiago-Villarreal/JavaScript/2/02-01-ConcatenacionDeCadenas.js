var nombre = 'Jose';
var apellido = 'Montes';
var nombreCompleto = nombre + ' ' + apellido;
console.log(nombreCompleto);
var nombreCompleto2 = 'Ariel' + ' ' + 'Betancud';
console.log(nombreCompleto2);
var juntos = nombre + 219;
console.log(juntos)
juntos = nombre + 78 + 17;
console.log(juntos)
juntos = 78 + 17 + nombre;
console.log(juntos);

nombre += apellido;
console.log(nombre)

let x,y; // crear variables en una misma linea
x = 17, y = 21; // asignar varias variables en una sola linea
let z = x + y;
console.log(z)

let _1num = 31;
let rompiendo = "rompe";

console.log(_1num)
console.log(rompiendo)

// No se recomienda el uso de var, se usan las variables let y const

let nombre = "Pedro";
console.log(nombre);

const apellido = "Lepes"; // las constantes no pueden ser reasignadas
console.log(apellido);

// Inconvenientes del uso de var

var edad = 10;
edad = 30;

console.log(edad);

function mostrarEdad() {
    var edad = 14
    console.log(edad); // NO se modifica la edad fuera de la función
}

mostrarEdad();
console.log(edad);

if(true) {
    var edad = 50
    console.log(edad);
}

console.log(edad); // Se modifica la edad dentro del if 
