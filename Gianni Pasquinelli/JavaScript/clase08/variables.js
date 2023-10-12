// var let y const

// dice que no se usa mas var, se usa let y const 

let nombre = 'Gianni';
console.log(nombre);

const apellido = 'Pasquinelli';

// var es global, let es local dentro de un bloque de codigo

function saludo() {
    var nombre2 = 'Astor';
    console.log(nombre2);
}

// console.log(nombre2); // no se puede acceder a nombre2 porque es local de la funcion

if (true) {
    var edad = 14;
    console.log(edad);
}
console.log(edad); // se puede acceder a edad porque es global


