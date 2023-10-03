import java.util.Scanner;

public class Ciclos03 {
  public static void main(String[] args) {
    Scanner entrada = new Scanner(System.in);
    int numero;
    System.out.println("Digite un número: ");
    numero = Integer.parseInt(entrada.nextLine());
    while (numero != 0) {
      if(numero % 2 == 0) {
        System.out.println("El número ingresado " + numero + " es par." );
      }else {
        System.out.println("El número ingresado " + numero + " es impar." );
      }
      System.out.println("Digite otro número: ");
      numero = Integer.parseInt(entrada.nextLine());
    }
    System.out.println("el 0 finaliza el programa ");
  }
}
