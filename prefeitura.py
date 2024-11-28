import os
os.system("cls || clear")

def adicionar_familia(dados):
    try:
        salario = float(input("Digite o salário da família: "))
        filhos = int(input("Digite o número de filhos da família: "))
        dados.append((salario, filhos))
        print("Família adicionada com sucesso!")
    except ValueError:
        print("Entrada inválida. Por favor, insira valores numéricos.")

def exibir_resultados(dados):
    if not dados:
        print("Nenhuma família cadastrada.")
        return

    total_familias = len(dados)
    media_salario = sum(s for s, _ in dados) / total_familias
    media_filhos = sum(f for _, f in dados) / total_familias
    maior_salario = max(s for s, _ in dados)
    menor_salario = min(s for s, _ in dados)

    print(f"Total de famílias: {total_familias}")
    print(f"Média do salário: {media_salario:.2f}")
    print(f"Média de filhos: {media_filhos:.2f}")
    print(f"Maior salário: {maior_salario:.2f}")
    print(f"Menor salário: {menor_salario:.2f}")

def salvar_dados(dados):
    with open("pesquisa_prefeitura.txt", "w") as file:
        for salario, filhos in dados:
            file.write(f"{salario},{filhos}\n")
    print("Dados salvos no arquivo 'pesquisa_prefeitura.txt'.")

def ler_dados():
    if os.path.exists("pesquisa_prefeitura.txt"):
        with open("pesquisa_prefeitura.txt", "r") as file:
            return [tuple(map(float, line.split(','))) for line in file]
    return []

def main():
    dados = ler_dados()

    while True:
        print("Menu:")
        print("1 - Adicionar família")
        print("2 - Exibir resultados")
        print("3 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            adicionar_familia(dados)
            salvar_dados(dados)

        elif opcao == '2':
            exibir_resultados(dados)
            input("Pressione Enter para continuar")
           
        elif opcao == '3':
            print("Saindo...")
            break
        else:
            print("Opção inválida")

if __name__ == "__main__":
    main()