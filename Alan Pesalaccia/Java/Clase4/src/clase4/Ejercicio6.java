//pdir numeros hasta que se teclee un 0, mostrar la suma de todos los numeros introducidos
package clase4;

import java.util.Scanner;


public class Ejercicio6 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int numero, suma = 0;
        do{
            System.out.println("Digite un numero: ");
            numero = Integer.parseInt(sc.nextLine());
            suma+= numero;
        }while(numero != 0);
        System.out.println("La suma de todos los numeros ingresados es: " + suma);
        
    }

}
