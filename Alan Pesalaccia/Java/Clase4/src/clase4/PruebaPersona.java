
package clase4;


public class PruebaPersona {
    public static void main(String[] args) {
        Persona persona1 = new Persona(); // llamamos al constructor
        persona1.nombre = "Ariel"; //El valor hexadecimal normalmente comienza con 0x
        persona1.apellido = "Betancud";
        persona1.obtenerInformacion();
        
        Persona persona2 = new Persona();
        System.out.println("persona2 = " + persona2);
        System.out.println("persona1 = " + persona1);
        persona2.obtenerInformacion();
        persona2.nombre = "Alan";
        persona2.apellido = "Pesalaccia";
        persona2.obtenerInformacion();
    }

}
