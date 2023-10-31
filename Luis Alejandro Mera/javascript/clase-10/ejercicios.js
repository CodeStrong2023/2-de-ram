
// Ejercicio 1: Calcualr la estación del año

let mes = 4;
let estacion;

if(mes == 1 || mes == 2 || mes == 3 || mes == 12) {
    estacion = "Verano";
} 
else if (mes == 3 || mes == 4 || mes == 5 ) {
    estacion = "Otoño";
}
else if (mes == 6 || mes == 7 || mes == 8 ) {
    estacion = "Invieron";
}
else if (mes == 9 || mes == 10 || mes == 11 ) {
    estacion = "Primavera";
} else {
    estacion = "Valor incorrecto"
}

console.log(`El valor corresponde a la estación de: ${estacion}`);


// Ejercico 2: Hora del día

let horaDía = 9;
let mensaje;

if(horaDía >= 6 && horaDía <= 11 ) {
    mensaje = "Buenos días";
}
else if (horaDía >= 12 && horaDía <= 16) {
    mensaje = "Buenas siestas ";
}
else if (horaDía >= 17 && horaDía <= 19) {
    mensaje = "Buenas tardes";
}
else if (horaDía >= 20 && horaDía <= 23) {
    mensaje = "Bunas noches";
} else {
    mensaje = "Valor incorrecto"
}

console.log(mensaje);

// Estructura switch

switch (mes) {
    case 1: case 2: case 12:
        estacion = "verano"
        break;
    case 3: case 4: case 5:
        estacion = "Otoño"
        break;
    case 6: case 7: case 8:
        estacion = "Invieron"
        break;
    case 9: case 10: case 11:
        estacion = "Primavera"
        break;
    default:
        estacion = "Valor incorrecto"
        break;
}

console.log(estacion);