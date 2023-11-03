package clase12.test;

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
    }
}
