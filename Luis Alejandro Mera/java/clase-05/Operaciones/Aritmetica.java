package Operaciones;

public class Aritmetica {

  int a; // Java por default le asigna un 0 a los enteros
  int b;

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
