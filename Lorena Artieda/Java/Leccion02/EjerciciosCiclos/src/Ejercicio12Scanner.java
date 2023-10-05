import java.util.Scanner;

public class Ejercicio12Scanner {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Ingrese un número para calcular su factorial: ");
        int numero = scanner.nextInt();

        long factorial = calcularFactorial(numero);

        System.out.println("El factorial de " + numero + " es: " + factorial);

        scanner.close(); // Cierra el scanner cuando ya no es necesario.
    }

    public static long calcularFactorial(int n) {
        if (n < 0) {
            return -1; // Error: Factorial de número negativo no está definido.
        } else if (n == 0 || n == 1) {
            return 1; // El factorial de 0 y 1 es 1.
        } else {
            long resultado = 1;
            for (int i = 2; i <= n; i++) {
                resultado *= i;
            }
            return resultado;
        }
    }
}
