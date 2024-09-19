def isMenor(vetor):
    menor = vetor[0]

    for i in range(1, len(vetor)):
        if vetor[i] < menor:
            menor = vetor[i]

    return menor

def isMaior(vetor):
    maior = vetor[0]

    for i in range(1, len(vetor)):
        if vetor[i] > maior:
            maior = vetor[i]

    return maior


def main():
    vetor = []

    for i in range(5):
        vetor.append(int(input(f"Digite o {i + 1}º elemento da lista: ")))

    maior = isMaior(vetor)
    menor = isMenor(vetor)

    print(f"O maior elemento do vetor é {maior}")
    print(f"O menor elemento do vetor é {menor}")

if __name__ == "__main__":
    main()