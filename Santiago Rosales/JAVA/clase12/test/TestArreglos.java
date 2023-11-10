package clase12.test;

public class TestArreglos {
    public static void main(String[] args) {
        // Los arreglos heredan de la clase object
        // Los arreglos no se pueden trabajar de manera dinámica
        int edades[] = new int[3]; // Entre los corchetes ponemos la cantidad límite de elementos que va a tener el arreglo
        System.out.println("edades = " + edades);
        // Modificar los elementos del arreglo
        edades[0] = 18;
        edades[1] = 44;
        edades[2] = 12;
        System.out.println("edades[0] = " + edades[0]);
        System.out.println("edades[1] = " + edades[1]);
        System.out.println("edades[2] = " + edades[2]);

        // Recorrer el arreglo
        for (int i = 0; i < edades.length; i++) {
            System.out.println(edades[i]);
        }
    }
}
