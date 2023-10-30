/*
Ejercicio 11: Diseñar un programa que muestre el producto de los 10 primeros impares 
JOptionPane
*/
package ejercicioC11;

import javax.swing.JOptionPane;

public class EjercicioC11 {
    public static void main(String[] args) {
        long producto = 1;
        for(int i = 1; i<=20;i+=2){
            producto *= i;
        }
        JOptionPane.showMessageDialog(null,"El producto de los numeros impares es: " + producto);
        
    }
}
