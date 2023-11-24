tarefas = []

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
            print("Programa encerrado")
            break
        else:
            print("Opção inválida!!")
if __name__ == "__main__":
    main()