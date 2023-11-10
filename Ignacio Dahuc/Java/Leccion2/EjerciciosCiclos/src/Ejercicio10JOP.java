import javax.swing.*;

/*
Ejercicio 10: pedir 10 numeros y escribir la suma total
Hacerlo con la clase Scanner y JoptionPane
*/
public class Ejercicio10JOP {
    public static void main(String[] args) {
        int cantidadNumeros = 10;
        double suma = 0;

        for (int i = 0; i < cantidadNumeros; i++) {
            String input = JOptionPane.showInputDialog("Ingrese el número " + (i + 1) + ":");
            double numero = Double.parseDouble(input);
            suma += numero;
        }


        JOptionPane.showMessageDialog(null, "La suma de los números ingresados es: " + suma);
    }
}