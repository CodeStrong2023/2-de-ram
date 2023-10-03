
public class cicloWhile {
    public static void main(String[] args) {
        var conteo = 0; // inferencia de tipos
        while (conteo < 7) {
            System.out.println("conteo = " + conteo);
            conteo ++; // Vamos incrementando en uno la variable
        }
    }
}
