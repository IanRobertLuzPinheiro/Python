
from abc import ABC, abstractmethod
import numpy as np

class Data:
    
    def __init__(self, dia = 1, mes = 1, ano = 2000):
        if dia < 1 or dia > 31:
            raise ValueError("Dia inválido")
        if mes < 1 or mes > 12:
            raise ValueError("Mês inválido")
        if ano < 2000 or ano > 2100:
            raise ValueError("Ano inválido")
        self.__dia = dia
        self.__mes = mes
        self.__ano = ano

    @property
    def dia(self):
        return self.__dia
    
    @dia.setter
    def dia(self, dia):
        if dia < 1 or dia > 31:
            raise ValueError("Dia inválido")
        self.__dia = dia

    @property
    def mes(self):
        return self.__mes
    
    @mes.setter
    def mes(self, mes):
        if mes < 1 or mes > 12:
            raise ValueError("Mês inválido")
        self.__mes = mes

    @property
    def ano(self):
        return self.__ano
    
    @ano.setter
    def ano(self, ano):
        if ano < 2000 or ano > 2100:
            raise ValueError("Ano inválido")
        self.__ano = ano
    
    def __str__(self):
        return "{}/{}/{}".format(self.__dia, self.__mes, self.__ano)

    def __eq__(self, outraData):
        return  self.__dia == outraData.__dia and \
                self.__mes == outraData.__mes and \
                self.__ano == outraData.__ano
    
    def __lt__(self, outraData):
        if self.__ano < outraData.__ano:
            return True
        elif self.__ano == outraData.__ano:
            if self.__mes < outraData.__mes:
                return True
            elif self.__mes == outraData.__mes:
                if self.__dia < outraData.__dia:
                    return True
        return False
    
    def __gt__(self, outraData):
        if self.__ano > outraData.__ano:
            return True
        elif self.__ano == outraData.__ano:
            if self.__mes > outraData.__mes:
                return True
            elif self.__mes == outraData.__mes:
                if self.__dia > outraData.__dia:
                    return True
        return False

class AnaliseDados(ABC): 

    @abstractmethod
    def __init__(self, tipoDeDados):
        self.__tipoDeDados = tipoDeDados

    @abstractmethod
    def entradaDeDados(self):
        pass

    @abstractmethod
    def mostraMediana(self):
        pass
    
    @abstractmethod
    def mostraMenor(self):
        pass

    @abstractmethod
    def mostraMaior(self):
        pass

class ListaNomes(AnaliseDados):
    
    def __init__(self):
        super().__init__(type("String"))
        self.__lista = []        

    def entradaDeDados(self):
        try:
            num_elementos = int(input("Quantos elementos na lista de nomes? "))
            for i in range(num_elementos):
                print("")
                print(f"Informe o {i+1}º nome!")
                nome = input("-> ")
                self.__lista.append(nome)
            print("")
            self.__lista.sort()
        except ValueError:
            print("Entrada inválida. Por favor, insira um número inteiro.")

    def mostraMediana(self):
        print(f"Mediana: {self.__lista[len(self.__lista)//2 - 1]}")

    def mostraMenor(self):
        print(f"Menor: {self.__lista[0]}")

    def mostraMaior(self):
        print(f"Maior: {self.__lista[len(self.__lista)-1]}")

    def __str__(self):
        for id, item in enumerate(self.__lista):
            print(f"{id+1}: {item}")
	
class ListaDatas(AnaliseDados):
        
    def __init__(self):
        super().__init__(type(Data))
        self.__lista = []        
    
    def entradaDeDados(self):
        try:
            num_elementos = int(input("Quantos elementos na lista de datas? "))
            for i in range(num_elementos):
                print("")
                print(f"Informe a {i+1}ª data!")
                dia = int(input("Digite o dia: "))
                mes = int(input("Digite o mês: "))
                ano = int(input("Digite o ano: "))
                nova_data = Data(dia, mes, ano)
                self.__lista.append(nova_data)
            print("")
            self.__lista.sort()
        except ValueError as e:
            print(f"Entrada inválida: {e}. Por favor, insira valores numéricos válidos.")
    
    def mostraMediana(self):
        print(f"Mediana: {self.__lista[len(self.__lista)//2 - 1]}")

    def mostraMenor(self):
        print(f"Menor: {self.__lista[0]}")

    def mostraMaior(self):
        print(f"Maior: {self.__lista[len(self.__lista)-1]}")

    def __str__(self):
        for id, item in enumerate(self.__lista):
            print(f"{id+1}: {item}")

class ListaSalarios(AnaliseDados):

    def __init__(self):
        super().__init__(type(float))
        self.__lista = []        

    def entradaDeDados(self):
        try:
            num_elementos = int(input("Quantos elementos na lista de salários? "))
            for i in range(num_elementos):
                print("")
                print(f"Informe o {i+1}º salário!")
                salario = float(input("-> "))
                self.__lista.append(salario)
            self.__lista.sort()
            print("")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")

    def mostraMediana(self):
        print(f"Mediana: {np.median(self.__lista)}")

    def mostraMenor(self):
        print(f"Menor: {self.__lista[0]}")

    def mostraMaior(self):
        print(f"Maior: {self.__lista[len(self.__lista)-1]}")

    def __str__(self):
        for id, item in enumerate(self.__lista):
            print(f"{id+1}: {item}")

class ListaIdades(AnaliseDados):
    
    def __init__(self):
        super().__init__(type(int))
        self.__lista = []        
    
    def entradaDeDados(self):
        try:
            num_elementos = int(input("Quantos elementos na lista de idades? "))
            for i in range(num_elementos):
                print("")
                print(f"Informe a {i+1}ª idade!")
                idade = int(input("-> "))
                self.__lista.append(idade)
            self.__lista.sort()
            print("")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número inteiro.")

    def mostraMediana(self):
        print(f"Mediana: {np.median(self.__lista)}")

    def mostraMenor(self):
        print(f"Menor: {self.__lista[0]}")

    def mostraMaior(self):
        print(f"Maior: {self.__lista[len(self.__lista)-1]}")

    def __str__(self):
        for id, item in enumerate(self.__lista):
            print(f"{id+1}: {item}")

def main():
    nomes = ListaNomes()
    datas = ListaDatas()
    salarios = ListaSalarios()
    idades = ListaIdades()

    listaListas = [nomes, datas, salarios, idades]

    for lista in listaListas:
        lista.entradaDeDados()
        lista.mostraMediana()
        lista.mostraMenor()
        lista.mostraMaior()
        print("___________________")

    print("Fim do teste!!!")

if __name__ == "__main__":
    main()