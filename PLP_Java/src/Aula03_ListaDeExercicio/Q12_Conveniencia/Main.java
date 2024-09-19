package Aula03_ListaDeExercicio.Q12_Conveniencia;

public class Main {
    public static void main(String[] args) {
        Produto produto1 = new Produto("Produto A", 100);
        Produto produto2 = new Produto("Produto B", 200);

        double total = produto1.sumPrices(produto2);
        System.out.println("O preço total dos produtos é: R$ " + total);
    }
}
