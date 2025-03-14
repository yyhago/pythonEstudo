nome_programador = "Yhago Felipe"  # String
idade_programador = 18  # Int
altura_programador = 1.67  # Float
saldoconta_programador = 23.233  # Float

PROGRAMA_PYTHON = True  # Boolean
stacks = {"Python": "Full Stack", "Javascript": "Front-End", "Java": "Back-End", "Anos_Programando": 5}  # Dicionário

# Os '%s' e '%d' são placeholders no estilo C, onde '%s' representa uma string e '%d' um número inteiro
print("Nome: %s - Idade: %d" % (nome_programador, idade_programador))

# Método format(), onde '{}' são placeholders substituídos pelos valores passados na função format
print("Nome: {} - Idade: {}".format(nome_programador, idade_programador))

# Os índices podem ser especificados dentro das chaves
print("Nome: {1} - Idade: {0}".format(nome_programador, idade_programador))
print("Nome: {1} - Idade: {0} - Nome: {1} {1}".format(nome_programador, idade_programador))

# Podemos usar nomeação de variáveis dentro do format
print("Nome: {nome} - Idade: {idade}".format(nome=nome_programador, idade=idade_programador))
print("Nome: {name} - Idade: {age} - {name} {name} {age}".format(name=nome_programador, age=idade_programador))

# Acessar valores do dicionário stacks
print(f"Stack: {stacks['Python']} - Experiência: {stacks['Anos_Programando']} anos")

# A melhor e mais moderna forma: f-strings (Python 3.6+)
print(f"Nome: {nome_programador} - Idade: {idade_programador}")

# Formatando floats com f-strings
print(f"Nome: {nome_programador} - Idade: {idade_programador} - Saldo: {saldoconta_programador:.2f}")  # Duas casas decimais
print(f"Nome: {nome_programador} - Idade: {idade_programador} - Saldo: {saldoconta_programador:10.1f}")  # Espaçamento de 10 caracteres, 1 casa decimal
