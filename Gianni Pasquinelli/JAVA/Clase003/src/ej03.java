import javax.swing.*;

public class ej03 {
  public static void main(String[] args) {

    int numero;
    numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un número: "));
    while (numero != 0) {
      if(numero % 2 == 0) {
        JOptionPane.showMessageDialog(null, "El número ingresado " + numero + " es par.");
      }else {
        JOptionPane.showMessageDialog(null, "El número ingresado " + numero + " es impar.");
      }
      numero = Integer.parseInt(JOptionPane.showInputDialog("Digite otro número: "));
    }
    JOptionPane.showMessageDialog(null, "el 0 finaliza el programa");

  }
}
