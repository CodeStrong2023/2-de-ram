

package arreglos;


import java.util.Scanner;

public class Ejercicio2 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int numeros[] = new int[5];

        for (int i = 0; i < numeros.length ; i++) {
            System.out.print("Ingrese el número de la posición " + i + " : ");
            numeros[i] = Integer.parseInt(scanner.nextLine());
        }
        for (int i = numeros.length - 1; i >= 0 ; i--) {
            System.out.println("En la posición " + i + " = " + numeros[i]);
        }
    }
}
