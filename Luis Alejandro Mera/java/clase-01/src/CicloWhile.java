public class CicloWhile {
    public static void main(String[] args) {
        var conteo = 0;

        // Ciclo while
        while (conteo < 7) {
            System.out.println("conteo = " + conteo);
            conteo++; // vamos aumentando en 1 la variable
        }

        // Ciclo do while

        var contador = 0;
        do {
            System.out.println("contador = " + contador);
            contador++;
        } while (contador < 7);
    }
}
