public class PruebaPersona {

  public static void main(String[] args) {
    Persona persona1 = new Persona();
    persona1.nombre = "Luis";
    persona1.apellido = "Mera";

    persona1.obtenerInformacion();
    //     Nombre: Luis
    //     Apellido: Mera

    Persona persona2 = new Persona();
    persona2.obtenerInformacion();
    persona2.nombre = "Juan";
    persona2.apellido = "Perez";
    persona2.obtenerInformacion();
  }
}
