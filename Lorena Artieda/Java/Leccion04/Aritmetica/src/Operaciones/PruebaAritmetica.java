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
    }

   public static void miMetodo(){
        //a=10;
        //b=12;
       System.out.println("Aqui hay otro metodo");
   }
}