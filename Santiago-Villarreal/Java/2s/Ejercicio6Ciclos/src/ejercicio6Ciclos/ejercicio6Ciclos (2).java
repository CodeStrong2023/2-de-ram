/*
Ejercicio 6: Pedir numeros hasta que se teclee un 0, mostrar la suma de todos los numeros introducidos
*/
package ejercicio6Ciclos;

import java.util.Scanner;
import javax.swing.JOptionPane;

public class ejercicio6Ciclos {
    public static void main(String[] args) {
        /*
      Scanner entrada = new Scanner(System.in);  
        int numero;
        int suma = 0;
        int contador = 0;
        do{
            if(contador == 0){
              System.out.println("Introduzca un número >"); 
              numero = Integer.parseInt(entrada.nextLine());
              suma = suma + numero;
              contador ++;
            } else {
                System.out.println("Introduzca un número nuevamente");
                numero = Integer.parseInt(entrada.nextLine());
                suma = suma + numero;
                contador ++;
            } 
        }while(numero != 0);
        System.out.println("Programa finalizado al introducir un '0'");
        System.out.println("Ingresó un total de " + contador + " números");
        System.out.println("La suma total de los números ingresados es " + suma);
        */
        int numero,suma = 0,contador = 0;
        do{
            if(contador == 0){
                numero = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un número"));
                System.out.println(numero);
                suma = suma + numero;
                contador++;
            } else {
                numero = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un número nuevamente"));
                System.out.println(numero);
                suma = suma + numero;
                contador++;
            }
        }while(numero != 0);
        System.out.println("Programa finalizado al introducir un '0'");
        System.out.println("Ingresó un total de " + contador + " números");
        System.out.println("La suma total de los números ingresados es " + suma);
    }

   
}
