package clase.pkg3.variables;

import java.util.Scanner;

public class Clase3Variables {

    public static void main(String[] args) {
        var miVariableEntera = 10;
        var miVariableCadena = "Seguimos estudiando";
        System.out.println("miVariableEntera = " + miVariableEntera);
        System.out.println("miVariableCadena = " + miVariableCadena);
        var usuario = "Osvaldo";
        var titulo = "ingeniero";
        var union = titulo + " " + usuario;
        System.out.println("union = " + union);
        var a = 8;
        var b = 4;
        System.out.println(usuario + a + b);
        System.out.println(usuario + (a + b));
        var nombre = "Natalia";
        System.out.println("Nueva Linea: \n" + nombre);
        System.out.println("Tabulador: \t" + nombre);
        System.out.println("\t \t .:MENU:.");
        System.out.println("retroceso: \b" + nombre);
        System.out.println("comillas simples: \'" + nombre + "\'");
        System.out.println("comillas dobles : \"" + nombre + "\"");
        Scanner entrada = new Scanner(System.in);
        System.out.println("Digite su nombre");
        var usuario2 = entrada.nextLine();
        System.out.println("usuario2 = " + usuario2);
        System.out.println("Ingrese el título");
        var titulo2 = entrada.nextLine();
        System.out.println("Resultado: "+ titulo2 + " " + usuario2);
    }

}
