import java.util.Scanner;

public class Ciclos004 {
  public static void main(String[] args) {
    Scanner entrada = new Scanner(System.in);
    int numero, conteo = 0;
    System.out.println("Digite un número: ");
    numero = Integer.parseInt(entrada.nextLine());
    while( numero >= 0) {
      System.out.println("El numero " + numero + " es positivo");
      conteo++;
      System.out.println("Digite otro número: ");
      numero = Integer.parseInt(entrada.nextLine());
    }
    System.out.println("Ingreso " + conteo + " números positivos" );
  }
}
