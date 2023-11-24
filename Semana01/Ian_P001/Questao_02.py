#Funcionamento dos operadores em Pyhton
import math
print("Apresentando os Operadores Aritméticos para a = 5 e b = 2:\n")
a = 5
b = 2
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

#Principais diferença em relação C/C++
#Python possui tipagem dinâmica, ou seja, não é necessário declarar uma variável antes de utilizá-la.
'''
Em C/C++ os números inteiros tem um limite máximo, pois são limitados pelo tipo (int, long, ...). 
Em python não tem esse problema
'''
#Python tem o operador de exponenciação. Em C/C++ tem usar a função pow()

print("Calculando o fatorial de 30:")
fatorial = math.factorial(30)
print("Fatorial de 30 = ", fatorial)


#Imutabilidade das variáveis em python
print("Imutabilidade das variáveis\nConsidere c=2")
print("É feito 'd=c', ou seja, d recebe o mesmo valor que c")
print("Ao mudar o valor de c fazendo 'c=3', o valor de d não é alterado")
c = 2
d = c
c = 3
print("Valor de c = ", c)
print("Valor de d = ", d)

#Métodos disponíveis para variáveis inteiras em python
print("\n Lista de métodos disponíveis para variáveis inteiras em pyhton")
e = 1
print("\n".join(dir(e)))