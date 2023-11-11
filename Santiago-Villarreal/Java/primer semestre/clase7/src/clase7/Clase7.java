package clase7;

public class Clase7 {
    
    public static void main(String[] args) {
        int num1 = 5, num2 = 4;
        var solucion = num1 + num2;
        System.out.println("solución: suma = " + solucion);
        solucion = num1 - num2;
        System.out.println("solución de la resta = " + solucion);
        solucion = num1 * num2;
        System.out.println("solucion de la multiplicacion = " + solucion);
        solucion = num1 / num2;
        System.out.println("solucion de la división = " + solucion);
        var solucion2 = 3.4 / num2;
        System.out.println("solución 2 resultado de la división = " + solucion2);
        solucion = num1 % num2;
        System.out.println("solucion del resto entero = " + solucion);
        
        if (num1 % 2 == 0)
            System.out.println("Es un número par");
        else
            System.out.println("Es un número impar");
        
        int varNum1 = 1, varNum2 = 4;
        int varNum3 = varNum1 + 6 - varNum2;
        System.out.println("varNum3 = " + varNum3);
        
        varNum1 += 1;
        System.out.println("varNum1 = " + varNum1);
        
        varNum1 *= 2;
        System.out.println("varNum1 = " + varNum1);
        
        varNum1 /= 2;
        System.out.println("varNum1 = " + varNum1);
        
        varNum1 %= 1;
        System.out.println("varNum1 = " + varNum1);
        
    }
    
}
