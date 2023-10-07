package clase08.test;

import clase08.encapsulamiento.Persona;

public class PersonaPrueba {
    public static void main(String[] args) {
        Persona persona1 = new Persona("Juan", 30000, false);
        System.out.println("El nombre es: "+persona1.getNombre());
        System.out.println("El sueldo es: "+persona1.getSueldo());
        System.out.println("Está eliminado?: "+persona1.isEliminado());

        // Modificamos a traves de los métodos
        persona1.setNombre("Pedro");
        persona1.setSueldo(20000);
        persona1.setEliminado(true);
        System.out.println("El nombre es: "+persona1.getNombre());
        System.out.println("El sueldo es: "+persona1.getSueldo());
        System.out.println("Está eliminado?: "+persona1.isEliminado());

        // Mostramos el método creado toString()
        System.out.println(persona1.toString());
    }
}
