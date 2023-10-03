import java.util.Scanner;

public class ciclo03 {
  public static void main(String[] args) {
    Scanner entrada = new Scanner(System.in);
    System.out.println("Escriba un numero: ");
    var numero = Integer.parseInt(entrada.nextLine());
    while (numero != 0) {
      if (numero > 0) {
        System.out.println("El numero es positivo ");
      }
      else {
        System.out.println("El numero es negativo ");
      }
      numero = Integer.parseInt(entrada.nextLine());
    }

    System.out.println("terminado ");

  }
}
