package Ejercicios;

import java.util.Scanner;

import javax.swing.JOptionPane;

public class Ciclos09 {

  public static void main(String[] args) {
    // Scanner entry = new Scanner(System.in);
    // System.out.println("Ingrese el día");
    // int day = Integer.parseInt(entry.nextLine());
    // System.out.println("Ingrese el mes");
    // int month = Integer.parseInt(entry.nextLine());
    // System.out.println("Ingrese el año");
    // int year = Integer.parseInt(entry.nextLine());

    // if (day != 0 && day <= 30) {
    //   if (month != 0 && month <= 12) {
    //     if (year != 0 && year <= 2023) {
    //       System.out.println(
    //         "La fecha ingresada es: dia " + day + "/" + month + "/" + year
    //       );
    //     } else {
    //       System.out.println("Fecha incorrecta: Año incorrecto");
    //     }
    //   } else {
    //     System.out.println("Fecha incorrecta: Mes incorrecto");
    //   }
    // } else {
    //   System.out.println("Fecha incorrecta: día incorrecto");
    // }
    
   
    int day = Integer.parseInt(JOptionPane.showInputDialog("Ingrese el día"));
    int month = Integer.parseInt(JOptionPane.showInputDialog("Ingrese el mes"));
    int year = Integer.parseInt(JOptionPane.showInputDialog("Ingrese el año"));

    if (day != 0 && day <= 30) {
      if (month != 0 && month <= 12) {
        if (year != 0 && year <= 2023) {
          System.out.println(
            "La fecha ingresada es: dia " + day + "/" + month + "/" + year
          );
        } else {
          System.out.println("Fecha incorrecta: Año incorrecto");
        }
      } else {
        System.out.println("Fecha incorrecta: Mes incorrecto");
      }
    } else {
      System.out.println("Fecha incorrecta: día incorrecto");
    }
  }
}
