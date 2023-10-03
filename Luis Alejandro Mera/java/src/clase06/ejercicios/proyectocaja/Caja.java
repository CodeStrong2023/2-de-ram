package clase06.ejercicios.proyectocaja;

public class Caja {

    int ancho;
    int alto;
    int profundidad;

    public Caja() {}

    public Caja(int ancho, int alto, int profundidad) {
        this.ancho = ancho;
        this.alto = alto;
        this.profundidad = profundidad;
    }

    public void calcularVolumen() {
        int volumen = ancho * alto * profundidad;

        System.out.println("El volumen es: " + volumen);
    }
}
