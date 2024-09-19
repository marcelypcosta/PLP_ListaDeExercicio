package Aula03_ListaDeExercicio;

class Q013_Matematica {

    public static int fatorial(int n) {
        if (n == 0 || n == 1) {
            return 1;
        } else {
            return n * fatorial(n - 1);
        }
    }

    public static void main(String[] args) {
        System.out.println("O fatorial de 5 é: " + Q013_Matematica.fatorial(5));
        System.out.println("O fatorial de 0 é: " + Q013_Matematica.fatorial(0));
    }
}



