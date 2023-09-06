import javax.swing.*;

public class Ejercicio2 {
    public static void main(String[] args) {
        int numero;
        /*
        // Con scanner
        Scanner entry = new Scanner(System.in);
        System.out.println("Digite un número");
        numero = Integer.parseInt(entry.nextLine());
        while (numero != 0) {
            if (numero > 0) {
                System.out.println("El número " + numero + " es positivo");
            } else if (numero < 0) {
                System.out.println("El número " + numero + " es negativo");
            }
            System.out.println("Digite otro número");
            numero = Integer.parseInt(entry.nextLine());
        }

        System.out.println("Fin de la aplicación introdujo un 0");

         */

        // Con JOptionpane

        numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un número: "));
        while (numero != 0) {
            if (numero > 0) {
                System.out.println("El número " + numero + " es positivo");
            } else if (numero < 0) {
                System.out.println("El número " + numero + " es negativo");
            }
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite otro número: "));
        }

        System.out.println("Fin de la aplicación introdujo un 0");
    }
}
