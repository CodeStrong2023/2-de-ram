package Operaciones;

public class PruebaAritmetica {
    public static void main(String[] args) {
        int a= 10;//Variables locales
        int b= 7;//Memoria stack
        miMetodo();//Llamamos al metodo nuevo
        Aritmetica aritmetica1= new Aritmetica();
        aritmetica1.a= 3;
        aritmetica1.b=7;

        aritmetica1.sumarNumeros();
        //Para almacenar un objeto o los atributos se utilizal a memoria heap
        int resultado= aritmetica1.sumarConRetorno();
        System.out.println("resultado = " + resultado);

        int resultado2= aritmetica1.sumarConArgumentos(3,5);
        System.out.println("El resultado es: "+resultado2);

        Aritmetica aritmetica2= new Aritmetica(3,6);

        Persona persona1= new Persona("Ariel", "Betancud");
        System.out.println("persona1 = " + persona1);
        System.out.println("Persona nombre: "+ persona1.nombre);
        System.out.println("Persona apellido: "+ persona1.apellido);
    }

   public static void miMetodo(){
        //a=10;
        //b=12;
       System.out.println("Aqui hay otro metodo");
   }
}

//Clase default o package(Solo puede haber una clase publica)

class Persona{
    String nombre;
    String apellido;

    Persona(String nombre, String apellido){

        super(); //Llamado al contructor padre object
        //Imprimir imprimir= new Imprimir();
        new Imprimir().imprimir(this);
        this.nombre=nombre;
        this.apellido=apellido;
        System.out.println("Objeto persona usando this: "+ this);

    }

}

class Imprimir{
    public Imprimir(){
        super();//El contructor de la clase padre para reservar memoria
    }
    public void imprimir(Persona persona){
        System.out.println("Persona desde la clase imprimir: "+ persona);
        System.out.println("Impresion del objeto actual (this): "+ this);
    }
}