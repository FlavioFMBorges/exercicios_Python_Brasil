def area_circulo():
    """
    Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
    1 - como calcular a area de um circulo. A = π r²
    2 - Estabelecer constante do Pi como 3,14
    3 - Receber o valor do raio
    4 - Fazer a conta do raio ao quadrado
    5 - Multiplicar o valor de Pi pelo raio ao quadrado e quardrado em area
    6 - retornar o valor da área para a função
    7 - Chamar a função

    :return: float
    """
    pi = 3.14
    raio = float(input("Digite o valor do raio em mm : "))
    raio_quadrado = raio ** 2
    area = pi * raio_quadrado
    return print(f"O valor da área do círculo é {area}")  # area = pi 25



area_circulo()
