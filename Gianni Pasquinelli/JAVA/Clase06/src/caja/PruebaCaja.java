package caja;

public class PruebaCaja {
  public static void main(String[] args) {
    int medidaAncho = 3;
    int medidaAlto = 2;
    int medidaProfundidad = 6;

    Caja caja1 = new Caja();
    caja1.ancho = medidaAncho;
    caja1.alto = medidaAlto;
    caja1.profundidad = medidaProfundidad;
    int resultado = caja1.calcularVolumen();
    System.out.println("resultado caja 1 = " + resultado);

    Caja caja2 = new Caja(2,4,6);
    System.out.println("caja2 = " + caja2.calcularVolumen());


  }



}
