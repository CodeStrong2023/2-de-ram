package Operaciones;

public class PruebaAritmetica {
    public static void main(String[] args) {
        var a = 10; //variables locales
        int b = 7; //Memoria stack
        miMetodo(); //Llamamos al metodo nuevo
        Aritmetica aritmetica1 = new Aritmetica();
        aritmetica1.a = 3;
        aritmetica1.b = 7;
        aritmetica1.sumarNumeros();
        //Para almacenar un objeto o los atributos se utiliza la memoria heap
        int resultado = aritmetica1.sumarConRetorno();
        System.out.println("resultado = " + resultado);

        resultado = aritmetica1.sumarConArgumentos(12, 26);
        System.out.println("resultado usando argumentos = " + resultado);

        System.out.println("aritmetica1 a: " + aritmetica1.a);
        System.out.println("aritmetica1 b: " + aritmetica1.b);

        Aritmetica aritmetica2 = new Aritmetica(5, 8);
        System.out.println("aritmetica2 = " + aritmetica2.a);
        System.out.println("aritmetica2 = " + aritmetica2.b);
        //aritmetica1 = null; nunca utilizar esto, no se debe hacer
        //System.gc(); método para limpiar residuos, es pesado, no utilizar
    }

    public static void miMetodo() {
       //a = 10; //Una variable esta limitada
        System.out.println("Aquí hay otro metodo");

    }
}