/* Ejercicio 5: Realizar un juego para adivinar un numero,
para ello generar un numero aleatorio entre 0 y 100 y luego
ir pidiendo numeros indicando "es mayor" o "es menor" segun sea mayor o menor con respecto
a N. El proceso termina conado el usuario acierta mostramos el numero de intentos
 */
import java.util.Random;
import java.util.Scanner;

public class Ejercicio05 {
    public static void main(String[] args) {
        Random rand = new Random();
        int numeroAdivinar = rand.nextInt(101); // Genera un número aleatorio entre 0 y 100
        int intentos = 0;

        System.out.println("¡Bienvenido al juego de adivinar el número!");
        System.out.println("He generado un número entre 0 y 100. Adivina cuál es!?");

        Scanner scanner = new Scanner(System.in);

        while (true) {
            System.out.print("Ingresa un numero: ");
            int suposicion = scanner.nextInt();
            intentos++;

            if (suposicion < numeroAdivinar) {
                System.out.println("Es mayor. Intentalo otra vez");
            } else if (suposicion > numeroAdivinar) {
                System.out.println("Es menor. Intentalo otra vez");
            } else {
                System.out.println("¡Felicidades! Has adivinado el número en " + intentos + " intentos.");
                break;
            }
        }

        scanner.close();
    }
}

