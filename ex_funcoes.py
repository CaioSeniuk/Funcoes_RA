#Pegar 3 valores e retornar o maior deles

def pegar_maior(listaValores): #parametro
    maior = 0
    for num in listaValores:
        if num>maior:
            maior = num
    return maior   

lista = [7,10,5]
maior_valor = pegar_maior(lista)
print(f"\nO maior valor é: {maior_valor}\n")
