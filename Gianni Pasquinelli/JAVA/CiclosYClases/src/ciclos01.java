import java.util.Scanner;

public class ciclos01 {
  public static void main(String[] args) {
  Scanner entrada = new Scanner(System.in);
    int numero, cuadrado;
    System.out.println("Escriba un número: ");
    numero = Integer.parseInt(entrada.nextLine());
    while (numero >= 0){
      cuadrado = (int)Math.pow(numero, 2);
      System.out.println(numero + " al cuadrado da: " + cuadrado);
      System.out.println("Escriba un número");
      numero = Integer.parseInt(entrada.nextLine());
    }
    System.out.println("Terminado");




  }
}
