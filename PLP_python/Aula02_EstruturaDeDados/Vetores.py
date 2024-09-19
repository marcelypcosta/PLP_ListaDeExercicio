def soma(vetor, x, y):
    return vetor[x] + vetor[y]

def main():
    vetor = [0] * 8

    for i in range(8):
        vetor[i] = int(input(f"Digite o valor da posição {i}: "))

    x = int(input("X = Digite a posição do valor que deseja somar: "))
    y = int(input("Y = Digite a posição do valor que deseja somar: "))

    resultado = soma(vetor, x, y)

    print(f"A soma dos valores nas posições X e Y é de {resultado}")

if __name__ == "__main__":
    main()
