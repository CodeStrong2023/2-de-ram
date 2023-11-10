package clase12.ejercicios;

import java.util.Scanner;

public class Ejercicio5 {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Ingrese el número de filas: ");
        int nFilas = scanner.nextInt();
        System.out.print("Ingrese el número de columnas: ");
        int nCol = scanner.nextInt();
        int matriz[][] = new int[nFilas][nCol];
        int filas[] = new int[nFilas];
        int columnas[] = new int[nCol];
        int sumaFilas;
        int sumaCol;

        System.out.println("Rellenado de la matriz");
        for (int i = 0; i < nFilas; i++) {
            for (int j = 0; j < nCol; j++) {
                System.out.print("Matriz [" + i + "] [" + j + "]: ");
                matriz[i][j] = scanner.nextInt();
            }
        }

        System.out.println("Mostrando la matriz");
        for (int i = 0; i < nFilas; i++) {
            for (int j = 0; j < nCol; j++) {
                System.out.print(matriz[i][j] + " ");
            }
            System.out.println("");
        }
        System.out.println("");

        // Sumando filas
        int posFilas = 0;
        for (int i = 0; i < nFilas; i++) {
            sumaFilas = 0;
            for (int j = 0; j < nCol; j++) {
                sumaFilas += matriz[i][j];
            }
            filas[posFilas] = sumaFilas;
            posFilas++;
        }

        // Sumando columnas
        int posCol = 0;
        for (int i = 0; i < nFilas; i++) {
            sumaCol = 0;
            for (int j = 0; j < nCol; j++) {
                sumaCol += matriz[i][j];
            }
            columnas[posCol] = sumaCol;
            posCol++;
        }

        System.out.println("\nLa suma de filas es: ");
        for (int i = 0; i < nFilas; i++) {
            System.out.print(filas[i] + " - ");
        }
        System.out.println("");

        System.out.println("\nLa suma de columnas es: ");
        for (int i = 0; i < nCol; i++) {
            System.out.print(columnas[i] + " - ");
        }
        System.out.println("");
    }

}
