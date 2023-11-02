import javax.swing.*;

/*
Ejercicio 11: diseñar un programa que nuyestre
el producto de los 10 primeros numero impares con JoptionPane
*/
public class Ejercicio11 {
    public static void main(String[] args) {
        int cantidadNumerosImpares = 10;
        long producto = 1; // Inicializamos el producto en 1.

        for (int i = 1; cantidadNumerosImpares > 0; i += 2) {
            producto *= i;
            cantidadNumerosImpares--;
        }

        JOptionPane.showMessageDialog(null, "El producto de los primeros 10 números impares es: " + producto);
    }
}
