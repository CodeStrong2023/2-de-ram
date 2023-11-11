package ejercicio6;

import java.util.Scanner;

public class Ejercicio6 {
    public static void main(String[] args) {
        //Guillermo tiene  N dolares, Luis la mitad. Juan la mitad de ambos sumados
        Scanner entrada = new Scanner(System.in);
        float guillermo,luis,juan,suma;
        System.out.println("Ingrese la suma de dinero en dolares que posee Guillermo");
        guillermo = Float.parseFloat(entrada.nextLine());
        luis = guillermo / 2;
        juan = (guillermo + luis) / 2;
        suma = guillermo + juan + luis;
        System.out.println("La suma del dinero de Guillermo, Luis y Juan es de $" + suma);
        
    }
    
}
