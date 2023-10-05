package aritmetica;
public class aritmetica {
    //atributos
    int a;
    int b;
    //metodo
    public void sumarNumeros(){
        int resultado = a + b;
        System.out.println("resultado = " + resultado);
    }
    public int sumarConRetorno(){
    return a + b;
    }
    public int sumarConArgumentos(int arg1,int arg2){
        this.a = arg1;
        this.b = arg2;
        //return a + b;
        return this.sumarConRetorno();
    }
}
