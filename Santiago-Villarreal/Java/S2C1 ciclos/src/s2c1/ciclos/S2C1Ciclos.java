package s2c1.ciclos;
public class S2C1Ciclos {
    public static void main(String[] args) {
        var conteo = 0;
        while(conteo < 3){
            System.out.println("conteo = " + conteo);
            conteo ++;
        }
        var contador = 0;
        do {  
            System.out.println("contador = " + contador);
            contador ++;
        } while(contador < 7);
        
        for(var contando = 0; contando < 7; contando++){
            System.out.println("contando = " + contando);
        }
        for(var contando = 0;contando < 7; contando++){
            if(contando % 2 != 0){
                System.out.println("contando = " + contando);
                break;
            }
        }
        for(var contando = 0; contando < 7;contando++){
            if(contando % 2 !=0){
                continue;
            }
            System.out.println("contando = " + contando);
        }
    

    }
    
}
