package clase07;

public class Persona {
  public static void main(String[] args) {
  String nombre;
  String apellido;
  Persona(String nombre, String apellido){
    super();
    //Imprimir imprimir = new Imprimir();
    new Imprimir().imprimir(this);
    this.nombre = nombre;
    this.apellido = apellido;
    System.out.println("this = " + this);
  }

  Persona persona = new Persona("Gianni", "Pasquinelli");

}
class Imprimir {
  public Imprimir() {
    super();
  }

  public void imprimir(Persona persona) {
    System.out.println("persona = " + persona);
    System.out.println("this = " + this);
  }
}
}
