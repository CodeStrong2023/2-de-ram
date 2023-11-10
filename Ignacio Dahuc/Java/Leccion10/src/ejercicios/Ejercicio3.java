package ejercicios;

import java.util.Scanner;

public class Ejercicio3 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int matriz[][] = new int[3][3];

        System.out.println("Rellenar Matriz");
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                System.out.print("Matriz ["+i+"] ["+j+"] : " );
                matriz[i][j] = Integer.parseInt(scanner.nextLine());
            }
        }

        System.out.println("Mostrar matriz original");
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                System.out.print(matriz[i][j] + " " );
            }
            System.out.println();

        }

        System.out.println("Mostrar matriz transpuesta");
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                System.out.print(matriz[j][i] + " " );
            }
            System.out.println();
        }
    }
}