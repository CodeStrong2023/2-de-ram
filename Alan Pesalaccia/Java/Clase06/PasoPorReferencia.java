package clase06;

import clase04.Persona;

public class PasoPorReferencia {

    public static void main(String[] args) {
        Persona persona1 = new Persona();
        persona1.nombre= "Jose";
        persona1.apellido = "Mattar";

        System.out.println("persona1 = " + persona1.nombre);

        cambiarValor(persona1);
        System.out.println("Nuevo valor");
        System.out.println("persona1 = " + persona1.nombre);

        persona1 = cambiarElValor(persona1);

        System.out.println("El nuevo nombre de persona1 es: " + persona1.nombre);

        // Persona persona2 = null;
        Persona persona2 = new Persona();
        persona2 = cambiarElValor(persona2);
        System.out.println("El nuevo nombre de persona2 es: " + persona2.nombre);
    }

    public static void cambiarValor(Persona persona) { // Paso por referencia
        persona.nombre = "Maria";
    }

    public static Persona cambiarElValor(Persona persona) {
        if (persona == null) {
            System.out.println("Persona es es null");
            return null;
        }
        persona.nombre = "Monica";

        return persona; // Retorna la persona modificada
    }
}