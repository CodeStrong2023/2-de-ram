// ejer 1: calcular estacion del año
// ej2 2: hora del dia



let mes = 8;

if (mes != NaN && mes >= 1 && mes <= 12) {
    if (mes >= 3 && mes <= 5) {
        console.log('Estamos en otoño');
    } else if (mes >= 6 && mes <= 8) {
        console.log('Estamos en invierno');
    } else if (mes >= 9 && mes <= 11) {
        console.log('Estamos en primavera');
    } else {
        console.log('Estamos en verano');
    }
} else {
    console.log('El mes ingresado no es valido');
}


let hora = 12;

if (hora != NaN && hora >= 0 && hora <= 24) {
    if (hora >= 6 && hora <= 12) {
        console.log('Buenos dias');
    } else if (hora >= 13 && hora <= 19) {
        console.log('Buenas tardes');
    } else if (hora >= 20 && hora <= 24) {
        console.log('Buenas noches');
    } else {
        console.log('Buenas madrugadas');
    }
}


// ej1 con switch y break

mes = 3;
switch (mes) {
    case 3:
    case 4:
    case 5:
        console.log('Estamos en otoño');
        break;
    case 6:
    case 7:
    case 8:
        console.log('Estamos en invierno');
        break;
    case 9:
    case 10:
    case 11:
        console.log('Estamos en primavera');
        break;
    case 12:
    case 1:
    case 2:
        console.log('Estamos en verano');
        break;
    default:
        console.log('El mes ingresado no es valido');
        break;
}