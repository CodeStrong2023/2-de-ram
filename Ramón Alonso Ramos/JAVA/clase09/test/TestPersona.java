package clase09.test;

import clase09.domain.Persona;

public class TestPersona {
    public static void main(String[] args) {
        Persona persona1 = new Persona("Luis");
        System.out.println("persona1 = " + persona1);
        Persona persona2 = new Persona("Juan");
        System.out.println("persona2 = " + persona2);

        imprimir(persona1);
    }
    public static void imprimir(Persona persona) {
        System.out.println("persona = " + persona);
    }
}
