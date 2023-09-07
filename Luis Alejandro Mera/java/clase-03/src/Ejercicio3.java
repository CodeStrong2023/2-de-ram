import javax.swing.*;
import java.util.Scanner;

public class Ejercicio3 {
    public static void main(String[] args) {
        int number;

        // Con clase scanner

        /*
        Scanner entry = new Scanner(System.in);
        System.out.println("Introduzca un número");
        number = Integer.parseInt(entry.nextLine());

        while (number != 0) {
            if (number % 2 == 0) {
                System.out.println("El número " + number + " es par");
            } else {
                System.out.println("El número " + number + " es impar");
            }
            System.out.println("Introduzca otro número");
            number = Integer.parseInt(entry.nextLine());
        }
        System.out.println("Proceso finalizado");
*/
        // Con JOptionPane
        number = Integer.parseInt(JOptionPane.showInputDialog("Digite un número"));

        while (number != 0) {
            if (number % 2 == 0) {
                System.out.println("El número " + number + " es par");
            } else {
                System.out.println("El número " + number + " es impar");
            }
            number = Integer.parseInt(JOptionPane.showInputDialog("Digite otro número"));
        }
        System.out.println("Proceso finalizado");

    }
}
