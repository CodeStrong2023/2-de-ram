import javax.swing.*;

public class ej05 {
  public static void main(String[] args) {
    int numero, aleatorio, conteo = 0;
    aleatorio = (int) (Math.random()*100);
    do {
      numero = Integer.parseInt(JOptionPane.showInputDialog(null,"Ingrese un número"));
      if (numero < aleatorio){
        JOptionPane.showMessageDialog(null, "Ingrese un número mayor ");
      }else if (numero > aleatorio) {
        JOptionPane.showMessageDialog(null, "digite un número menor " );
      }else {
        JOptionPane.showMessageDialog(null, "acertó, son igulaes!! " );
      }
      conteo++;
    } while (numero != aleatorio);{
      JOptionPane.showMessageDialog(null, "Adivinaste en "+ conteo + " intentos");
    }
  }
}
