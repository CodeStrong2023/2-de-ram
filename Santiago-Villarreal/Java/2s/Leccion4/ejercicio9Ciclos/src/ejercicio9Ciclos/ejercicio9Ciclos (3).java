/*
ejercicio 9: pedir el día, mes y año de una fecha e indicar si la fecha es correcta.
Suponiendo que todos los meses son de 30 días
*/
package ejercicio9Ciclos;

import java.util.Scanner;
import javax.swing.JOptionPane;

public class ejercicio9Ciclos {
    public static void main(String[] args) {
        int dia, mes, any;
        /*
        Scanner entrada = new Scanner(System.in);
        System.out.println("Ingrese el día");
        dia = Integer.parseInt(entrada.nextLine());
        System.out.println("Ingrese el mes");
        mes = Integer.parseInt(entrada.nextLine());
        System.out.println("Ingrese el año");
        any = Integer.parseInt(entrada.nextLine());
        if((dia != 0 )&&(dia <= 30)){
            if((mes != 0)&&(mes<=12)){
                if((any != 0)&&(any <= 2022)){
                    System.out.println("La fecha ingresada es: " + dia + "/" + mes + "/" + any);
                } else {
                    System.out.println("Fecha incorrecta: año mal ingresado");
                }
            } else {
                System.out.println("Fecha incorrecta: mes mal ingresado");
            }
        } else {
            System.out.println("Fecha incorrecta: día mal ingresado");
        }
        */
        dia = Integer.parseInt(JOptionPane.showInputDialog("Ingrese el día"));
        mes = Integer.parseInt(JOptionPane.showInputDialog("Ingrese el mes"));
        any = Integer.parseInt(JOptionPane.showInputDialog("Ingrese el año"));
        if((dia != 0 )&&(dia <= 30)){
            if((mes != 0)&&(mes<=12)){
                if((any != 0)&&(any <= 2022)){
                    System.out.println("La fecha ingresada es: " + dia + "/" + mes + "/" + any);
                } else {
                    System.out.println("Fecha incorrecta: año mal ingresado");
                }
            } else {
                System.out.println("Fecha incorrecta: mes mal ingresado");
            }
        } else {
            System.out.println("Fecha incorrecta: día mal ingresado");
        }
    }
}
