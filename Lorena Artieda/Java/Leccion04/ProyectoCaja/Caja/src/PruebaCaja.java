/*
Proyecto caja:
Ejercicio 1: Crear un proyecto segun las especificaciones
mostradas a continuacion.
La formula del volumen es: volumen= ancho* alto * profundidad;
 */
public class PruebaCaja {
    public static void main(String[] args) {
        Caja caja1= new Caja();

        Caja caja2= new Caja(2,3,6);

        double volumenCaja= caja2.volumen(2,4,6);

        System.out.println("volumenCaja = " + volumenCaja);
    }



}
