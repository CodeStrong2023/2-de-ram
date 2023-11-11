
package clase2;

import javax.swing.JOptionPane;


public class Ejercicio02ConPane {
    public static void main(String[] args) {
        int num;
        num = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero"));
        while(num != 0){
            if(num > 0){
               System.out.println("El numero " + num +" es positivo");
            }
            else{
            System.out.println("El numero " + " es negativo");
            }
            System.out.println("Digite otro numero");
            num = Integer.parseInt(JOptionPane.showInputDialog("Digite otro numero"));

        }
        System.out.println("El numero " + num + " finaliza el programa");
    }

}
