package Ejercicios;

import java.util.Scanner;

import javax.swing.JOptionPane;

public class Ciclos6 {

  public static void main(String[] args) {
    // Scanner entry = new Scanner(System.in);
    // int number;
    // int total = 0;

    // System.out.println("Digite un numero entero");
    // number = Integer.parseInt(entry.nextLine());

    // while (number != 0) {
    //   total = total + number;
    //   System.out.println("Digite otro numero entero");
    //   number = Integer.parseInt(entry.nextLine());
    // }

    // System.out.println("La suma total de los numeros ingresados es: " + total);
    
 
    int number;
    int total = 0;

    number = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero entero"));

    while (number != 0) {
      total = total + number;
      number = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero entero"));
    }

    System.out.println("La suma total de los numeros ingresados es: " + total);
  }
}
