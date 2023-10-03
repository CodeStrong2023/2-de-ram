
package clase6;

import java.util.Scanner;

public class Clase6 {
    public static void main(String[] args) {
        boolean varBool = true;
        System.out.println("varBool = " + varBool);
        if(varBool){
            System.out.println("La bandera es verde"); 
        }
        else{
            System.out.println("La bandera es roja");
        }
        var edad = 30;
        var adulto = edad >=18;
        if(adulto){
            System.out.println("Eres mayor de edad");
        }
        else{
            System.out.println("Eres menor de edad");
        }
        var edad2 = Integer.parseInt("20");
        System.out.println("edad2 = " + (edad2 + 1));
        var valorPI = Double.parseDouble("3.1416");
        System.out.println("valorPI = " + valorPI);
        
        var entrada = new Scanner(System.in);
        System.out.println("Ingrese su edad >");
        edad = Integer.parseInt(entrada.nextLine());
        System.out.println("edad = " + edad);
        
        var edadTexto = String.valueOf(10);
        System.out.println("edadTexto = " + edadTexto);
        var fraseChar = "programadores".charAt(12);
        System.out.println("fraseChar = " + fraseChar);
        
        System.out.println("Digite un caracter");
        fraseChar = entrada.nextLine().charAt(0);
        System.out.println("fraseChar = " + fraseChar);
    }
        
    
}
