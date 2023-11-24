#Para a segunda parte do exercício é possível criar um caminho para armazenar as tarefas
#Em seguida é necessário adicionar uma função que seja capaz de carregar tarefas ao iniciar o aplicativo
#Também é necessário adicionar uma função que seja capaz de salvar tarefas no arquivo de texto
#Essa função de carregar as taregas ao iniciar o aplicativo deve ser chamada logo na função main()
#A função de salvar tarefas deve ser chamada ao sair do progama
#É necessário adicionar os 'import os' e 'import json'
#As funções de salvar e carregar tarefas permitem que aplicativo mantenha a persistência de dados
#O programa salva as tarefas em um arquivo e as carrega de volta quando o aplicativo é executado novamente

import os
import json

file = "tarefas.json"

tarefas = []

def carregar_tarefas():
    global tarefas
    if os.path.exists(file):
        with open(file, "r") as arquivo:
            tarefas = json.load(arquivo)

def salvar_tarefas():
    with open(file, "w") as arquivo:
        json.dump(tarefas, arquivo, indent=2)


def listar():
    print("Lista de Tarefas:")
    for i, tarefa in enumerate(tarefas, start=1):
        status = "[x]" if tarefa["concluida"] else "[ ]"
        print(f"{i}. {tarefa['descricao']} {status}")

def registrar():
    descricao = input("Digite a descrição da tarefa: ").capitalize()
    tarefa = {"descricao": descricao, "concluida": False}
    tarefas.append(tarefa)
    print("Tarefa registrada!")

def marcar():
    listar()
    try:
        id_tarefa = int(input("Digite o ID da tarefa a ser marcada como realizada: ")) - 1
        if 0 <= id_tarefa < len(tarefas):
            tarefa = tarefas.pop(id_tarefa)
            tarefa["concluida"] = True
            tarefas.insert(0, tarefa)
            print("Tarefa marcada como realizada!")
        else:
            print("ID inválido")
    except ValueError:
        print("Digite ID válido.")

def editar():
    listar()
    try:
        id_tarefa = int(input("Digite o ID da tarefa a ser editada: ")) - 1
        if 0 <= id_tarefa < len(tarefas):
            nova_descricao = input("Digite a nova descrição da tarefa: ").capitalize()
            tarefas[id_tarefa]["descricao"] = nova_descricao
            print("Tarefa editada com sucesso!")
        else:
            print("ID inválido")
    except ValueError:
        print("Digite ID válido.")

def main():
    carregar_tarefas()
    while True:
        print("\nMenu:")
        print("1. Listar tarefas")
        print("2. Registrar nova tarefa")
        print("3. Marcar tarefa como realizada")
        print("4. Editar tarefa")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            listar()
        elif opcao == "2":
            registrar()
        elif opcao == "3":
            marcar()
        elif opcao == "4":
            editar()
        elif opcao == "5":
            salvar_tarefas()
            print("Saindo do aplicativo. Até mais!")
            break
        else:
            print("Opção inválida!!")
if __name__ == "__main__":
    main()