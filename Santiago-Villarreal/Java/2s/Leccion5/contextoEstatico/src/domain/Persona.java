
package domain;

public class Persona {
    
    //ATRIBUTOS
    private int idPersona;
    private static int ContadorPersona;
    private String nombre;
    
    //CONSTRUCTOR
    public Persona(String nombre){
        this.nombre = nombre;
        //Incrementar el contador por cada objeto nuevo
        Persona.ContadorPersona++;
        // Asignar un nuevo valor a la variable idPersona
        this.idPersona = Persona.ContadorPersona;
        
    }
    
    public static int getContadorPersona() {
        return ContadorPersona;
    }

    public static void setContadorPersona(int aContadorPersona) {
        ContadorPersona = aContadorPersona;
    }
    public int getIdPersona() {
        return this.idPersona;
    }

    public void setIdPersona(int idPersona) {
        this.idPersona = idPersona;
    }

    public String getNombre() {
        return this.nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    @Override
    public String toString() {
        return "Persona{" + "idPersona=" + idPersona + ", nombre=" + nombre + '}';
    }
    
    
    
}
