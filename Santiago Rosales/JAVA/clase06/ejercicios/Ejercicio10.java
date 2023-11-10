package clase06.ejercicios;

import java.util.Scanner;
import javax.swing.JOptionPane;

public class Ejercicio10 {

    public static void main(String[] args) {
        // conScanner();
        conJOptionPane();
    }

    public static void conScanner() {
        Scanner entry = new Scanner(System.in);

        int total = 0;

        for (var i = 1; i <= 10; i++) {
            System.out.println("N° " + i + " Ingrese un número: ");
            int number = Integer.parseInt(entry.nextLine());
            total += number;
        }

        System.out.println(
                "La suma total de los 10 números ingresados es: " + total
        );
    }

    public static void conJOptionPane() {
        int total = 0;

        for (var i = 1; i <= 10; i++) {
            int number = Integer.parseInt(
                    JOptionPane.showInputDialog("N° " + i + " Ingrese un número: ")
            );
            total += number;
        }

        System.out.println(
                "La suma total de los 10 números ingresados es: " + total
        );
    }
}