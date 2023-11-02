
package aritmetica;

public class PruebaAritmetica {
    public static void main(String[] args) {
        var a = 10; //variables locales
        int b = 7; // memoria stack
        miMetodo();
        aritmetica aritmetica1 = new aritmetica();
        aritmetica1.a = 3;
        aritmetica1.b = 7;
        aritmetica1.sumarNumeros(); 

        // memoria heap = objetos y atributos
        
        int resultado = aritmetica1.sumarConRetorno();
        System.out.println("resultado = " + resultado);
        
        resultado = aritmetica1.sumarConArgumentos(12, 26);
        System.out.println("resultado usando argumentos = " + resultado);
        
        System.out.println("aritmetica a: " + aritmetica1.a);
        System.out.println("arimetica b: " + aritmetica1.b);
        
        aritmetica aritmetica2 = new aritmetica(5,8);
        System.out.println("aritmetica2 = " + aritmetica2.a);
        System.out.println("aritmetica2 = " + aritmetica2.b);
    }
    public static void miMetodo(){
        //int a = 10;
        System.out.println("Aquí hay otro metodo");
    }
}
