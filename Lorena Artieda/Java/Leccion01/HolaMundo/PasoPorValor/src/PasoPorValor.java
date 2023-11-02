package HolaMundo.PasoPorValor.src;

public class PasoPorValor {
    public static void main(String[] args) {
        var valorX=20;
        System.out.println("valorX = " + valorX);
        cambioValor(valorX);//SOlo le enviamos una copia
    }
    public static void cambioValor(int arg1){
        System.out.println("arg1 = " + arg1);
    }
}
