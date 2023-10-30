package ejercicios;

import java.util.Scanner;

public class ej03 {
  public static void main(String[] args) {
    Scanner entrada = new Scanner(System.in);
    float numeros[] = new float[5];
    float negativos = 0;
    float positivos = 0;
    float mediaPositivos;
    float mediaNegativos;
    int conteo = 0;
    int contNegativos = 0;
    int contPositivos = 0;

    for (int i = 0; i < 5 ; i++) {
      System.out.println("Ingrese un numero");
      numeros[i] = entrada.nextFloat();
      if (numeros[i] > 0){
        positivos += numeros[i];
        contPositivos++;
      } else if (numeros[i] < 0) {
        negativos += numeros[i];
        contNegativos++;
      } else {
        conteo++;
      }
    }

    if (contPositivos == 0){
      System.out.println(" No hay media de positivos");
    } else {
      mediaPositivos = positivos / contPositivos;
      System.out.println("La media de positivos es: " + mediaPositivos);
    }
    if (contNegativos == 0){
      System.out.println(" No hay media de negativos");
    } else {
      mediaNegativos = negativos / contNegativos;
      System.out.println("La media de negativos es: " + mediaNegativos);
    }

    System.out.println("la cantidad de 0 es:" + conteo);


  }
}
