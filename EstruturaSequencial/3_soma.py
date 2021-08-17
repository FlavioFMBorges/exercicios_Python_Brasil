def soma_numeros():
    """
    Faça um Programa que peça dois números e imprima a soma.
    :return: inteiro
    1 - Pedir para o usuário digitar um número e repetir o passo
    2 - somar os valores e colocar em uma variável
    3 - retornar o valor para a função
    4 - chamar a função
    """
    numero_1 = eval(input("Digite o primeiro valor: "))
    numero_2 = eval(input("Digite o segundo valor: "))
    soma = numero_1 + numero_2

    return print(f"A soma dos valores é {soma}")

soma_numeros()
