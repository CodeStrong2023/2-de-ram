package Parametros;

public class Valor {
  public static void main(String[] args) {

    var valorX = 20;
    System.out.println("valorX = " + valorX);
    cambioValor(valorX); //se envia copia de la variable (el Valor)
    System.out.println("valorX = " + valorX);


  }
  public static void cambioValor(int arg1){
    System.out.println("arg1 = " + arg1);
  }
}
