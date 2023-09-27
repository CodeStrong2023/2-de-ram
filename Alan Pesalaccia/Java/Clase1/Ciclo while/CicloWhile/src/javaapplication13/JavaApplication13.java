
package javaapplication13;


public class JavaApplication13 {


    public static void main(String[] args) {
        var conteo = 0; //inferencia de tipos
        while (conteo <= 7 ){
            System.out.println("conteo = " + conteo);
            conteo++;
        }
        
        var contador = 0;
        do{
            System.out.println("contador = " + contador);
            contador++;
        
        }while(contador <= 7);
        for(int i=0; i <= 7; i++ ){
            if(i % 2 != 0){
                  System.out.println("i = " + i);
                  break;
            }
        }
        inicio:    
        for(int i=0; i <= 7; i++ ){
            if(i % 2 != 0){
                continue inicio;
            }          
             System.out.println("i = " + i);
        
        } 
    }
}
    

