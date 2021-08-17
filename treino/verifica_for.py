def verifica():
    l = [1, 2, 3]
    for x in l:
        print(x)  # o 'i' é o elemento da lista

def ver_2():
    s = 'algoritmos'
    for c in s:
        if c in 'aeiou':
            print(c) # o 'i' é o caracter da string

def ver_1():
    L =['cão', 'gato', 'coelho']
    for i in L:
        print(i)  # o 'i' é o elemento da lista

def ver_3():
    a = ['a', 'b', 'c']
    for i in range(len(a)):
        print(a[i])  # o 'i' é o indice da lista

def acumulador():
    acum = 0
    for x in range(1, 100):
        if x % 2 == 0:
            acum = acum + x
    print(acum)

def aninhados():
    str_lst = ['João', 'Roberto', 'Rafael']
    for nome in str_lst:
        for c in nome:
            if c in 'aeiou':
                print(c)

def ver_4():
    lst = range(10)
    for x in lst:
        print(lst[x])



"""verifica()
ver_1()
ver_2()
ver_3()
acumulador()
aninhados()"""
ver_4()

