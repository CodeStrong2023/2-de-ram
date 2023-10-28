/*
Ejercicio 10: Pedir 10 numeros y escribir la suma total 
Hacerlo con la clase Scanner y JOptionPane
*/
package ejercicioC10;

import java.util.Scanner;
import javax.swing.JOptionPane;

public class ejercicioC10 {
    public static void main(String[] args) {
        /*Scanner entrada = new Scanner(System.in);
        int numero, suma = 0;
        for(int i=1; i<=10;i++){
            System.out.println("Ingrese un número >");
            numero = Integer.parseInt(entrada.nextLine());
            suma += numero;
        }
        System.out.println("suma = " + suma);*/
        int numero, suma = 0;
        for(int i=1; i<=10;i++){
            numero = Integer.parseInt(JOptionPane.showInputDialog("Ingrese 10 números (" + i +")"));
            suma += numero;
        }
        System.out.println("suma = " + suma);
    }
}
