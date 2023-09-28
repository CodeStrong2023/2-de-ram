package ejercicio7;

import java.util.Scanner;

public class Ejercicio7 {
    public static void main(String[] args) {
        /* Una companía de venta de autos usados, paga a su personal de ventas
        un salario de $1000 mensuales mas una comision de $150 por cada venta,
        más el 5% del valor de la venta. Cada mes el capturista de la empresa 
        ingresa en la computadora los datos pertinentes. Hacer un programa que 
        calcule e imprima el salario mensaual de un vendedor dado.
        */
        final var salario = 1000;
        var comision = 150;
        float salarioMensual, ventaAuto, porcVenta, totalPrecio;
        Scanner entrada = new Scanner(System.in);
        System.out.println("Ingrese la cantidad de ventas realizó el empleado");
        int venta = Integer.parseInt(entrada.nextLine());
        System.out.println("Ingrese el valor de las ventas");
        ventaAuto = Float.parseFloat(entrada.nextLine());
        comision *= venta;
        totalPrecio = ventaAuto * venta;
        porcVenta = totalPrecio * 0.05f;
        salarioMensual = salario + comision + porcVenta;
        System.out.println("El salario mensual es " + salarioMensual);
        
    }
    
}
