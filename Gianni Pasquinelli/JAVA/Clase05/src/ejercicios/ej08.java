package ejercicios;

import javax.swing.*;
import java.util.Scanner;

// pedir un num y mostrar del 1 a n
public class ej08 {
  public static void main(String[] args) {
    Scanner entrada = new Scanner(System.in);
    System.out.println("Ingrese un numero: ");
    int numero = Integer.parseInt(entrada.nextLine());
    int i = 1;
    while (i <= numero){
      System.out.println(i);
      i++;
    }

    int numero2 = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un numero: "));
    int j = 1;
    while(j <= numero2){
      JOptionPane.showMessageDialog(null, j);
      j++;
    }


  }
}
