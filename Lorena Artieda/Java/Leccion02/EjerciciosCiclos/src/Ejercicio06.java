
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

/*Ejercicio 6: pedir numeros hasta que se teclee un 0, mostrar la suma de todos los numeros;
*/
public class Ejercicio06 {
    public static void main(String[] args) {
        //Pedimos por teclado al usuario que ingrese numeros
        Scanner entrada= new Scanner(System.in);
        System.out.println("Por favor ingrese un numero: ");

        //INICIALIZACION DE VARIABLES
        int numero= Integer.parseInt(entrada.nextLine());
        int suma = 0;
        List<Integer> numeros=new ArrayList<Integer>();;

        //Creamos un ciclo while para pedir por teclado la sucesion de numeros hasta
        //que el usuario ingrese 0
        while(numero!= 0){
            numeros.add(numero);
            System.out.println("Ingrese otro numero: ");
            numero= Integer.parseInt(entrada.nextLine());
        }
        //A traves de un ciclo for each sumamos la lusta de numeros ingresados

        for( int i : numeros)
        {
            suma+=i;
        }


        System.out.println("Ha introducido un 0, fin del programa");
        System.out.println("La suma de los numeros introducidos es: "+ suma);
    }
}
