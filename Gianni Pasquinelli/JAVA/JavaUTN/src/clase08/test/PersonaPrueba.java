package clase08.test;
import clase07.dominio.Persona;

public class PersonaPrueba {
  public static void main(String[] args) {
  Persona persona1 = new Persona("Gianni", 50000, false);

  persona1.setNombre("Juan");
    System.out.println("persona1 = " + persona1.getNombre());
    System.out.println("persona1 = " + persona1.getSueldo());
    System.out.println("persona1= " + persona1.isEliminado());

    Persona persona2 = new Persona("Pablo", 20000, false);
    System.out.println("persona2 = " + persona2.getNombre());
  persona2.setSueldo(150000);
    System.out.println("persona2 = " + persona2.getSueldo());

    System.out.println("persona1 = " + persona1.toString());


  }
}
