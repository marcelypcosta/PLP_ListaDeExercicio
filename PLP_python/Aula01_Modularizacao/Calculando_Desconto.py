def calculandoReducaoEmMinutos(cigarrosPorDia, haQuantosAnosFuma):
    return cigarrosPorDia * 365 * haQuantosAnosFuma * 10


def calculandoReducaoEmDias(reducaoEmMinutos):
    return reducaoEmMinutos / (24 * 60)


def exibir(reducaoEmDias):
    print(f"Você está reduzindo sua vida em {reducaoEmDias:.0f} dias")


def main():
    cigarrosPorDia = int(input("Digite quantos cigarros fuma por dia: "))
    haQuantosAnosFuma = int(input("Digite há quantos anos fuma: "))

    reducaoEmMinutos = calculandoReducaoEmMinutos(cigarrosPorDia, haQuantosAnosFuma)
    reducaoEmDias = calculandoReducaoEmDias(reducaoEmMinutos)

    exibir(reducaoEmDias)


if __name__ == "__main__":
    main()
