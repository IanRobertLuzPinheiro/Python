#Imprime o caractere e seu código
for i in range(10):
    print("Caractere:" + str(chr(ord('0') + i)) + " - Código Numérico:" + str(ord('0') + i))

#Imprime o caractere e seu código em octal e hexadecimal
for i in range(10):
    decimal = ord('0') + i
    octal = oct(decimal)
    hexadecimal = hex(decimal)

    print("Caractere:" + str(chr(ord('0') + i)) + " - Código Decimal:" + str(decimal) + " - Código Octal:" + str(octal) + " - Código Hexadecimal:" + str(hexadecimal))

valor = input("Digite um valor: ")
FormaDecimal = ord(valor)
FormaOctal = oct(FormaDecimal)
FormaHexadecimal = hex(FormaDecimal)
print(f"Código Decimal: {FormaDecimal} | Código Octal: {FormaOctal} | Código Hexadecimal: {FormaHexadecimal}")

#Caracteres especiais
#Em Python é possível utilizar os caracteres especiais como quaisquer outros
#Python manipula automaticamente a representação Unicode.
#É possível utilizar o mesmo código anterior para caracteres especiais
#Uso dos caracteres especiais
cedilha = 'ç'
til  = 'ã'
print(f"\nCaracteres especiais:\n'{cedilha}' - {ord(cedilha)}")
print(f"'{til}' - {ord(til)}")