

package testarreglos;


public class TestArreglosObject {
    
     public static void main(String[] args) {
        Persona personas[] = new Persona[2];
        personas[0] = new Persona("Juan");
        personas[1] = new Persona("Pepe");
        System.out.println("personas[0] = " + personas[0]);
        System.out.println("personas[1] = " + personas[1]);

        for (int i = 0; i < personas.length; i++) {
            System.out.println("personas " + i + " = " + personas[i]);
        }

        // Forma más corta de hacer los arreglos
        String frutas[] = {"Banana", "Pera", "Durazno"};
            for (int i = 0; i < frutas.length; i++) {
                System.out.println("frutas " + i + " = " + frutas[i]);
        }
    }
    

}
