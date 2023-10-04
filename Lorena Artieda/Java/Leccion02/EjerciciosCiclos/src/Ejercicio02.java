import javax.swing.*;

/*Ejercicio 2: leer un numero e indicar si es positivo o
negativo. L proceso se repetira hasta que se introduzca
un cero.

 */
public class Ejercicio02 {
    public static void main(String[] args) {

int numero= 1;
        while(numero !=0) {
            numero= Integer.parseInt(JOptionPane.showInputDialog("Digite un numero: "));
            if (numero > 0){
                System.out.println("El numero "+ numero+ " es positivo");
            }
            else if (numero <0){
                System.out.println("El numero "+ numero+" es negativo");
            }
            else {
                System.out.println("El numero es 0 fin del programa" );
            }



        }
    }
}
