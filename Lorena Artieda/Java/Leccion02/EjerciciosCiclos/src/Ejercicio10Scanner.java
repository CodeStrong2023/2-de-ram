import java.util.Scanner;

public class Ejercicio10Scanner {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int cantidadNumeros = 10;
        double suma = 0;

        for (int i = 0; i < cantidadNumeros; i++) {
            System.out.print("Ingrese el número " + (i + 1) + ": ");

            while (!entrada.hasNextDouble()) {
                System.out.println("Entrada no válida. Por favor, ingrese un número válido.");
                entrada.next(); // Descarta la entrada no válida.
                System.out.print("Ingrese el número " + (i + 1) + ": ");
            }

            double numero = entrada.nextDouble();
            suma += numero;
        }

        entrada.close(); // Cierra el scanner cuando ya no es necesario.

        System.out.println("La suma de los números ingresados es: " + suma);
    }
}
