// No se recomienda el uso de var, se usan las variables let y const

let nombre = "Pedro";
console.log(nombre);

const apellido = "Flores"; // las constantes no pueden ser reasignadas
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