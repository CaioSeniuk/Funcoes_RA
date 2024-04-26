#Exercício 1: Imprimir Nome
#Definição da função como bloco

"""def imprimir_nome():
    nome = str(input("\nInforme o seu nome: "))
    print(f"O nome é: {nome}\n")
imprimir_nome()"""

#Definição da função com parâmetro
"""def imprimir_nome(nome):
    print(f"\nO nome é: {nome}")

n = input("\nInforme o seu nome: \n")
imprimir_nome(n)"""

#Função para pedir nome
def pedir_nome():
    nome = input("\nInforme o nome: ")
    return nome

 #Atribuir à uma variável quando usar return
print(f"\nO nome é: {pedir_nome()}")



