package clase08.contexto.test;

import clase08.contexto.Persona;

public class PersonaPrueba {
  private int contador;

  public static void main(String[] args) {
    Persona persona1 = new Persona("Astor");
    System.out.println("persona1 = " + persona1);
    Persona persona2 = new Persona("Milan");
    System.out.println("persona2 = " + persona2);
    imprimir(persona1);
    imprimir(persona2);

    PersonaPrueba personaP1 = new PersonaPrueba();
    System.out.println("personaP1 = " + personaP1.getContador());
  }
  
  public static void imprimir(Persona persona) {
    System.out.println("persona = " + persona);
  }
  public int getContador(){
    imprimir(new Persona("fdggf"));
    return this.contador;
  }
}
