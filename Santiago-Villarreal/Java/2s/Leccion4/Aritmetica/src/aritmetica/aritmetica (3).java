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
    // El constructor es un método especial
    public aritmetica(){
        System.out.println("Se está ejecutando el contructor 1");
    }
    public aritmetica(int a, int b){
        this.a = a;
        this.b = b;
        System.out.println("Se está ejecutando el constructor 2");
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
