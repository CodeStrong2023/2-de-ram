package clase06.ejercicios.proyectocaja;

public class PruebaCaja {

    public static void main(String[] args) {
        Caja caja1 = new Caja(); // Constructor 1
        caja1.ancho = 10;
        caja1.alto = 40;
        caja1.profundidad = 20;
        caja1.calcularVolumen();

        Caja caja2 = new Caja(10, 40, 20); // Constructor 2
        caja2.calcularVolumen();
    }
}
