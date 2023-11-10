
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
    mensaje = "Buenas noches";
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

//evitar repetir codigo
//let days = ['Lunes','Martes','Miercoles','Jueves','Viernes','Sabado','Domingo'];
/*switch(days){
    Case 'Lunes':
        console.log('Hoy es' + days)
        break;
    Case 'Martes':
        console.log('Hoy es' + days)
        break;
    Case 'Miercoles':
        console.log('Hoy es' + days)
        break;
    Case 'Jueves':
        console.log('Hoy es' + days)
        break;
    Case 'Viernes':
        console.log('Hoy es' + days)
        break;
    Case 'Sabado':
        console.log('Hoy es' + days)
        break;
    Case 'Domingo':
        console.log('Hoy es' + days)
        break;
    default:
        break;

}*/
let days = 1;
switch(days){
    case 1:
        console.log('Hoy es lunes')
        break;
    case 2:
        console.log('Hoy es martes')
        break;
    case 3:
        console.log('Hoy es miercoles')
        break;
    case 4:
        console.log('Hoy es jueves')
        break;
    case 5:
        console.log('Hoy es viernes')
        break;
    case 6:
        console.log('Hoy es sabado')
        break;
    case 7:
        console.log('Hoy es domingo')
        break;
    default:
        console.log("Error en el ingreso del dia de la semana");
        break;
}

//opcion mejorada
let days2 = ['Lunes','Martes','Miercoles','Jueves','Viernes','Sabado','Domingo'];

function getDay(n){
    if(n < 1 || n > 7){
        throw new Error('out of range');
    }
    return days2[n-1];
}
console.log(getDay(5));

let months = ['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre'];

function getMonth(n){
    if(n < 1 || n > 12){
        throw new Error('out of range');
    }
    return months[n-1];
}
console.log(getMonth(7));
