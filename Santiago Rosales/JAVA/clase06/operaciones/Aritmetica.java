package clase06.operaciones;

public class Aritmetica {

    int a; // Java por default le asigna un 0 a los enteros
    int b;

    // Sobrecarga de constructores

    public Aritmetica() { // Constructor 1
        System.out.println("Se está ejecutando el constructor 1");
    }

    public Aritmetica(int a, int b) { // Constructor 1
        this.a = a;
        this.b = b;

        System.out.println("Se está ejecutando el constructor 2");
    }

    public void sumarNumeros() {
        int resultado = a + b;
        System.out.println("Resultado: " + resultado);
    }

    public int sumarConRetorno() {
        return a + b;
    }

    public int sumarConArgumentos(int a, int b) {
        this.a = a;
        this.b = b;
        return this.a + this.b;
    }
}