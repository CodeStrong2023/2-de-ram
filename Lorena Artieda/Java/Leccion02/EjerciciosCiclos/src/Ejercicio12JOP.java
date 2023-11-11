import javax.swing.*;

/*
Ejercicio 12: pedir un numero y calcular su factorial
 */
public class Ejercicio12JOP {
    public static void main(String[] args) {
        String entrada = JOptionPane.showInputDialog("Ingrese un número para calcular su factorial:");

        try {
            int numero = Integer.parseInt(entrada);

            if (numero < 0) {
                JOptionPane.showMessageDialog(null, "El factorial de un número negativo no está definido.");
            } else {
                long factorial = calcularFactorial(numero);
                JOptionPane.showMessageDialog(null, "El factorial de " + numero + " es: " + factorial);
            }
        } catch (NumberFormatException e) {
            JOptionPane.showMessageDialog(null, "Entrada no válida. Por favor, ingrese un número entero válido.");
        }
    }

    public static long calcularFactorial(int n) {
        if (n == 0 || n == 1) {
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
