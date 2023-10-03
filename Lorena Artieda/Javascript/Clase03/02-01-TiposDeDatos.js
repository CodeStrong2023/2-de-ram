//Tipos de datos en javascript
/*La sintaxis en lo que es comentarios
es muy similar a la de Java
realmente diriamos es identica*/

var nombre= 'Ariel';//string
console.log(nombre);
nombre=7;
console-log(nombre);
var numero=3000;//numerico

var objeto={
    nombre: "Ariel",
    apellido:"Betancud",
    telefono:"23568907565"
}

console.log(objeto)

//Tipo boolean
var bandera = true;
console.log(bandera);

//Funciones

function miFuncion(){
    console.log("Hola mundo")
}

//Simbol

var simbolo= Symbol("Mi simbolo");
console.log(simbolo);

//Clase

class Persona {
    constructor(nombre, apellido){
        this.nombre=nombre;
        this.apellido=apellido;
    }
}

console.log(Persona);

//Undefined

var x;
console.log(x);

//null Significa ausencia de un valor
var y= null; //null no es un tipo de dato pero su origen es object

//Tipo de dato array y Empty String

var autos = ['Citroen', 'Audi', 'Ford'];
console.log(autos);

var z= '';
console.log(z);
console.log(z);
