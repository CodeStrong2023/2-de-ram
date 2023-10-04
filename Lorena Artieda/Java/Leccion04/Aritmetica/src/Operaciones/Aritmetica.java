package Operaciones;

public class Aritmetica {
    //Atributos de la clase
    int a;
    int b;

    //Metodos
    public void sumarNumeros(){
        int resultado= a + b;
        System.out.println("resultado: "+ resultado);
    }
    public int sumarConRetorno(){
        int resultado= a + b;
        return a + b;
    }

    public int sumarConArgumentos(int argA, int argB){
        this.a= argA;
        this.b=argB;
        //return a+b;
        return sumarConRetorno(); //NO se recomienda
    }


}
