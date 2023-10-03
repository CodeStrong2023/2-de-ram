import java.util.Scanner;

public class Ciclos05 {
  public static void main(String[] args) {
    Scanner entrada = new Scanner(System.in);
    int numero, aleatorio, conteo = 0;
    aleatorio = (int) (Math.random()*100);
    do {
      System.out.println(" Digite un número: ");
      numero = Integer.parseInt(entrada.nextLine());
      if (numero < aleatorio){
        System.out.println("Ingrese un número mayor ");
      }else if (numero > aleatorio) {
        System.out.println("digite un número menor " );
      }else {
        System.out.println("acertó, son igulaes!! " );
      }
      conteo++;
    } while (numero != aleatorio);{
      System.out.println("Adivinaste en "+ conteo + " intentos");
    }
  }
}
