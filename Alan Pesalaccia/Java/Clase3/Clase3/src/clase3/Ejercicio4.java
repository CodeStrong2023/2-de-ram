// pedir numeros hasta que se teclee uno negativo y mostrar cuantos se han introducidos
package clase3;

import java.util.Scanner;


public class Ejercicio4 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int num, cont = 0;
        System.out.println("Digite un numero: ");
        num = Integer.parseInt(sc.nextLine());
        while(num >= 0){
            System.out.println("El numero " + num + " es positivo");
            cont++;
            System.out.println("Digite otro numero: ");
            num = Integer.parseInt(sc.nextLine());
        }
        System.out.println("A ingresado "+ cont + " numeros que no son negativos");
        
    }

}
