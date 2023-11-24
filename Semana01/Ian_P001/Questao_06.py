#Primeira Parte
L = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(L[::-1])   # Mostra a lista do último ao primeiro termo
print(L[-1::])   # Mostra o último elemento
print(L[:-1:])   # Exclui o último elemento
print(L[::-2])   # Mostra a lista do último ao primeiro termo, mas "pulando" um termo
print(L[-2::])   # Mostra os dois últimos elementos
print(L[:-2:])   # Exclui os últimos dois elementos

#Segunda Parte
signos = ['Macaco', 'Galo', 'Cão', 'Porco', 'Rato', 'Boi', 'Tigre', 'Coelho', 'Dragão', 'Serpente', 'Cavalo', 'Carneiro']
ano = int(input("Digite seu ano de nascimento:"))
seu_signo = signos[ano%12]
print("Seu signo é :",seu_signo)