import javax.swing.*;

public class ej04 {
  public static void main(String[] args) {
    int numero, conteo = 0;
    numero = Integer.parseInt(JOptionPane.showInputDialog(null, "Ingrese un número"));
    while( numero >= 0) {
      JOptionPane.showMessageDialog(null,"El numero " + numero + " es positivo");
      conteo++;
      numero = Integer.parseInt(JOptionPane.showInputDialog(null, "Ingrese otro número"));
    }
    JOptionPane.showMessageDialog(null,"Ingreso " + conteo + " números positivos");

  }
}
