import javax.swing.*;

public class ej06 {
  public static void main(String[] args) {
        int numero, suma = 0;
    do{

      numero = Integer.parseInt(JOptionPane.showInputDialog(null, "Digite un número"));
      suma += numero;
    }while( numero != 0);
        JOptionPane.showMessageDialog(null, "La suma de todos los numeros es:  " + suma);
  }
}
