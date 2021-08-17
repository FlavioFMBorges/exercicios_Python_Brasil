def nfat(L):
    n = 0
    fat = 1
    while fat <=L:
        n += 1
        fat *= n
    return n - 1

def num_correto():
    num = eval(input('Digite um número positivo: '))
    while num < 0:
        num = eval(input("Por favor digite um número positivo: "))

def lista_vazia():
    l = []
    nome = input("Digite um nome: ")
    while nome != '':
        l.append(nome)

"""print(nfat(3))
"""
num_correto()
