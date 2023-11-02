
package caja;

public class pruebaCaja {
    public static void main(String[] args) {
        int MedidaAncho = 3;
        int medidaAlto = 2;
        int medidaProfund = 6;
        
        Caja caja1 = new Caja();
        caja1.ancho = MedidaAncho;
        caja1.alto = medidaAlto;
        caja1.profundidad = medidaProfund;
        int resultado = caja1.calcularVolumen();
        System.out.println("resultado volumen de caja 1= " + resultado);
        
        Caja caja2 = new Caja(2,4,6);
        System.out.println("resultado volumen caja 2= " + caja2.calcularVolumen());
    }
}
