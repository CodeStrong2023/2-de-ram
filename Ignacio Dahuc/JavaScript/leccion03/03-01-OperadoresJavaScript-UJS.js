//Ejercicio para encontrar números pares e impares

let parImpar = 10;
if(parImpar % 2 == 0){
    console.log("Es un número PAR");
}
else{
    console.log("Es un número IMPAR");
}

//Ejercicio: es mayor de edad

let edad = 14, adulto = 18;
if(edad >= adulto){
    console.log('Usted es una persona adulta');
}
else{
    console.log('Usted es una persona menor de edad');
}

//Ejercicio: dentro de un rango
let dentroRango = 10; //Aquí vamos a ir cambiando el valor
let valMin = 0, valMax = 10;
if(dentroRango >= valMin && dentroRango <= valMax){
    console.log('Esta dentro del rango establecido');
}
else{
    console.log('Esta fuera del rango establecido');
}