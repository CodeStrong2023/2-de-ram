/*Ejercicio 3: Leer numeros hasta que se introduzca un cero
indicar si es par o impar. 
1 clase scanner
2 clase joption
*/
package ciclos03;

import java.util.Scanner;
import javax.swing.JOptionPane;

public class ciclos03 {
    public static void main(String[] args) {
        /* Scanner entrada = new Scanner(System.in);
        System.out.println("Introduzca un número por favor >");
        int numero = Integer.parseInt(entrada.nextLine());
        while(numero != 0){
            if(numero % 2 == 0){
                System.out.println("Es número par");
            } else {
                System.out.println("Es número impar");
            }
            System.out.println("Ingrese otro número");
            numero = Integer.parseInt(entrada.nextLine());
        }
        System.out.println("Programa finalizado al introducir un '0'");*/
        
        int numero; 
        numero = Integer.parseInt(JOptionPane.showInputDialog("Introduzca un número"));
        while(numero != 0){
            if(numero % 2 == 0){
                System.out.println("Es número " + numero + " es par");
            } else {
                System.out.println("Es número " + numero + " es impar");
            }
            numero = Integer.parseInt(JOptionPane.showInputDialog("Introduzca otro número"));
        }
        System.out.println("Programa finalizado al introducir un '0'");
    }
    
}
