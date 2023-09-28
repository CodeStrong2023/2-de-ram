package clase10java;
public class Clase10Java {
    public static void main(String[] args) {
        var condicion = true;
        if(condicion){
            System.out.println("Condición verdadera");
        } else {
            System.out.println("Condición falsa");
        }
        var numero = 4;
        var numeroTexto = "Número desconocido";
        if(numero == 1){
            numeroTexto = "Número uno";
        } else if(numero == 2){
            numeroTexto = "Número dos"; 
        } else if(numero == 3){
            numeroTexto = "Número tres";
        } else if(numero == 4){
            numeroTexto = "Número cuatro";
        } else {
            numeroTexto = "Número no encontrado";
        } 
        System.out.println("numeroTexto = " + numeroTexto);
        
    }
    
}
