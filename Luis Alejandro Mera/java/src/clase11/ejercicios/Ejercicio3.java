package clase11.ejercicios;

import java.util.Scanner;

public class Ejercicio3 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int numeros[] = new int[5];
        int numerosPositivos = 0;
        int numerosNegativos = 0;
        for (int i = 0; i < numeros.length; i++) {
            System.out.print("Ingrese el número de la posición " + i + " : ");
            numeros[i] = Integer.parseInt(scanner.nextLine());
            if (numeros[i] >= 0) {
                numerosPositivos = numerosPositivos + numeros[i];
            }
            if (numeros[i] < 0) {
                numerosNegativos = numerosNegativos + numeros[i];
            }
        }


        for (int i = 0; i < numeros.length; i++) {
            System.out.println("En la posición " + i + " = " + numeros[i]);
        }
        int mediaPositivos = numerosPositivos / numeros.length;
        int mediaNegativos = numerosNegativos / numeros.length;
        System.out.println("mediaNegativos = " + mediaNegativos);
        System.out.println("mediaPositivos = " + mediaPositivos);
    }
}
