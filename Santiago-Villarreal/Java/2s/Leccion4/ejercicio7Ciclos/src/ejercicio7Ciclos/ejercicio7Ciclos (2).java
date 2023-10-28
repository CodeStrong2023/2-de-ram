/*
Ejercicio 7: solicitar la entrada de numeros hasta que se introduzca uno negativo
sacar la media
*/
package ejercicio7Ciclos;

import java.util.Scanner;
import javax.swing.JOptionPane;

public class ejercicio7Ciclos {
    public static void main(String[] args) {
        /*
        int numero, contador = 0,suma = 0;
        float media;
        Scanner entrada = new Scanner(System.in);
        System.out.println("Por favor introduzca un número >");
        numero = Integer.parseInt(entrada.nextLine());
        contador++;
        suma = suma + numero;
        while(numero >= 0){
            System.out.println("Introduzca nuevamente un número >");
            numero = Integer.parseInt(entrada.nextLine());
            contador++;
            suma = suma + numero;
        }
        System.out.println("Programa finalizado por ingresar un número negativo");
        media = (float)suma / contador;
        System.out.println("La media de los números es " + media);
        */
        int numero, contador = 0,suma = 0;
        float media;
        numero = Integer.parseInt(JOptionPane.showInputDialog("Introduzca un número"));
        contador++;
        suma = suma + numero;
        System.out.println(numero);
        while(numero >= 0){
            numero = Integer.parseInt(JOptionPane.showInputDialog("Introduzca otro número"));
            suma = suma + numero;
            contador++;
            System.out.println(numero);
        }
        System.out.println("Programa finalizado por ingresar un número negativo");
        media = (float)suma / contador;
        System.out.println("La media de los números es " + media);
    }
}
