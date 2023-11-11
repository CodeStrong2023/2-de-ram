
// Evitar repetir un código

let days = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sábado", "Domingo"];


let day = 1 

switch (day) {
  case 1:
    console.log("Hoy es Lunes");
    break;
  case 2:
    console.log("Hoy es Martes");
    break;
  case 3:
    console.log("Hoy es Miercoles");
    break;
  case 4:
    console.log("Hoy es Jueves");
    break;
  case 5:
    console.log("Hoy es Viernes");
    break;
  case 6:
    console.log("Hoy es Sábado");
    break;
  case 7:
    console.log("Hoy es Domingo");
    break;
  default:
    console.log("No es un día válido");
    break;
}


// Evitar repetir un código versión mejorada
let days2 = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sábado", "Domingo"];

function getDay(n) {
  if(n < 1 || n > 7) {
    throw new "No es un día válido";
  }

  return days2[n-1];
}

console.log(getDay(1));

// Ejercicios con meses del año

let months = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"];

let month = 1;

switch (month) {
  case 1:
    console.log("Enero");
    break;
  case 2:
    console.log("Febrero");
    break;
  case 3:
    console.log("Marzo");
    break;
  case 4:
    console.log("Abril");
    break;
  case 5:
    console.log("Mayo");
    break;
  case 6:
    console.log("Junio");
    break;
  case 7:
    console.log("Julio");
    break;
  case 8:
    console.log("Agosto");
    break;
  case 9:
    console.log("Septiembre");
    break;
  case 10:
    console.log("Octubre");
    break;
  case 11:
    console.log("Noviembre");
    break;
  case 12:
    console.log("Diciembre");
    break;
  default:
    console.log("No es un mes válido");
    break;
}

// Ejercicios con meses del año versión mejorada

let months2 = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"];

function getMonth(n) {
  if(n < 1 || n > 12) {
    throw new "No es un mes válido";
  }

  return months2[n-1];
}


console.log(getMonth(1));