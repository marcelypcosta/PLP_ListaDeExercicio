class ContaBancaria:
    """
    A class used to represent a Bank Account.
    """

    def __init__(self, titular, saldo_inicial=0):
        """
        The constructor for the ContaBancaria class.
        """
        self.__saldo = saldo_inicial  # Private attribute
        self.titular = titular

    def depositar(self, valor):
        """
        Deposits a given amount into the account.
        """
        if valor > 0:
            self.__saldo += valor
        else:
            print("O valor do depósito deve ser positivo.")

    def sacar(self, valor):
        """
        Withdraws a given amount from the account, if sufficient funds are available.
        """
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
        else:
            print("Saldo insuficiente ou valor inválido.")

    def consultar_saldo(self):
        """
        Returns the current balance of the account.
        """
        return self.__saldo


# Example usage
conta = ContaBancaria("João", 1000)
print("Saldo inicial: R$", conta.consultar_saldo())
conta.depositar(500)
print("Saldo após depósito: R$", conta.consultar_saldo())
conta.sacar(300)
print("Saldo após saque: R$", conta.consultar_saldo())
