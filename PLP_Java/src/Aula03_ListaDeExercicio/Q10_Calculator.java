package Aula03_ListaDeExercicio;

public class Q10_Calculator {
    public int sum(int a, int b) {
        return a + b;
    }

    public int sum(int a, int b, int c) {
        return a + b + c;
    }

    public static void main(String[] args) {
        Q10_Calculator calculator = new Q10_Calculator();

        int result1 = calculator.sum(10, 20);
        System.out.println("Soma de dois números: " + result1);

        int result2 = calculator.sum(10, 20, 30);
        System.out.println("Soma de três números: " + result2);
    }
}
