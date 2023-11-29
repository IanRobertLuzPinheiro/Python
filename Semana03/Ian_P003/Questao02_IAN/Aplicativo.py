#Implementação da função de reajustar o preço dos produtos no exercicio 1
def cadastrar(produtos):
    print("\nCadastrar Novo Produto")
    codigo = input("Digite o código do produto que contenha apenas e somente 13 caracteres numéricos: ")
    
    while len(codigo) != 13 or not codigo.isdigit():
        print("\nCódigo inválido. Digite novamente")
        codigo = input("Digite o código do produto que contenha apenas e somente 13 caracteres numéricos: ")

    nome = input("Digite o nome do produto com o primeiro caractere maiúsculo: ")

    while not nome[0].isupper():
        print("\nNome inválido. Digite novamente")
        nome = input("Digite o nome do produto com o primeiro caractere maiúsculo: ")

    preco = input("Digite o preço do produto utilizando no máximo duas casas decimais ")

    while not preco.replace('.', '', 1).isdigit():
        print("\nPreço inválido. Digite novamente")
        preco = input("Digite o preço do produto utilizando no máximo duas casas decimais ")

    produto = {"codigo": codigo, "nome": nome, "preco": float(preco)}
    produtos.append(produto)
    print("Produto cadastrado com sucesso!\n")

def excluir(produtos):
    print("\nExcluir Produto")
    codigo = input("Digite o código do produto a ser excluído: ")

    for produto in produtos:
        if produto["codigo"] == codigo:
            produtos.remove(produto)
            print("Produto excluído com sucesso!\n")
            return

    print("Produto não encontrado.\n")

def listar(produtos):
    print("\nLista de Produtos")
    
    for i, produto in enumerate(produtos, start=1):
        print(f"{i}. Código: {produto['codigo']}, Nome: {produto['nome']}, Preço: R${produto['preco']:.2f}")

    print()

def consultar(produtos):
    print("\nConsultar Preço")
    codigo = input("Digite o código do produto a ser consultado: ")

    for produto in produtos:
        if produto["codigo"] == codigo:
            print(f"O produto é {produto['nome']} e seu preço é R${produto['preco']:.2f}\n")
            return

    print("Produto não encontrado.\n")

def reajustar(produtos):
    for produto in produtos:
        produto['preco'] *= 1.1

    print("Preços reajustados em 10%.\n")

def main():
    produtos = []
    
    while True:
        print("\nMenu Principal")
        print("1. Cadastrar novo produto")
        print("2. Excluir produto cadastrado")
        print("3. Listar todos os produtos")
        print("4. Consultar preço de um produto")
        print("5. Reajustar preços em 10%")
        print("6. Sair")

        opcao = input("Digite a opção desejada: ")

        if opcao == "1":
            cadastrar(produtos)
        elif opcao == "2":
            excluir(produtos)
        elif opcao == "3":
            listar(produtos)
        elif opcao == "4":
            consultar(produtos)
        elif opcao == "5":
            reajustar(produtos)
        elif opcao == "6":
            print("Saindo do programa. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
