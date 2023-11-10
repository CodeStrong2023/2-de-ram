package Dominio;

public class Persona {
    //Atributos
    private int idPersona;
    private static int contadorPersona;
    private String nombre;
    //private double sueldo;
    //private boolean eliminado;

    //Constructor

    public Persona(String nombre) {
        this.nombre = nombre;
        //Incrementar el contador por cada objeto nuevo
        Persona.contadorPersona++;
        //Vamos a asignar un nuevo valor a la variable id persona
        this.idPersona= Persona.contadorPersona;
    }

    /*public Persona(String nombre) {
        this.nombre = nombre;
        //this.sueldo = sueldo;
        //this.eliminado = eliminado;
    }*/

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    /*public double getSueldo() {
        return sueldo;
    }

     */
    /*
    public void setSueldo(double sueldo) {
        this.sueldo = sueldo;
    }

    public boolean isEliminado() {
        return eliminado;
    }

    public void setEliminado(boolean eliminado) {
        this.eliminado = eliminado;
    }

    @Override
    public String toString() {
        return "Persona{" +
                "nombre='" + nombre + '\'' +
                ", sueldo=" + sueldo +
                ", eliminado=" + eliminado +
                '}';
        */

    public int getIdPersona() {
        return idPersona;
    }

    public void setIdPersona(int idPersona) {
        this.idPersona = idPersona;
    }

    public static int getContadorPersona() {
        return contadorPersona;
    }

    public static void setContadorPersona(int contadorPersona) {
        Persona.contadorPersona = contadorPersona;
    }

    @Override
    public String toString() {
        return "Persona{" +
                "idPersona=" + idPersona +
                ", nombre='" + nombre + '\'' +
                '}';
    }
}