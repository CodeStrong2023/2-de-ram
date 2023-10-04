//Ejercicio3: leer numeros hasta que se introduzca un cero
//para cada uno indicar si es par o impar
package clase3;

import java.util.Scanner;


public class Clase3 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int numero;
        System.out.println("Digite un numero: ");
        numero = Integer.parseInt(sc.nextLine());
        while(numero !=0){
            if(numero % 2 == 0){
                System.out.println("El numero ingresado " + numero + " es par");
            }
            else{
                System.out.println("El numero ingresado "+numero+ " es impar");
            }
            System.out.println("Digite otro numero");
            numero = Integer.parseInt(sc.nextLine());
        
        }
        System.out.println("El numero ingresado es " + numero + " finaliza el programa");
        
    }
    
}
