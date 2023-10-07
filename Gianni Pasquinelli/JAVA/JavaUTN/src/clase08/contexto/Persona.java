package clase08.contexto;

public class Persona {
  private int idPersona;
  private static int contadorPersona;
  private String nombre;

  public Persona(String nombre) {
    this.nombre = nombre;
  Persona.contadorPersona++;
  this.idPersona = Persona.contadorPersona;
  }

  public static int getContadorPersona() {
    return contadorPersona;
  }

  public static void setContadorPersona(int contadorPersona) {
    Persona.contadorPersona = contadorPersona;
  }

  public int getIdPersona() {
    return idPersona;
  }

  public void setIdPersona(int idPersona) {
    this.idPersona = idPersona;
  }

  public String getNombre() {
    return nombre;
  }

  public void setNombre(String nombre) {
    this.nombre = nombre;
  }

}
