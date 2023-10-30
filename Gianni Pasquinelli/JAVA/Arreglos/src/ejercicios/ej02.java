package ejercicios;

import java.util.Scanner;

public class ej02 {
  public static void main(String[] args) {
    Scanner entrada = new Scanner(System.in);
    float numero[] = new float[5];
    System.out.println("Datos de array");
    for (int i = 0; i < 5 ; i++) {
      System.out.println((i+1) + "ingrese un numero:" );
      numero[i] = entrada.nextFloat();
    }

    for (int i = 4; i >= 0 ; i--) {
      System.out.println(i + " ");
    }

  }

}
