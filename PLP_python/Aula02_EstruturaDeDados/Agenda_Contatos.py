import json

def coletarDados():
    dados = []
    continuar = 'sim'

    while continuar.lower() == 'sim':
        nome = input("Digite seu nome completo: ")
        numero = input("Digite o número (YY XXXXX-XXXX): ")

        dados.append({
            "nome": nome,
            "numero": numero
        })

        continuar = input("Deseja adicionar mais [sim/nao]? ").strip().lower()
        if continuar == 'não':
            break

    return dados

def salvarEmArquivoTXT(dados, nomeArquivo):
    with open(nomeArquivo, "w") as arquivo:
        for item in dados:
            dados = (f"Nome: {item['nome']}\n"
                     f"Número: {item['numero']}\n\n")
            arquivo.write(dados)


def salvarEmArquivoJSON(dados, nomeArquivo):
    with open(nomeArquivo, "w") as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)


def main():
    dados = coletarDados()

    if dados:
        tipoDoArquivo = input("Deseja armazenar em que tipo de arquivo (.txt ou .json)? ")
        if tipoDoArquivo == 'txt':
            salvarEmArquivoTXT(dados, 'agendaDeContatos.txt')
            print("Dados salvos no arquivo 'agendaDeContatos.txt'.")
        elif tipoDoArquivo == 'json':
            salvarEmArquivoJSON(dados, 'agendaDeContatos.json')
            print("Dados salvos no arquivo 'agendaDeContatos.json'.")
    else:
        print("Nenhum dado foi coletado!")


if __name__ == "__main__":
    main()
