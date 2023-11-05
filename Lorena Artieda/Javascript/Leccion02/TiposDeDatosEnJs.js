//Tipos de datos en JavasScript
/*La sintaxis en lo que es comentarios
es muy similar a la de Java
reamente diriamos es identica
*/

var name = "Lorena";
console.log(name);
console.log(typeof name);
name = 3;
console.log(name);
console.log(typeof name);

var objeto = {
  nombre: "Lorena",
  apellido: "Artieda",
  telefono: "323332",
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

//Tipo de dato undefined

var x;
console.log(x);
console.log(typeof x);


// null: significaausencia de un valor
var y = null;
console.log(y);
console.log(typeof y); // null no es un tipo de dato, pero su origine es object

// Tipo de dato array y Empty String
var autos = ["Citroen", "Audi", "BMW", "Ford"];
console.log(autos);
console.log(typeof autos); // Pregunta que tipo de dato es

var z = "";
console.log(z); // Esto se refiere a una cadena vacía
console.log(typeof z);