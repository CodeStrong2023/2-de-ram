package clase08.encapsulamiento;

public class Persona2 {
    // Atributos
    private String nombre;
    private double sueldo;
    private boolean eliminado;

    public Persona2() {
        this.nombre = "Juan";
        this.sueldo = 20300;
        this.eliminado = false;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public double getSueldo() {
        return sueldo;
    }

    public void setSueldo(double sueldo) {
        this.sueldo = sueldo;
    }

    public boolean isEliminado() {
        return eliminado;
    }

    public void setEliminado(boolean eliminado) {
        this.eliminado = eliminado;
    }
}
