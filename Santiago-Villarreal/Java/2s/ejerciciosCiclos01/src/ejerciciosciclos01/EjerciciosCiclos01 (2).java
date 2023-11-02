package ejerciciosciclos01;

import java.util.Scanner;
import javax.swing.JOptionPane;

public class EjerciciosCiclos01 {
    public static void main(String[] args) {
        /* Leer un número y devolver su cuadrado, repetir hasta que 
        se instroduzca un número negativo
        */
        /*Scanner entrada = new Scanner(System.in);
        int numero, potencia;
        System.out.println("Por favor introduzca un número para obtener su cuadrado >");
        numero = Integer.parseInt(entrada.nextLine());
        while(numero >= 0){
            potencia = (int)Math.pow(numero,2);
            System.out.println("La potencia del número es " + potencia);
            System.out.println("ingrese otro número >");
            numero = Integer.parseInt(entrada.nextLine());
        }
        System.out.println("El programa ha finalizado por introducir un número negativo");*/
        
        int numero, potencia;
        numero = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un nùmero"));
        while(numero >= 0){
            potencia = (int)Math.pow(numero,2);
            System.out.println("La potencia del número es " + potencia);
            numero = Integer.parseInt(JOptionPane.showInputDialog("Ingrese otro número"));
        }
        System.out.println("El programa ha finalizado por introducir un número negativo");
    }
    
}
