var nombre = 'jose';
var apellido = 'Montes';
var nombreCompleto = nombre+' '+ apellido;
console.log(nombreCompleto);
var nombreCompleto2 = 'Ramon'+' '+'Ramos';
console.log(nombreCompleto2);
var juntos = nombre + 219;
console.log(juntos)
var juntos =  219 + 25 + nombre; // Primero se tratan como numeors y se realiza la suma y luego como cadena o str
console.log(juntos)

nombre += apellido;
console.log(nombre);

// Hoy ya no se usa var sino que se utiliza let y const
let nombre2 = "Ramon"; // utilizando var podemos reasignar en cualquier momento
console.log(nombre2);

const apellido2 = "Ramos"; // Una constante se puede utulizar en datos que no se puedan modificar, en casos de DNI, fechas de nacimiento, etc
console.log(apellido2);