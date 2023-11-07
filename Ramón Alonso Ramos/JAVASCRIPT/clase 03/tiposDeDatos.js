/* TAMBIEN SE PUEDE COMENTAR DE LA MISMA FORMA QUE SE REALIZA EN JAVA*/
//TIPOS DE DATOS: las variables son dinámicas, con la porpiedad typeof podemos visualziar que tipo de dato estamos utilizando en la variable 

// STRING
var nombre = 'Ramon';
console.log(nombre);

// TIPO NUMERICO

var numero = 10000;
console.log(numero);

var objeto = {
    nombre : "Ramon",
    apellido : "Ramos",
    telefono: 2654125478

}
console.log(objeto)

// Boolean True or False

var bandera = true;
console.log(bandera);

// TIPO DE DATO FUNCIÓN 
function miFuncion() {
console.log(typeof miFuncion);
}

// TIPO DE DATO SYMBOL
var simbolo = Symbol("Mi simbolo");
console.log(typeof simbolo);

//Tipo de dato clase 
class Persona {
    constructor(nombre,apellido){
        this.nombre = apellido;
    }
}

console.log(Persona);

// TIPO DE DATO UNDEFINED, es decir es una variable no definida pero sí es un dato a diferencia de null
var x;
console.log(x);

// null: ausencia de valor, la variable está vacía
var y = null; // null no es un tipo de dato, pero su origen es object
console.log(y);

// Tipo de dato array y Empty String

var futbol = ['Messi', 'Julián Álvarez', 'Rondón', 'Aliendro'];
console.log(futbol)
console.log(typeof futbol) // Preguntamos que tipo de dato es:

var z = "";
console.log(z) // SIGNIFICA QUE ES UNA CADENA VACÍA, SINO LE PONDRÍAMOS "" APARECERÍA COMO UNDEFINED
console.log(typeof z)

