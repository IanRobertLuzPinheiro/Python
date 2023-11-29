def ler_dados(arquivo):
    funcionarios = []
    with open(arquivo, 'r') as file:
        for line in file:
            dados = line.strip().split()
            print(f"Dados: {dados}")
            funcionario = {
                'nome': dados[0],
                'sobrenome': dados[1],
                'ano_nascimento': int(dados[2]),
                'RG': dados[3],
                'ano_admissao': int(dados[4]),
                'salario': float(dados[5])
            }
            funcionarios.append(funcionario)

    return funcionarios

def Reajusta_dez_porcento(lista_funcionarios):
    for funcionario in lista_funcionarios:
        funcionario['salario'] *= 1.1 

def main():
    lista_funcionarios = ler_dados('DadosFucionarios.txt')
    

    Reajusta_dez_porcento(lista_funcionarios)

    print("\n\nDados após o reajuste de 10% do salário:")
    for funcionario in lista_funcionarios:
        print(funcionario)
        
if __name__ == "__main__":
    main()