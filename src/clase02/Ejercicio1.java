package clase02;

import javax.swing.*;
import java.util.Scanner;

public class Ejercicio1 {
    public static void main(String[] args) {
        int numero;
        int cuadrado;
        // Con clase Scanner
        Scanner entry = new Scanner(System.in);

        System.out.println("Digite un número");
        numero = Integer.parseInt(entry.nextLine());

        while (numero >= 0) {
            cuadrado = (int) Math.pow(numero, 2); // Método para sacar la potencia de un número
            System.out.println("El número " + numero + " elevado al cuadrado es " + cuadrado);
            System.out.println("Digite otro número");
            numero = Integer.parseInt(entry.nextLine());
        }
        System.out.println("Programa finalizado por número negativo");
//         Con JOptionPane
        numero = Integer.parseInt(JOptionPane.showInputDialog("Digitie un número: "));

        while (numero >= 0) {
            cuadrado = (int) Math.pow(numero, 2); // Método para sacar la potencia de un número
            System.out.println("El número " + numero + " elevado al cuadrado es " + cuadrado);
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digitie otro número: "));
        }
        System.out.println("Programa finalizado por número negativo");
    }
}
