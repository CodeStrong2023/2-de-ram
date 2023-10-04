//JOptionPane

import javax.swing.JOptionPane;

public class Ejercicio04Jopt {
    public static void main(String[] args) {
        int contador = 0;
        int input;

        JOptionPane.showMessageDialog(null, "Este programa cuenta cuántos números has introducido. Finaliza al colocar un numero negativo.");

        while (true) {
            input = Integer.parseInt(JOptionPane.showInputDialog("Introduce un número (o presiona 'Cancelar' para finalizar):"));

            if (input < 0 ) {
                break; // Salir del bucle si se presiona 'Cancelar' o se cierra la ventana de entrada
            }

            try {
                int numero = Integer.parseInt(String.valueOf(input));
                contador++;
            } catch (NumberFormatException e) {
                JOptionPane.showMessageDialog(null, "Entrada no válida. Por favor, introduce un número válido.");
            }
        }

        JOptionPane.showMessageDialog(null, "Se han introducido " + contador + " números.");
    }
}

