public class PruebaPersona {
  public static void main(String[] args) {
    Persona persona1;
    persona1 = new Persona(); //contructor de la clase persona
    persona1.nombre = "Gianni";
    persona1.apellido = "Pasquinelli";
    persona1.obtenerInformacion();

    Persona persona2 = new Persona();
    System.out.println("persona2 = " + persona2);
    System.out.println("persona1 = " + persona1);

    persona2.obtenerInformacion();
    persona2.nombre = "Belén";
    persona2.obtenerInformacion();
    persona2.apellido = "Cortese";
    persona2.obtenerInformacion();




  }
}
