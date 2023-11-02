//Ejercicio3: leer numeros hasta que se introduzca un cero
//para cada uno indicar si es par o impar

package clase3;

import javax.swing.JOptionPane;


public class Ejericio3OptionPane {
    public static void main(String[] args) {
        int numero;
        System.out.println("Digite un numero: ");
        numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero"));
        while(numero !=0){
            if(numero % 2 == 0){
                JOptionPane.showMessageDialog(null, "El numero ingresado " + numero + " es par");
            }
            else{
                JOptionPane.showMessageDialog(null, "El numero ingresado " + numero + " es impar");

            }
           numero = Integer.parseInt(JOptionPane.showInputDialog("Digite otro numero"));
        
        }
        JOptionPane.showMessageDialog(null, "El numero ingresado es " + numero + " finaliza el programa");
        
    }
 
}
