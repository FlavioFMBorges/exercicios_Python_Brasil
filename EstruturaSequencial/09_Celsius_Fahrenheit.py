def celsius_Fahrenheit():
    """
    Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
C = 5 * ((F-32) / 9).

    1 - Pedir a temperatura em Fahrenheit
    2 - Aplicar a fórmula para transformar em Celsius
    3 - retornar o valor de Celsius
    4 - Chamar a função
    """
    f = float(input("Digite uma temperatura em Fahrenheit: "))
    c = 5 * ((f - 32) / 9)


#    c2 = f - 32
#    c1 = c2 / 9
#    c = 5 * c1
    return print(f"o valor em Celsius é: {c}")

celsius_Fahrenheit()
