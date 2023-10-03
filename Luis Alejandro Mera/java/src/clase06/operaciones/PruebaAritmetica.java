package clase06.operaciones;


public class PruebaAritmetica {

    public static void main(String[] args) {

        // Variables locales del main
        int a = 8;
        int b = 7; // Memoria stack solo almacena la referencia del objeto

        // Llamamos al método creado
        miMetodo();


        Aritmetica aritmetica1 = new Aritmetica(); // Estamos apuntando al constructor 1
        System.out.println("Valor de a: " + aritmetica1.a);
        System.out.println("Valor de b: " + aritmetica1.b);

        // aritmetica1 = null; deja el objeto nulo, no se debe utilizar ya que el compilador limpia los residuos que puede dejar el objeto en memoria

        Aritmetica aritmetica2 = new Aritmetica(2,3); // Estamos apuntando al constructor 2
        System.out.println("Valor de a: " + aritmetica2.a);
        System.out.println("Valor de b: " + aritmetica2.b);
    }

    public static void miMetodo() {
        int a = 10; // Variable local de miMetodo
        System.out.println("Aquí miMetodo");
    }
}
