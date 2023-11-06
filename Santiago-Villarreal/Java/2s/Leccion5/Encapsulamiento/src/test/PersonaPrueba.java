
package test;

import Dominio.Persona;

public class PersonaPrueba {
    public static void main(String[] args) {
        Persona persona1 = new Persona("Osvaldo",57.000,false);
        System.out.println("persona1: " + persona1.toString());
        System.out.println("persona1 su nombre es: " + persona1.getNombre());
        //modificar a travez del método
        persona1.setNombre("Juan Ignacio");
        //para acceder a los atributos privados
        System.out.println("persona1 con su nombre modificado: " + persona1.getNombre());
        System.out.println("persona1 el resultado para el sueldo: " + persona1.getSueldo());
        System.out.println("persona1 para obtener el booleano: " + persona1.isEliminado());
        
        System.out.println("persona1: " + persona1.toString());
        
    }
}
