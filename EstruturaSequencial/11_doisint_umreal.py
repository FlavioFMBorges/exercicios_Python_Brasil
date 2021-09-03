def doisint_umreal():
    """
    Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
1 - o produto do dobro do primeiro com metade do segundo.
2 - a soma do triplo do primeiro com o terceiro.
3 - o terceiro elevado ao cubo.
    """
    n_inteiro_1 = int(input("Digite o primeiro número inteiro: "))
    n_inteiro_2 = int(input("Digite o segundo número inteiro: "))
    n_real = float(input("Digite o número real: "))
    dobro = n_inteiro_1 * 2
    metade_segundo = n_inteiro_2 / 2
    prod_dobro = dobro * metade_segundo
    print(f"O produto do dobro do primeiro com metade do segundo é {prod_dobro}")
    triplo = n_inteiro_1 * 3
    soma_triplo = triplo + n_real
    print(f"A soma do triplo do primeiro com o terceiro {soma_triplo}")
    el_cubo = n_real ** 3
    print(f"O terceiro elevado ao cubo {el_cubo}")

doisint_umreal()

