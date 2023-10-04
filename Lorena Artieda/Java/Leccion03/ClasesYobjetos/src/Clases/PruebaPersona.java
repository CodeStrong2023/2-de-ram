package Clases;

public class PruebaPersona {
    public static void main(String[] args) {
        Persona persona1= new Persona();
        persona1.nombre="Juan";
        persona1.apellido="Perez";
        persona1.obtenerInformacion();

        Persona persona2= new Persona();
        persona2.nombre="Pedro";
        persona2.apellido="Garcia";
        persona2.obtenerInformacion();

    }
}
