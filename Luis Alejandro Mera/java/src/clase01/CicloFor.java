package clase01;

public class CicloFor {
    public static void main(String[] args) {
        // Ciclo for

        for (var i = 0; i < 10; i++) {
            System.out.println("i = " + i);
        }

        for (var i = 0; i < 10; i++) {
            if (i % 2 == 0) {
                System.out.println("Par");
                System.out.println("i = " + i);
                break; // Cunado se cumpla la condición que corte el ciclo
            }
        }

        for (var i = 0; i < 10; i++) {
            if (i % 2 != 0) {
                continue; // cuando se cumpla la condicion que siga con el ciclo lo salta
            }
            System.out.println("numero par = " + i);
        }

        // Etiquetas Labels (no es buna práctica usar)

        inicio:

        for (var i = 0; i < 10; i++) {
            if (i % 2 == 0) {
                System.out.println("Par");
                System.out.println("i = " + i);
                break inicio; // inidica que vuelva al punto de la etiqueta
            }
        }
    }
}
