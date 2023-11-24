#Tópico 1
# #Funcionamento dos operadores em Pyhton para ponto flutuante
import math
print("Apresentando os Operadores Aritméticos para a = 5 e b = 2:\n")
a = 5.1
b = 2.2
#Adição
adicao = a + b
print("Adição = ", adicao)

#Subtração
subtracao = a - b
print("Subtração = ", subtracao)

#Multiplicação
multiplicao = a*b
print("Multiplicação =", multiplicacao)


#Divisão real - Realiza divisão de ponto flutuante
divisao = a/b
print("Divisão real = ", divisao)

#Módulo
modulo = a%b
print("Módulo = ", modulo)

print("\n\nNovidades em realação a C/C++:\n")
#Exponenciação
exponenciacao = a**b
print("Exponenciação = ", exponenciacao)

#Unário negativo
unario = -a
print("Unário negativo = ", unario)

#Divisão truncada
divisaoT = a//b
print("Divisão truncada = ", divisaoT)

print("\n\nOperadores aritméticos compostos:\n")
print(a+=b)
print(a-=b)
print(a*=b)
print(a/=b)
print(a//=b)
print(a%=b)
print(a**=b)
print(a**=b)

#Tópico 2
menor = 2.0 ** -1022  
maior = (2.0 ** 1023) * (1.0 - (2.0 ** -52))

print(f"\nMenor potência de 2 representável: {menor}")
print(f"Maior potência de 2 representável: {maior}")

#Tópico 3
#Imutabilidade das variáveis em python com ponto flutuante
print("Imutabilidade das variáveis\nConsidere c=2.5")
print("É feito 'd=c', ou seja, d recebe o mesmo valor que c")
print("Ao mudar o valor de c fazendo 'c=3.4', o valor de d não é alterado")
c = 2.5
d = c
c = 3.4
print("Valor de c = ", c)
print("Valor de d = ", d)

#Tópico 4
#Métodos disponíveis para variáveis inteiras em python
print("\n Lista de métodos disponíveis para variáveis ponto flutuante em pyhton")
e = 1.2
print("\n".join(dir(e)))