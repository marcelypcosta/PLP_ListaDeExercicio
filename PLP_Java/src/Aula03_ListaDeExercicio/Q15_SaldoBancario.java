package Aula03_ListaDeExercicio;

class Q015_SaldoInsuficienteException extends Exception {
    public Q015_SaldoInsuficienteException(String message) {
        super(message);
    }
}

class Q015_ContaBancaria {
    private double saldo;

    public Q015_ContaBancaria(String titular, double saldo) {
        this.saldo = saldo;
    }

    public void sacar(double valor) throws Q015_SaldoInsuficienteException {
        if (valor > saldo) {
            throw new Q015_SaldoInsuficienteException(
                    "Erro: Tentativa de saque de R$" + valor + ", mas saldo disponível é R$" + saldo + "."
            );
        }
        saldo -= valor;
    }

    public double getSaldo() {
        return saldo;
    }
}

