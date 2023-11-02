package clase10.palabrafinal.domain;

//final public class Persona { // Esta clase no la podemos heredar por el final
//}

public class Persona {
    public final  static int CONSTANTE_AQUI = 15;
    private String nombre;
//     final public void imprimir() { // Este método no se lo puede sobre escribir por la palabra final
//        System.out.println("Método imprimir de la clase hija");
//    }
    public void imprimir() { // Este método no se lo puede sobre escribir por la palabra final
        System.out.println("Método imprimir de la clase hija");
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }
}