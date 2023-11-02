//Ejercicio 7: pedir numeros hasta que se introduzca un negativo y calcular la media

import java.util.Scanner;

public class Ejercicio07 {

    public static void main(String[] args) {
        int numero = 0;
        int sumatoria=0;
        float promedio = 0;
        int contador=0;


        Scanner entrada= new Scanner(System.in);
        System.out.println("Introduzca un numero: ");
        numero= entrada.nextInt();

        while(numero>=0){

                sumatoria+=numero;
                contador++;
                System.out.println("Introduzca otro numero: ");
                numero= entrada.nextInt();
        }


        promedio= sumatoria/contador;
        System.out.println("El promedio de numero ingresados es: "+ promedio);
    }

}
