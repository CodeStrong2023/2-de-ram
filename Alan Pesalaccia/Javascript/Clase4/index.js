var name = "Alan";
console.log(name);
console.log(typeof name);
name = 3;
console.log(name);
console.log(typeof name);

var objeto = {
  nombre: "Alan",
  apellido: "Pesalaccia",
  telefono: "21321",
};

console.log(typeof objeto);

// Tipos booleanos
var bandera = true;
console.log(bandera);
console.log(typeof bandera);

// Tipo de datos función
function miFuncion() {}

console.log(miFuncion);
console.log(typeof miFuncion);

// Tipo de dato symbol
var simbolo = Symbol("Mi symbol")
console.log(simbolo);
console.log(typeof simbolo);

// Tipo de dato clase
class Persona {
    constructor(nombre, apellido){
        this.nombre = nombre
        this.apellido = apellido
    }
}

console.log(Persona);
console.log(typeof Persona);
