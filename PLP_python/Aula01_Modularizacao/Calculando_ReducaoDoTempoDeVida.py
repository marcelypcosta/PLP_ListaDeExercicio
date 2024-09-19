def calculandoValorDoDesconto(valor, desconto):
    return valor * (desconto / 100)


def calculandoValorFinal(valor, valorDoDesconto):
    return valor - valorDoDesconto


def exibirValorFinal(produto, valor, desconto, valorDoDesconto, valorFinal):
    print(f"\nAs LOJAS MAGALU estão com promoção de {desconto} % em toda a loja!!! "
          f"\n\nNota Fiscal\n\n"
          f"{produto} - R$ {valor:.2f} (- R$ {valorDoDesconto:.2f})\n\n"
          f"Valor Final: R$ {valorFinal:.2f}")


def main():
    produto = str(input("Digite o produto que deseja comprar: "))
    valor = float(input("Digite o valor do produto: R$ "))
    desconto = int(input("Digite o desconto (em %) que as lojas MAGALU está dando: "))

    valorDoDesconto = calculandoValorDoDesconto(valor, desconto)
    valorFinal = calculandoValorFinal(valor, valorDoDesconto)

    exibirValorFinal(produto, valor, desconto, valorDoDesconto, valorFinal)


if __name__ == "__main__":
    main()
