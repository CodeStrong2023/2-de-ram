package clase07;

import javax.swing.*;

public class Ejercicio11 {
    public static void main(String[] args) {
        long producto = 1;

        for (int i = 1; i < 20; i+=2) {
            producto *= i;
        }

        JOptionPane.showMessageDialog(null, "El producto de los números impares es: " + producto);
    }
}
