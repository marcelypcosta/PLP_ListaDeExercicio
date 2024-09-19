def vetorA():
    vetorA = []
    for i in range(2):
        vetorA.append(int(input(f"Digite o {i + 1}º elemento do vetor A: ")))
    return vetorA

def vetorB():
    vetorB = []
    for i in range(2):
        vetorB.append(int(input(f"Digite o {i + 1}º elemento do vetor B: ")))
    return vetorB

def vetorC(vA, vB):
    vetorC = []
    for i in range(2):
        vetorC.append(vA[i] + vB[i])
    return vetorC

def main():
    vA = vetorA()
    vB = vetorB()
    vC = vetorC(vA, vB)

    print("Vetor A:", vA)
    print("Vetor B:", vB)
    print("Vetor C:", vC)

if __name__ == "__main__":
    main()
