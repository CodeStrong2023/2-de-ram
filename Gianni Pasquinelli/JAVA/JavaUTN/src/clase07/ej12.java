package clase07;

import javax.swing.*;
import java.util.Scanner;

// calcular el factorial de un numero
public class ej12 {
  public static void main(String[] args) {
    long factorial = 1;
    //Scanner entrada = new Scanner(System.in);
    //System.out.println("Ingrese un número: ");
    int numero = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un numero"));
    for (int i = 1; i <= numero; i ++){
      factorial *= i;
    }
    //System.out.println("factorial = " + factorial);
    JOptionPane.showMessageDialog(null, "el factorial es: " + factorial);
  }
}
