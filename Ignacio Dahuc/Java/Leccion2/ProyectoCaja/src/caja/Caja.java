package caja; //Package

public class Caja { //Clase publica Caja

    //Atributos (caracteristicas)
    int ancho;
    int alto;
    int profundidad;

    //Métodos y constructores (acciones)
    public Caja() {} //Constructor 1 = vacio

    //Constructor con parámetros
    public Caja(int ancho, int alto, int profundidad) { //Constructor 2
        this.ancho = ancho;
        this.alto = alto;
        this.profundidad = profundidad;
    }

    public int calcularVolumen() { //Método para calcular
        return ancho * alto * profundidad;
    }

}