import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

/*
Ejercicio 8: pedir un numero N y mostrar todos los
numeros del 1 al N.
 */
public class Ciclos08 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        System.out.print("Por favor ingrese un numero: ");
        int numero = entrada.nextInt();
        for(int i=1; i<=numero;i++){
            System.out.print(i+" ");
        }
    }
}
