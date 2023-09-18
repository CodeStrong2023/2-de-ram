package ejercicios;

import javax.swing.*;
import java.util.Scanner;

// pedir dia, mes, año e indicar si esuna fecha correcta
public class ej09 {
  public static void main(String[] args) {

    Scanner entrada = new Scanner(System.in);
    System.out.println("Día: ");
    int dia1 = Integer.parseInt(entrada.nextLine());
    System.out.println("Mes: ");
    int mes1 = Integer.parseInt(entrada.nextLine());
    System.out.println("Año: ");
    int anio1 = Integer.parseInt(entrada.nextLine());

    if( (dia1 != 0) && (dia1 <= 30) ){

      if( (mes1 != 0) && (mes1 <= 12)){

        if ( (anio1 != 0) && (anio1 <= 2023)){
          System.out.println("La fecha ingresada es: " + dia1+"/"+ mes1+"/"+ anio1);
        } else {
          System.out.println("Fecha incorrecta, año incorrecto");
        }
      } else {
        System.out.println("Fecha incorrecta, mes incorrecto");
      }

    }else {
      System.out.println("Fecha incorrecta, día incorrecto");
    }


    int dia2 = Integer.parseInt(JOptionPane.showInputDialog("Ingrese el día: "));
    int mes2 = Integer.parseInt(JOptionPane.showInputDialog("Ingrese el mes: "));
    int anio2 = Integer.parseInt(JOptionPane.showInputDialog("Ingrese el año: "));

    if( (dia1 != 0) && (dia1 <= 30) ){

      if( (mes1 != 0) && (mes1 <= 12)){

        if ( (anio1 != 0) && (anio1 <= 2023)){
          JOptionPane.showMessageDialog(null,"La fecha ingresada es: " + dia2+"/"+ mes2+"/" + anio2);
        } else {
          JOptionPane.showMessageDialog(null,"Fecha incorrecta, año incorrecto");
        }
      } else {
        JOptionPane.showMessageDialog(null,"Fecha incorrecta, mes incorrecto");
      }

    }else {
      JOptionPane.showMessageDialog(null,"Fecha incorrecta, día incorrecto");
    }

  }
}
