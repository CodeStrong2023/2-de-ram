import java.util.Scanner;

/*
Ejercicio 3: leer numeros hasta que se introduzca
un cero para cada uno indicar si es par o impar.
Primero lo haremos con la clase Scanner
luego con la clase JOPtionPane
 */
public class Ejercicio03 {
    public static void main(String[] args) {
        //Clase Scanner
        Scanner entrada= new Scanner(System.in);


        int numero=1;

        while(numero != 0){
            System.out.println("Digite un numero: ");
            numero= Integer.parseInt(entrada.nextLine());
            if(numero%2 ==0){
                System.out.println("El numero "+ numero +" es par");

            }
            else if(numero%2 !=0){
                System.out.println("El numero: "+ numero+" es impar");

            }
            System.out.println("El numero: "+ numero+" finaliza el programa");
        //Clase JOPtionPane

            
        }
    }
}
