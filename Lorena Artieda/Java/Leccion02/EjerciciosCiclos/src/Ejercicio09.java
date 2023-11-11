import java.util.Scanner;

/*Ejercicio 9: Pedir el dia, mes y año de una fecha e
indicar si la fecha es correcta.Suponinedo que todos los
meses son de 30 dias
 */
public class Ejercicio09 {
    public static void main(String[] args) {
    Scanner input = new Scanner(System.in);

        System.out.println("Ingrese el día: ");
    int dia = input.nextInt();

        System.out.println("Ingrese el mes: ");
    int mes = input.nextInt();

        System.out.println("Ingrese el año: ");
    int año = input.nextInt();

        if (esFechaValida(dia, mes, año)) {
        System.out.println("La fecha ingresada es válida.");
    } else {
        System.out.println("La fecha ingresada no es válida.");
    }
}

    public static boolean esFechaValida(int dia, int mes, int año) {
        if (mes < 1 || mes > 12) {
            return false;
        }

        if (dia < 1 || dia > 30) {
            return false;
        }

        return true;
    }
}
