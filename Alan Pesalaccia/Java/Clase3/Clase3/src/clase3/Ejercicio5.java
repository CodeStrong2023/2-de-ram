//Realizar un juego para adivinar un numero, para ello generar un numero aleatoriio
//entre 0-100 y luego ir pidiendo numeros indicando " es mayor" o "es menor" segun
//sea mayor o menor con respecto a N, el proceso termina cuando el usuario acierta
package clase3;

import java.util.Scanner;


public class Ejercicio5 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int numero, aleatorio, conteo = 0;
        aleatorio = (int)(Math.random()*100); //ESto genera un numero aleatorio
        do{
            System.out.println("Digite un numero: ");
            numero = Integer.parseInt(sc.nextLine());
            if(numero < aleatorio){
                System.out.println("Digite un numero mayor");
            }
            else if(numero > aleatorio){
                System.out.println("Digite un numero menor");
            }
            else{
                System.out.println("Has adivinado el numero");
            
            }
            conteo ++;
        }while(numero != aleatorio);
        System.out.println("Adivinaste el numero en: " + conteo + " intentos");
        
    }

}
