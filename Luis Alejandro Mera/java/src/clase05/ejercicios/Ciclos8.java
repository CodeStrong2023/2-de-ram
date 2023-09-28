package clase05.ejercicios;

import java.util.Scanner;

import javax.swing.JOptionPane;

public class Ciclos8 {
    public static void main(String[] args) {
        // Scanner entry = new Scanner(System.in);
        // System.out.println("Digite un numero");
        // int number = Integer.parseInt(entry.nextLine());

        // for(int i = 1; i <= number; i++ ) {
        //   System.out.println(i);
        // }

        int number = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero"));

        for(int i = 1; i <= number; i++ ) {
            System.out.println(i);
        }
    }
}
