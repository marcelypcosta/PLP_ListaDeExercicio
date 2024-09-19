class Produto:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    # Sobrecarga do operador + para somar preços de produtos
    def __add__(self, other):
        if isinstance(other, Produto):
            return self.price + other.price
        raise TypeError("A soma só pode ser feita entre objetos da classe Produto.")

# Testando a sobrecarga do operador +
if __name__ == "__main__":
    produto1 = Produto("Produto A", 100)
    produto2 = Produto("Produto B", 200)

    total = produto1 + produto2
    print("O preço total dos produtos é: R${}".format(total))
