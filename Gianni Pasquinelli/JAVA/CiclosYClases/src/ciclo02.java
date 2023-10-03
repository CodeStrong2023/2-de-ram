import javax.swing.*;

public class ciclo02 {
  public static void main(String[] args) {
    int numero, cuadrado;
    numero = Integer.parseInt(JOptionPane.showInputDialog("Escriba un número: "));
    while (numero >= 0){
      cuadrado = (int)Math.pow(numero, 2);
      System.out.println(numero + " al cuadrado da: " + cuadrado);
      System.out.println("Escriba un número");
      numero = Integer.parseInt(JOptionPane.showInputDialog("Escriba un número: "));
    }
    System.out.println("Terminado");
  }
}
