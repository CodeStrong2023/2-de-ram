package clase05.operaciones;

public class PruebaAritmetica {

    public static void main(String[] args) {
        Aritmetica aritmetica1 = new Aritmetica();
        aritmetica1.a = 3;
        aritmetica1.b = 7;
        aritmetica1.sumarNumeros();

        int resultado = aritmetica1.sumarConRetorno();
        System.out.println(resultado);

        int resultado2 = aritmetica1.sumarConArgumentos(20, 30);
        System.out.println(resultado2);
    }
}
