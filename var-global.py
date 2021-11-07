#
# Variável global e funções
#
nome = "Gustavo"
sobrenome = "Hammes"


def escrevenome():
    return nome, sobrenome


def alteraglobal():
    # Declara a variável global 
    global sobrenome  # comparando com o #this-> do PHP
    # Altera a variável global
    sobrenome = "Melo"
    return nome, sobrenome


print(f'\n Função escrevenome: {escrevenome()}')
print(f'\n Variáveis globais (nome e sobrenome): {nome}, {sobrenome}')
print(f'\n Função alteraglobal: {alteraglobal()}')
print(f'\n Variáveis globais (nome e sobrenome): {nome}, {sobrenome} \n')
