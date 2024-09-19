package Aula03_ListaDeExercicio;

public class Main {
    public static void main(String[] args) {
        Q015_ContaBancaria conta = new Q015_ContaBancaria("João", 1000);

        try {
            conta.sacar(1500);  // Tentativa de sacar mais que o saldo
        } catch (Q015_SaldoInsuficienteException e) {
            System.out.println(e.getMessage());
        }
    }
}
