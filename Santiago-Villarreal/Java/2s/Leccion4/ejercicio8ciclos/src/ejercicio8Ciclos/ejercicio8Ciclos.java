/*
Ejercicio 9: Pedir un número N, y mostrar todos los números del 1 al N
*/

package ejercicio8Ciclos;

import java.util.Scanner;
import javax.swing.JOptionPane;

public class ejercicio8Ciclos {
    public static void main(String[] args) {
        int i,numN;
        /*
        Scanner entrada = new Scanner(System.in);
        System.out.println("Ingrese un número para mostrar todos los números que lo componen");
        numN = Integer.parseInt(entrada.nextLine());
        i=1;
        System.out.println("Todos los números desde el 1 al " + numN + ":");
        while(i<=numN){
            System.out.println(i);
            i++;
        }
        */
        numN = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un número para mostrar todos los números que lo componen"));
        i=1;
        System.out.println("Todos los números desde el 1 al " + numN + ":");
        while(i<=numN){
            if(i == numN){
                System.out.print(numN + ".");
            } else {
                System.out.print(i + ", ");
            }
            i++;
        }
        System.out.println(" ");
    }
}
