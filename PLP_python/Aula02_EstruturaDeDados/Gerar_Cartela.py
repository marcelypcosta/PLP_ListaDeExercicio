import random

def gerarCartela():
    numeros = set()
    cartela = []

    for i in range(5):
        numero = random.randint(0, 99)
        while numero in numeros:
            numero = random.randint(0, 99)
        numeros.add(numero)
        cartela.append(numero)

    return cartela

def main():
    cartela = gerarCartela()
    print("Cartela de Bingo")
    for linha in cartela:
        print(linha)

## Tarefa de casa melhorar como mostra a tabela

if __name__ == "__main__":
    main()