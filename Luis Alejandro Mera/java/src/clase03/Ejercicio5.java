package clase03;

import javax.swing.*;
import java.util.Random;
import java.util.Scanner;

public class Ejercicio5 {
    public static void main(String[] args) {
        Random random = new Random();
        // Calculamos un número aleatorio del 0 al 100
        int randomNumber = random.nextInt(101);
        int number;
        int attempts = 0;

        // Con clase scanner
        /*
        System.out.println("Ingrese un número para adivinar");
        Scanner entry = new Scanner(System.in);
        number = Integer.parseInt(entry.nextLine());

        while (number != randomNumber) {
            if(number > randomNumber) {
                System.out.println("El número ingresado es mayor");
            } else {
                System.out.println("El número ingresado es menor");
            }
            attempts++;
            System.out.println("Ingrese otro número para adivinar");
            number = Integer.parseInt(entry.nextLine());
        }
        */

        // Con JOptionPane

        number = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un número para adivinar"));

        while (number != randomNumber) {
            if(number > randomNumber) {
                System.out.println("El número ingresado es mayor");
            } else {
                System.out.println("El número ingresado es menor");
            }
            attempts++;
            number = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un número para adivinar"));
        }
        System.out.println("Felicidades adivinates el número en " + attempts + " intentos");
    }
}
