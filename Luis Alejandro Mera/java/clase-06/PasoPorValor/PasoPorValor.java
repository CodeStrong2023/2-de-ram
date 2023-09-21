package PasoPorValor;

public class PasoPorValor {
  public static void main(String[] args) {

    int valorX = 20;
    cambioValor(valorX); // Solo envía una copia 
    System.out.println("valorX = " + valorX);

  }

  public static void cambioValor(int arg1) {
    arg1 = 15; // Solo se modifica en el entorno de este método
    System.out.println("arg1 = " + arg1);
  }
}
