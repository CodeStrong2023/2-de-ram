package ejercicio5;

import java.util.Scanner;

public class Ejercicio5 {
    public static void main(String[] args) {
        //Hacer un programa que calcule e imprima tres calificaciones
        //Pedir las calificaciones al usuario
        Scanner entrada = new Scanner(System.in);
        float nota1,nota2,nota3,suma,resultado;
        System.out.println("Ingrese sus 3 calificaciones");
        nota1 = Float.parseFloat(entrada.nextLine());
        nota2 = Float.parseFloat(entrada.nextLine());
        nota3 = Float.parseFloat(entrada.nextLine());
        suma = nota1+nota2+nota3;
        System.out.println("El resultado de la suma de sus calificaciones es " + suma);
        resultado = suma/3;
        System.out.println("El promedio de sus calificaciones es " + resultado);
        
        
    }
    
}
