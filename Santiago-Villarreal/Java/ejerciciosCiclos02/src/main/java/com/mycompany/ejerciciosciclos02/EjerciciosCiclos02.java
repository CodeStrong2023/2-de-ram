package com.mycompany.ejerciciosciclos02;

import java.util.Scanner;
import javax.swing.JOptionPane;

public class EjerciciosCiclos02 {
    public static void main(String[] args) {
        /*Leer un número e indicar si es positivo o negativo. El
        proceso se repetira hasta que se introduzca un cero 0*/
        /*Scanner entrada = new Scanner(System.in);
        int numero;
        System.out.println("Por favor, ingrese un número para indicar si es positivo o negativo >");
        numero = Integer.parseInt(entrada.nextLine());
        while(numero != 0){
            while(numero > 0){
            System.out.println("El número es positivo");
            System.out.println("ingrese otro número >");
            numero = Integer.parseInt(entrada.nextLine());
            }
            while(numero < 0){
            System.out.println("El número es negativo");
            System.out.println("ingrese otro número >");
            numero = Integer.parseInt(entrada.nextLine());
            }
        }
        System.out.println("El programa ha finalizado por ingresar '0'")*/
        
        Scanner entrada = new Scanner(System.in);
        int numero;
        numero = Integer.parseInt(JOptionPane.showInputDialog("Introduzca un número"));
        while(numero != 0){
            while(numero > 0){
            System.out.println("El número es positivo");
            System.out.println("ingrese otro número >");
            numero = Integer.parseInt(JOptionPane.showInputDialog("Introduzca un número"));
            }
            while(numero < 0){
            System.out.println("El número es negativo");
            System.out.println("ingrese otro número >");
            numero = Integer.parseInt(JOptionPane.showInputDialog("Introduzca un número"));
            }
        }
        System.out.println("El programa ha finalizado por ingresar '0'");
    }
}
