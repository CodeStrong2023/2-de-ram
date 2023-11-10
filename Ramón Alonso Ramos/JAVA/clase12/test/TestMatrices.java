package clase12.test;

import clase12.domain.Persona;

public class TestMatrices {
    public static void main(String[] args) {
        int edades[][] = new int[3][2];
        System.out.println("edades = " + edades);
        edades[0][0] = 7;
        edades[0][1] = 5;
        edades[1][0] = 8;
        edades[1][1] = 4;
        edades[2][0] = 10;
        edades[2][1] = 3;
        System.out.println("edades edades 0 - 0 = " + edades[0][0]);
        System.out.println("edades edades 0 - 1 = " + edades[0][1]);
        System.out.println("edades edades 1 - 0 = " + edades[1][0]);
        System.out.println("edades edades 1 - 1 = " + edades[1][1]);
        System.out.println("edades edades 2 - 0 = " + edades[2][0]);
        System.out.println("edades edades 2 - 1 = " + edades[2][1]);

        System.out.println("Recorremos la matriz a través del cliclo for");
        for (int fila = 0; fila < edades.length; fila++) {
            for (int col = 0; col < edades[fila].length ; col++) {
                System.out.println("edades " + fila + "-" + col + ": " + edades[fila][col]);
            }
        }

//        String frutas[][] = new String[3][2]:
        String frutas[][] = {{"Limón", "Pomelo"}, {"Ciruela", "Kiwi"}, {"Banana", "Manzana"}};
        System.out.println("Recorremos nuestra matriz de frutas con ciclo for");
        for (int i = 0; i < frutas.length; i++) {
            for (int j = 0; j < frutas[i].length ; j++) {
                System.out.println("frutas " + i + "-" + j + ": " + frutas[i][j]);
            }
        }

        Persona personas[][] = new Persona[2][3];
        personas[0][0] = new Persona("Jose");
        personas[0][1] = new Persona("Juan");
        personas[0][2] = new Persona("Maria");
        personas[1][0] = new Persona("Pedro");
        personas[1][1] = new Persona("Simon");
        personas[1][2] = new Persona("Ana");

        System.out.println("personas 0-0: " + personas[0][0]);
        System.out.println("personas 0-1: " + personas[0][1]);
        System.out.println("personas 0-2: " + personas[0][2]);
        System.out.println("personas 1-0: " + personas[1][0]);
        System.out.println("personas 1-1: " + personas[1][1]);
        System.out.println("personas 1-2: " + personas[1][2]);

    }
}
