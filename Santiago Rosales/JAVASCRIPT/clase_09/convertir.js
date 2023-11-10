// Convertir string a number
let MiNumero = "10";
console.log(typeof MiNumero);
let edad = Number(MiNumero);
console.log(typeof edad);

let MiNumero2 = 18;
console.log(typeof MiNumero2);
let edad2 = String(MiNumero2);
console.log(typeof edad2);
if(edad2 >= 18){
    console.log("Puede votar")
}
else{
    console.log("No puede votar")
}