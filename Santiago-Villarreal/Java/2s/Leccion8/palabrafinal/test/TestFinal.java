package clase10.palabrafinal.test;

import clase10.palabrafinal.domain.Persona;

/*
Uso de la palabra Final
Esta palabra tiene diferentes significados dependiendo donde se apliquen:
- variables: evita que cambie el valor que almacena la variable. Se suelen combinar con el modificador de acceso static
para convertir una variable en una constante, que no se pueda modificar su valor. Ej: Clase Math todos sus
atributos son static final, no podemos cambiar el valor de pi.
- métodos: evita que se modifique la definición o el comportamiento de un método dede una subclase hija.
- clase: evita que se creen clases hijas.
* */
public class TestFinal {

    public static void main(String[] args) {
        final int miDni = 2321312;
        System.out.println("miDni = " + miDni);
//        miDni = 3243332; No se puede modificar ya que fue convertida a constante con final
//        Persona.CONSTANTE_AQUI = 8; no se puede modificar por que tiene la palabra final

        final Persona persona1 = new Persona();
        persona1.setNombre("Juan");
        System.out.println("persona1 = " + persona1.getNombre());
        persona1.setNombre("Maria");
        System.out.println("persona1 = " + persona1.getNombre());
    }
}
