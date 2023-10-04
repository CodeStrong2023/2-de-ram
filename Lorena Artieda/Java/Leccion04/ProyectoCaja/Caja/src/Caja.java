public class Caja {
    double ancho;
    double alto;
    double profundidad;

    public Caja() {
    }

    public Caja(double ancho, double alto, double profundidad) {
        this.ancho = ancho;
        this.alto = alto;
        this.profundidad = profundidad;
    }

    public double mostrarVolumen(){
        return ancho * alto * profundidad;
    }
}
