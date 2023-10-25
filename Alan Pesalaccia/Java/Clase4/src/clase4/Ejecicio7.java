//pedir numeros hasta que se introduzca uno negativo y calcular la media
package clase4;

import java.util.Scanner;


public class Ejecicio7 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int numero, conteo = 0, suma = 0;
        float promedio = 0;
        System.out.println("Digite un numero: ");
        numero = Integer.parseInt(sc.nextLine());
        while(numero >= 0){
            suma += numero;
            conteo++;
            System.out.println("Digite otro numero: ");
            numero = Integer.parseInt(sc.nextLine());
        }
        if(conteo ==0){
            System.out.println("Error, Ladivision entre cero no existe");
        }
        else{
            promedio = (float)suma/conteo;
            System.out.println("El promedio es: " + promedio);
        }
    }

}
