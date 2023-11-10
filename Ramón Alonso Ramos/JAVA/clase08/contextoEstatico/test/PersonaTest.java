package clase08.contextoEstatico.test;

import clase08.contextoEstatico.domain.Persona;

public class PersonaTest {
    private int contador;

    public static void main(String[] args) {
        Persona persona1 = new Persona("Juan");
        System.out.println(persona1);
        Persona persona2 = new Persona("Pedro");
        System.out.println(persona2);
        imprimir(persona1);
        imprimir(persona2);

        PersonaTest personaTest1 = new PersonaTest();
        System.out.println("personaTest1 = " + personaTest1.getContador());

    }

    public static void imprimir(Persona persona) {
        System.out.println("persona = " + persona);
    }

    public int getContador() {
        imprimir(new Persona("Diana"));
        return this.contador;
    }
}
