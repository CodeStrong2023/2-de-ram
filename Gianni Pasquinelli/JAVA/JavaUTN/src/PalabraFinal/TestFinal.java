package PalabraFinal;

public class TestFinal {
  public static void main(String[] args) {
    final int dni = 27879997;
    System.out.println("dni = " + dni);
    // dni = 27272727;

    final Persona persona1 = new Persona();
    persona1.setNombre("Gianni");
    System.out.println("persona1.getNombre() = " + persona1.getNombre());
    persona1.setNombre("Berretin");
    System.out.println("persona1.getNombre() = " + persona1.getNombre());

  }
}
