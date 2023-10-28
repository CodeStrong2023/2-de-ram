
package PasoPorReferencia;

import clases.Persona;

public class PasoPorReferencia {
    public static void main(String[] args) {
        Persona persona1 = new Persona();
        persona1.nombre = "Ester";
        System.out.println("persona1 nombre = " + persona1.nombre);
        cambiarValor(persona1);
        System.out.println("El cambio que hicimos en el nombre es: " + persona1.nombre);
        persona1 = cambiarElValor(persona1);
        System.out.println("persona1 = " + persona1.nombre);
        Persona persona2 = new Persona();
        //Persona persona2 = null;
        persona2 = cambiarElValor(persona2);
        System.out.println("persona2 = " + persona2.nombre);
    }
    
    public static void cambiarValor(Persona persona){
        persona.nombre = "Maria";
    }
    
    public static Persona cambiarElValor(Persona persona){
        if(persona == null){
            System.out.println("Valor de persona es invalido");
            return null;
        }else{
            persona.nombre = "Mónica";
            return persona;  
        }
    }
}
