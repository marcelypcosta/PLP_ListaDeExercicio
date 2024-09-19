class Q015_SaldoInsuficienteException(Exception):
    def __init__(self, message="Saldo insuficiente para realizar o saque."):
        self.message = message
        super().__init__(self.message)


class Q015_ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def sacar(self, valor):
        if valor > self.saldo:
            raise Q015_SaldoInsuficienteException(
                "Erro: Tentativa de saque de R${}, mas saldo disponível é R${}.".format(valor, self.saldo)
            )
        self.saldo -= valor
        return self.saldo


if __name__ == "__main__":
    conta = Q015_ContaBancaria("João", 1000)

    try:
        conta.sacar(1500)
    except Q015_SaldoInsuficienteException as e:
        print(e)
