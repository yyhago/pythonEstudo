print("String 01 | Python")

# Input de entrada de valores para o usuário
#   nome = input("Insira seu nome:")
#   idade = input("Insira sua idade:")

# Saida com 'end' onde adiciona no final '...'
#   print(nome, idade, end="...\n")

# Saida com 'end' e com o 'sep' onde separa valores pela string escrita, exemplo no código: '#'
#   print(nome, idade, sep="#", end="...\n")

# -------------------------------------------------------------------------------------------------------------

#   nome = "Yhago Felipe"

#   print(nome.upper()) <- Formata o texto para maiúsculo
#   print(nome.lower()) <- Formata o texto para minúsculo
#   print(nome.title()) <- Formata o texto deixando sempre a primeira letra de cada palavra maiúsculo

# -------------------------------------------------------------------------------------------------------------

#   texto = "  Olá mundo!    "

#   print(texto + ".") <- Ao final do 'texto' adiciona o '.'
#   print(texto.strip() + ".") <- Ao final do 'texto' adiciona o '.' porém removendo todos espaços
#   print(texto.rstrip() + ".") <- Ao final do 'texto' adiciona o '.' porém não remove os espaços
#   print(texto.lstrip() + ".") <- Deixa o 'texto' na extremidade da esquerda removendo o espaço e joga o ponto para o outro extremo

# -------------------------------------------------------------------------------------------------------------

#   menu = "Python"

#   print("####" + menu + "####") <- Junta a string '#' com o 'menu'
#   print(menu.center(14)) <- Deixa o 'menu' no centro, porém ocupando 14 posições
#   print(menu.center(14, "#")) <- Deixa o 'menu' no centro, porém ocupando 14 posições com as strings '#'
#   print("-".join(menu)) <- Separa letra por letra do 'menu' pela string '-' 