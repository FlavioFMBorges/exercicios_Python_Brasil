def metro_cm():
    """
    Faça um Programa que converta metros para centímetros
    :return: inteiro
    1 - receber um valor
    2 - valor e dividir por 100
    3 - mostrar o valor achado
    4 - chamar a função no corpo do programa
    """
    metro = eval(input("Digite um valor em metros: "))
    cm = metro*100
    return print(f"{metro} metros tem {cm} centímetros")

metro_cm()
