public class Ciclos {
  public static void main(String[] args) {
    // while
    var conteo = 0;
    while (conteo <= 4) {
      System.out.println("conteo = " + conteo);
      conteo++;
    }

    // Do - while
    var count = 0;
    do {
      System.out.println("count = " + count);
      count++;
    } while(count <=4);

    // for
    for (var i = 1; i <=7 ; i++){
      if(i % 2 == 0){
        System.out.println("par con break " + i);
        break; // con este breack sale del ciclo al encontrar el primer numero par
      }
    }

    for (var i = 1; i <=7 ; i++){
      if(i % 2 != 0){
        continue;
      }
      System.out.println("par con continue " + i);
    }
    //break y continue

  //labels
    inicio:
    for (var i = 0; i<= 7; i++){
      if (i % 2 == 0){
        System.out.println("i = " + i);
        break inicio;
      }
    }




  }
}
