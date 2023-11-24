#Tópico 1
nome_completo = "Ian Robert Luz Pinheiro"

#Tópico 2
separar = nome_completo.split()
primeiro_nome = separar[0]
sobrenome = separar[-1]
print(f"Nome: {primeiro_nome} {sobrenome}")

#Tópico 3
ordenar= sorted([primeiro_nome, sobrenome])
a = ordenar[0]
b = ordenar[1]

print(a, b)

#Tópico 4
tamanho_nome = len(primeiro_nome)
tamanho_sobrenome = len(sobrenome)
print(tamanho_nome, tamanho_sobrenome)

#Tópico 5
palindromo = primeiro_nome[::-1]

print(palindromo)

if(primeiro_nome == palindromo):
    print("É palindromo")
else:
    print("Não é palindromo")
