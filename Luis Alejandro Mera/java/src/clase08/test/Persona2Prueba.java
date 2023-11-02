package clase08.test;

import clase08.encapsulamiento.Persona2;

public class Persona2Prueba {
    public static void main(String[] args) {
        Persona2 persona = new Persona2();

        // Mostramos los datos iniciales
        System.out.println("---------- Datos originales --------------");
        System.out.println(persona.getNombre());
        System.out.println(persona.getSueldo());
        System.out.println(persona.isEliminado());

        // Modificamos los datos
        persona.setNombre("Jose");
        persona.setSueldo(44000);
        persona.setEliminado(true);

        // Mostramos los cambios
        System.out.println("---------- Datos cambiados --------------");
        System.out.println(persona.getNombre());
        System.out.println(persona.getSueldo());
        System.out.println(persona.isEliminado());
    }
}
