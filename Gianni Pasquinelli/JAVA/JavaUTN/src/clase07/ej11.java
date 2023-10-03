package clase07;

import javax.swing.*;

// mostrar el producto de los primeros 10 numeros pares
public class ej11 {
  public static void main(String[] args) {
    long producto = 1;
    for (int i = 1; i <= 20; i+=2){
      producto *= i;
    }
    JOptionPane.showMessageDialog(null, "el producto de los pares es: " + producto);
  }

}
