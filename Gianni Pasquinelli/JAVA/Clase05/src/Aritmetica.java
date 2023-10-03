public class Aritmetica {
  int a;
  int b;

  // constructor -> método especial
  public Aritmetica(){
    System.out.println("ejecutando constructor 1");
  }
  // sobrecarga
  public Aritmetica(int a, int b){
    this.a = a;
    this.b = b;
    System.out.println("ejecutando constructor 2");
  }


  public void sumarNumeros(){
    int resultado = a + b;
    System.out.println("Resultado = " + resultado);
  }
  public int sumarConRetorno(){
    int resultado = a + b;
    return resultado;
  }

  public int sumarConArgumentos(int a, int b ) {
    this.a = a;
    this.b = b;
    // return a + b;
    return sumarConRetorno();
  }


}
