/*
Ejercicio 4: Pedir números hasta que se teclee uno negativo
y mostrar cuantos números se han introducido.
1 Scanner
2 JOptionPane
*/
package ciclos03;

import java.util.Scanner;
import javax.swing.JOptionPane;

public class ejercicio4 {
    public static void main(String[] args) {
        /*
        Scanner entrada = new Scanner(System.in);
        System.out.println("Introduzca un numero por favor >");
        int numero = Integer.parseInt(entrada.nextLine());
        int contador = 0;
        while(numero >= 0){
            if(numero > 0){
                System.out.println("El número introducido es " + numero + ": positivo");
            } else {
                System.out.println("El número introducido es " + numero + ": neutro");
            }
            System.out.println("Introduzca otro número >");
            numero = Integer.parseInt(entrada.nextLine());
            contador++;
        }
        if(numero < 0){
            contador++;
        }
        System.out.println("Programa finalizado al introducir un número negativo");
        System.out.println("La cantidad de número(s) introducido(s) es " + contador);*/
        
        int numero = Integer.parseInt(JOptionPane.showInputDialog("Introduzca un número"));
        int contador = 0;
        while(numero >= 0){
            if(numero > 0){
                System.out.println("El número introducido es " + numero + ": positivo");
            } else {
                System.out.println("El número introducido es " + numero + ": neutro");
            }
            System.out.println("Introduzca otro número >");
            numero = Integer.parseInt(JOptionPane.showInputDialog("Introduzca otro numero"));
            contador++;
        }
        if(numero < 0){
            contador++;
        }
        System.out.println("Programa finalizado al introducir un número negativo");
        System.out.println("La cantidad de número(s) introducido(s) es " + contador);
    }
    
}
