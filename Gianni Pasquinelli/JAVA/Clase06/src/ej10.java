// ej10 pedir 10 numero y retornar la suma

import javax.swing.*;
import java.util.Scanner;

public class ej10 {
  public static void main(String[] args) {
  //scanner
    Scanner entrada = new Scanner(System.in);
    int num1;
    int suma1 = 0;
    for (int i = 1; i <= 10; i++){
      System.out.println("Ingrese un número");
      num1 = Integer.parseInt(entrada.nextLine());
      suma1 += num1;
    }
    System.out.println("la suma total es = " + suma1);

    int num2;
    int sum2 = 0;
    for (int i = 1; i <= 10; i++){
      num2 = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un numero: "));
      sum2 += num2;
    }
    JOptionPane.showMessageDialog(null,"la suma es =" + sum2);
  }
}
