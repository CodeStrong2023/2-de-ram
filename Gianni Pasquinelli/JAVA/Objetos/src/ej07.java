import javax.swing.*;

public class ej07 {
  public static void main(String[] args) {
    int numero, conteo = 0, suma = 0;
    float promedio = 0;

    numero = Integer.parseInt(JOptionPane.showInputDialog(null,"Digite un número: " ));
    while (numero >= 0){
      suma += numero;
      conteo++;
      numero = Integer.parseInt(JOptionPane.showInputDialog(null,"Digite otro número: " ));

    }
    if (conteo == 0){
      System.out.println("Error " );
    }else {
      promedio = (float)suma / conteo;
      JOptionPane.showMessageDialog(null, "El promedio es: " + promedio);
    }
  }
}
