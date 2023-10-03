/*Ejercicio 5: Realizar un juego para adivinar un número, para ello generar un
numero aleatorio entra 0-100, y luego ir pidiendo numeros indicando si es mayor
o menor, segun sea mayor o menor con respecto a N.
El proceso termina cuando el usuario acierta y mostramos el números de intentos.
*/
package ciclos03;

import java.util.Scanner;
import javax.swing.JOptionPane;

public class ejercicio5 {
    public static void main(String[] args) {
        
        /*
        Scanner entrada = new Scanner(System.in);
        int numero, aleatorio, contador = 0;
        aleatorio = (int)(Math.random()*100);
        System.out.println("Introduzca un número");
        numero = Integer.parseInt(entrada.nextLine());
        contador++;
        if(numero != aleatorio){
            while(numero != aleatorio){
                if(numero > aleatorio){
                    System.out.println("Introduzca un número menor");
                    numero = Integer.parseInt(entrada.nextLine());
                } else if(numero < aleatorio){
                    System.out.println("Introduzca un número mayor");
                    numero = Integer.parseInt(entrada.nextLine());
                }
                contador++;
            }
        } else {
            System.out.println("Felicitaciones, ha acertado el número!");
        }
        System.out.println("Felicitaciones, ha acertado el número!");
        System.out.println("Ha acertado el número en " + contador +" intento(s)");*/
        
        int numero, numeroA, aleatorio, contador = 0;
        aleatorio = (int)(Math.random()*100);
        numero = Integer.parseInt(JOptionPane.showInputDialog("Introduzca un número"));
        contador++;
        if(numero != aleatorio){
            while(numero != aleatorio){
                numeroA = numero;
                if(numero > aleatorio){
                    numero = Integer.parseInt(JOptionPane.showInputDialog("Introduzca un número menor (" + numeroA + ")"));
                } else if(numero < aleatorio){
                    numero = Integer.parseInt(JOptionPane.showInputDialog("Introduzca un número mayor (" + numeroA + ")"));
                }
                contador++;
            }
        } else {
            System.out.println("Felicitaciones, ha acertado el número!");
        }
        System.out.println("Felicitaciones, ha acertado el número!");
        System.out.println("Ha acertado el número en " + contador +" intento(s)");
    }
}
