package ejercicios;

import java.util.Scanner;

public class ej01 {
  public static void main(String[] args) {
    Scanner entrada = new Scanner(System.in);
    float[] arreglos = new float[5];
    System.out.println("Guardando datos ");
    for (int i = 0; i < 5 ; i++) {
      System.out.println( i + 1 + " Digite un número: ");
      arreglos[i] = entrada.nextFloat();
    }
  for (float i:arreglos){
    System.out.println( i + " ");
  }

  }
}
