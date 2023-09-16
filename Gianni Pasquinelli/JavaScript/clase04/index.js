// tipo de dato booleano

var bandera = true;
console.log(bandera);
console.log(typeof bandera);

//  tipo función

function miFuncion(){
}
console.log(miFuncion);
console.log(typeof miFuncion);

var simbolo = Symbol("mi simbolo");
console.log(simbolo);
console.log(typeof simbolo);


// tipo clase es una función
class Persona{
  constructor(nombre, apellido){
    this.nombre = nombre;
    this.apellido = apellido;
  }
}
console.log(Persona);
console.log(typeof Persona);