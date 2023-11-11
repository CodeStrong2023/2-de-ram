package test;

public class operacionestest {

    public static void main(String[] args) {
        var operacionInt = Operaciones.sumar(10, 6);
        System.out.println("operacionInt = " + operacionInt);

        var operacionDouble = Operaciones.sumar(20.4, 4.23);
        System.out.println("operacionDouble = " + operacionDouble);
    }
}
