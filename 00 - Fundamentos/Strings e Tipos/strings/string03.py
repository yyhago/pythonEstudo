# Manipulação de strings com slicing
nome = "Yhago Felipe Desenvolvedor"

print(nome[0])  # Primeiro caractere
print(nome[-2])  # Penúltimo caractere
print(nome[:9])  # Primeiros 9 caracteres
print(nome[10:])  # A partir do índice 10 até o final
print(nome[10:16])  # Caracteres do índice 10 ao 15
print(nome[10:16:2])  # Caracteres do índice 10 ao 15, pulando de 2 em 2
print(nome[:])  # String completa
print(nome[::-1])  # String invertida