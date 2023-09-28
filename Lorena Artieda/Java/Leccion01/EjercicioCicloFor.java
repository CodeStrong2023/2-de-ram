public class EjercicioCicloFor {
    public static void main(String[] args) {
        for(var contando=0; contando<7; contando++){
            if(contando%2==0){
                System.out.println("Contando= "+ contando);
                break;
            }
        }
        //Uso de las palabras break y continue junto a las etiquetas label;
        inicio:
        for(var contando=0; contando<7; contando++) {
            if (contando % 2 == 0) {


                continue inicio;
            }
            System.out.println("Contando= " + contando);
        }
    }
}
