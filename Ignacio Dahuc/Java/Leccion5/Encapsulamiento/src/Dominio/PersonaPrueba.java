package Dominio;

public class PersonaPrueba {
    public static void main(String[] args) {
        Persona persona1 = new Persona("Osvaldo"); //57.000, false);
        System.out.println("Persona1 su nombre es: "+ persona1.getNombre());
        //Modificar a traves de los metodos
        persona1.setNombre("Juan Ignacio");
        //persona1.nombre= "Juan Ignacio"; //Ya no se puede utilizar
        //System.out.println("Nombre es: "+ persona1.nombre)//Error
        System.out.println("persona1 con su nombre modificado: "+ persona1.getNombre());
        //System.out.println("person1 el resultado para el sueldo: "+ persona1.getSueldo());
        //System.out.println("persona1 para obtener el booleano: "+ persona1.isEliminado());

        //Tarea: crear otro objeto de tipo Persona, asignar valores de manera inicial
        //y imprimir luego modificar sus valores y volver a imprimir

        //Persona persona2 = new Persona("Marcos", 198.000, false);
        //System.out.println("Persona2 su nombre es: "+ persona2.getNombre());
        //persona2.setNombre("Pedro");

        //System.out.println("persona2 con su nombre modificado: "+ persona2.getNombre());
        //System.out.println("persona2 el resultado para el sueldo: "+ persona2.getSueldo());
        //System.out.println("persona2 para obtener el booleano: "+ persona2.isEliminado());

    }
}