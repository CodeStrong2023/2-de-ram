

public class TestObject {
  public static void main(String[] args) {
    Persona personas[] = new Persona[2];
    personas[0] = new Persona("Gianni");
    personas[1] = new Persona("Astor");
    System.out.println("personas[0] = " + personas[0]);
    System.out.println("personas[1] = " + personas[1]);

    for (int i = 0; i < personas.length; i++){
      System.out.println("personas " + personas[i]);
    }

    String frutas[] = {"Banana", "Pera", "Durazno"};
    for (int i = 0; i < frutas.length; i++){
      System.out.println("frutas[i] = " + frutas[i]);
    }

  }
}
