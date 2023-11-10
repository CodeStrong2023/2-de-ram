package domain;

public class Persona {
    //atributos
    protected String nombre;
    protected char genero;
    protected int edad;
    protected String dirreccion;

    //Constructor
    public Persona(){

    }

    public Persona(String nombre){
        this.nombre = nombre;
    }

    public Persona(String nombre, char genero, int edad, String dirreccion) {
        this.nombre = nombre;
        this.genero = genero;
        this.edad = edad;
        this.dirreccion = dirreccion;
    }

    public String getDirreccion() {
        return this.dirreccion;
    }

    public void setDirreccion(String dirreccion) {
        this.dirreccion = dirreccion;
    }

    public String getNombre() {
        return this.nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public char getGenero() {
        return this.genero;
    }

    public void setGenero(char genero) {
        this.genero = genero;
    }

    public int getEdad() {
        return this.edad;
    }

    public void setEdad(int edad) {
        this.edad = edad;
    }

    @Override
    public String toString() {
        return "Persona{" + "nombre=" + nombre + ", genero=" + genero + ", edad=" + edad + ", dirreccion=" + dirreccion + '}';
    }

}