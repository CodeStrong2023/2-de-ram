/*
Ejercicio 12: Pedir un número y calcular su factorial
Hacerlo con las dos clases, Scanner y JOptionPane
*/
package ejercicioC12;
//import java.util.Scanner;

import javax.swing.JOptionPane;



public class EjercicioC12 {
    public static void main(String[] args) {
        long factorial = 1;
        int numero = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un número"));
        for(int i=1; i<=numero;i++){
            factorial *= i;
        }
        //System.out.println("El factorial del número ingresado es: " + factorial);
        JOptionPane.showMessageDialog(null,"El factorial del número ingresado es " + factorial);
    }
}
