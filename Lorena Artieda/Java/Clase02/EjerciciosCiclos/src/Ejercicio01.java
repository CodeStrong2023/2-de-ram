import javax.swing.*;
import java.util.Scanner;
import javax.swing.JOptionPane;

public class Ejercicio01 {
    public static void main(String[] args) {

        //Scanner entrada= new Scanner(System.in);
        int numero, cuadrado;

        numero= Integer.parseInt(JOptionPane.showInputDialog("Digite un numero"));
        while (numero>=0){
            cuadrado=(int)Math.pow(numero, 2);
            System.out.println("El numero: "+ numero+ " elevado al cuadrado es: "+ cuadrado);
            System.out.println("Digite otro numero: ");
            numero= Integer.parseInt(JOptionPane.showInputDialog("Digite otro numero"));


        }
        System.out.println("El programa ha finalizado por numero negativo");
    }


}
