package Ejercicios;

import java.util.Scanner;

import javax.swing.JOptionPane;

public class Ciclos7 {

  public static void main(String[] args) {
    // Scanner entry = new Scanner(System.in);
    // int number;
    // int total = 0;
    // int count = 0;

    // System.out.println("Digite un numero entero");
    // number = Integer.parseInt(entry.nextLine());

    // while (number != 0) {
    //   total = total + number;
    //   count++;
    //   System.out.println("Digite otro numero entero");
    //   number = Integer.parseInt(entry.nextLine());
    // }

    // int media = total / count;

    // System.out.println("La media de los numeros ingresados es: " + media);
    
    
    int number;
    int total = 0;
    int count = 0;

    number = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero entero"));

    while (number != 0) {
      total = total + number;
      count++;
      number = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero entero"));
    }

    int media = total / count;

    System.out.println("La media de los numeros ingresados es: " + media);
  }
}
