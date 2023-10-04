package Operaciones;

public class PruebaAritmetica {
    public static void main(String[] args) {
        Aritmetica aritmetica1= new Aritmetica();
        aritmetica1.a= 3;
        aritmetica1.b=7;

        aritmetica1.sumarNumeros();
        int resultado= aritmetica1.sumarConRetorno();
        System.out.println("resultado = " + resultado);

        int resultado2= aritmetica1.sumarConArgumentos(3,5);
        System.out.println("El resultado es: "+resultado2);
    }
}