// pedir numeros hasta que se teclee uno negativo y mostrar cuantos se han introducidos

package clase3;

import javax.swing.JOptionPane;


public class Ejercicio4OptionPane {
    public static void main(String[] args) {
        int num, cont = 0;
        num = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero: "));
        while(num >= 0){
            JOptionPane.showMessageDialog(null, "El numero "+num + " es positivo");
            cont++;
            num = Integer.parseInt(JOptionPane.showInputDialog("Digite otro numero: "));
           
        }
        JOptionPane.showMessageDialog(null, "A ingresado " + cont + " numeros que no son negativos");
    }

}
