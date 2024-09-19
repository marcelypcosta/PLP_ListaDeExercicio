package Aula03_ListaDeExercicio;

public class Q03_ContaBancaria {
    // Private attributes
    private double saldo;
    private String titular;

    // Constructor
    public Q03_ContaBancaria(String titular, double saldoInicial) {
        this.saldo = saldoInicial;
        this.titular = titular;
    }

    // Method to deposit money into the account
    public void depositar(double valor) {
        if (valor > 0) {
            this.saldo += valor;
        } else {
            System.out.println("O valor do depósito deve ser positivo.");
        }
    }

    // Method to withdraw money from the account
    public void sacar(double valor) {
        if (valor > 0 && valor <= this.saldo) {
            this.saldo -= valor;
        } else {
            System.out.println("Saldo insuficiente ou valor inválido.");
        }
    }

    // Method to check the current balance
    public double consultarSaldo() {
        return this.saldo;
    }

    // Main method to test the class
    public static void main(String[] args) {
        Q03_ContaBancaria conta = new Q03_ContaBancaria("João", 1000);
        System.out.println("Saldo inicial: R$" + conta.consultarSaldo());
        conta.depositar(500);
        System.out.println("Saldo após depósito: R$" + conta.consultarSaldo());
        conta.sacar(300);
        System.out.println("Saldo após saque: R$" + conta.consultarSaldo());
    }
}
