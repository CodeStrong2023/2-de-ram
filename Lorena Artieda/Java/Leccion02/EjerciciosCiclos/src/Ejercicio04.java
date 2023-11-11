/* Ejercicio 4: pedir numeros hasta que se teclee uno negativo,
y mostrar cuantos numeros se ha introducido.
Lo hacemos primero con la clase Scanner
luego lo hacemos con la clase JOPtionPane
*/

import java.util.Scanner;

public class Ejercicio04 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int contador = 0;

        System.out.println("Introduce números (introduce un número negativo para finalizar):");

        while (true) {
            System.out.print("Introduce un número: ");
            int numero = scanner.nextInt();

            if (numero < 0) {
                break;  // Salir del bucle si se introduce un número negativo
            }

            contador++;
        }

        System.out.println("Se han introducido " + contador + " números.");
    }

}
