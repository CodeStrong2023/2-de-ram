package clase10.domain;

public class Empleado extends Persona { // Con extends indicamos que herdamos de una clase, solo se puede heredar de una sola clase
    private int idEmpleado;
    private double sueldo;
    private static int contadorEmpleados;

    public Empleado() {
        // Esto no es un ejemplo de constructor vacío como inidca el profesor en la clase, el this toma este constructor
        // por que no tiene parámetros, pero no es un caso de uso normal
        this.idEmpleado = ++Empleado.contadorEmpleados;
    }
    public Empleado(String nombre, double sueldo) {
//        super(nombre);
        this(); // LLamamos al constructor interno vacío
        this.sueldo = sueldo;
        this.nombre = nombre;
    }


    public int getIdEmpleado() {
        return this.idEmpleado;
    }

    public double getSueldo() {
        return this.sueldo;
    }
    public void setSueldo(double sueldo) {
        this.sueldo = sueldo;
    }

    @Override
    public String toString() {
        final StringBuilder sb = new StringBuilder("Empleado{");
        sb.append("idEmpleado=").append(idEmpleado);
        sb.append(", sueldo=").append(sueldo);
        sb.append('}');
        return sb.toString();
    }
}
