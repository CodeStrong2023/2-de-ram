//Tipos de datos en javaScript
/*
La sintaxis es muy similar a java
*/
var nombre = "Ariel";
console.log(typeof nombre);
nombre = 7;
console.log(typeof nombre);
nombre = 12.3;
console.log(typeof nombre);
var numero = 3000; //tipo numerico
console.log(numero);
// tipo objeto
var objeto = {
    Nombre : "Ariel",
    apellido : "Betancud",
    telefono : "2614567893",
}
console.log(typeof objeto);

//Tipo dato booleano
var bandera = true;
console.log(bandera);

//tipo de dato funcion
function miFuncion(){}
console.log(typeof miFuncion);

//tipo simbol
var simbolo = Symbol("Mi simbolo");
console.log(simbolo);

//tipo clase
class Persona{
    constructor(nombre,apellido){
        this.nombre = nombre;
        this.apellido = apellido;
    }
}
console.log(Persona)

//tipo undefined
var x;
console.log(x);

x = undefined;
console.log(x)

// null:significa ausencia de valor
var y = null; //null no es un dato pero su origen es objeto
console.log(null);

//tipo de dato array y Empty string
var autos = ['citroen','audi','bmw','ford','chevrolet','renault'];
console.log(autos);
console.log(typeof autos);

var z = '';
console.log(z);

