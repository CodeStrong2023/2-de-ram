package ejercicio_1;

import java.util.Scanner;

public class Ejercicio_1 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        System.out.println("Ingrese el nombre del libro");
        String nombreLibro = entrada.nextLine();
        System.out.println("Ingrese ID del libro");
        int idLibro = Integer.parseInt(entrada.nextLine());
        System.out.println("Ingrese el precio del libro");
        double precioLibro = Double.parseDouble(entrada.nextLine());
        System.out.println("Confirme si el envío es gratuito (Ingrese 'true' o 'false')");
        boolean envioGratuito = Boolean.parseBoolean(entrada.nextLine());
        System.out.println(nombreLibro + " #"+idLibro);
        System.out.println("El precio del libro es $" + precioLibro);
        System.out.println("El envío es gratuito es " + envioGratuito);
    }
      
}
