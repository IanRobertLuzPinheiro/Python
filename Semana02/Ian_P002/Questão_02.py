#Para a segunda parte do exercício é possível criar um caminho para armazenar as tarefas
#Em seguida é necessário adicionar uma função que seja capaz de carregar tarefas ao iniciar o aplicativo
#Também é necessário adicionar uma função que seja capaz de salvar tarefas no arquivo de texto
#Essa função de carregar as taregas ao iniciar o aplicativo deve ser chamada logo na função main()
#A função de salvar tarefas deve ser chamada ao sair do progama
#É necessário adicionar os 'import os' e 'import json'
#As funções de salvar e carregar tarefas permitem que aplicativo mantenha a persistência de dados
#O programa salva as tarefas em um arquivo e as carrega de volta quando o aplicativo é executado novamente
#Abaixo está um esboço de como seriam essa funções


def carregar_tarefas():
    global tarefas
    if os.path.exists(ARQUIVO_TAREFAS): #Veririca a existencia de um possível arquivo de tarefa denominado ARQUIVO_TAREFAS
        #esse arquivo tem seu caminho criado anteriomente
        with open(ARQUIVO_TAREFAS, "r") as arquivo:
            tarefas = json.load(arquivo)

def salvar_tarefas():
    with open(ARQUIVO_TAREFAS, "w") as arquivo:
        json.dump(tarefas, arquivo, indent=2)