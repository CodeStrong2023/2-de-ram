package clase07;

import javax.swing.*;
import java.util.Scanner;

public class Ejercicio12 {
    public static void main(String[] args) {
        /*Scanner entrada = new Scanner(System.in);
        long factorial = 1;
        System.out.println("Digite un número");
        int numero = Integer.parseInt(entrada.nextLine());
        for (int i = 1; i < numero; i++) {
            factorial *= i;
        }

        System.out.println("\nEl factorial del número ingresado es: " + factorial);Scanner entrada = new Scanner(System.in);*/
        long factorial = 1;
        int numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un número"));
        for (int i = 1; i < numero; i++) {
            factorial *= i;
        }
        JOptionPane.showMessageDialog(null, "El factorial del número ingresado es: " + factorial);
    }
}
