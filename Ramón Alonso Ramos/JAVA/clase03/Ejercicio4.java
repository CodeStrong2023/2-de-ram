package clase03;

import javax.swing.*;
import java.util.Scanner;

public class Ejercicio4 {
    public static void main(String[] args) {
        int number;
        int counter = 0;
        // Con clase scanner
 /*
        Scanner entry = new Scanner(System.in);
        System.out.println("Introduzca un número");
        number = Integer.parseInt(entry.nextLine());

        while (number >= 0) {
            counter++;
            System.out.println("Se van ingresando " + counter + " números");
            System.out.println("Introduzca otro número");
            number = Integer.parseInt(entry.nextLine());
        }
        System.out.println("Proceso finalizado se ingresaron " + counter + " números");
        */
        // Con JOptionPane
        number = Integer.parseInt(JOptionPane.showInputDialog("Digite un número"));

        while (number  >= 0) {
            counter++;
            System.out.println("Se van ingresando " + counter + " números");
            number = Integer.parseInt(JOptionPane.showInputDialog("Digite otro número"));
        }
        System.out.println("Proceso finalizado se ingresaron " + counter + " números");

    }
}
