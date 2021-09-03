def dobro_area():
    """
    Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
    :return: float
    1 - área do quadrado (A = l ** 2)
    2 - Pedir para o usuário o tamanho do lado do quadrado
    3 - Calcular o dobro da area
    4 - Mostrar retorno para o usuário
    5 - Chamar a função para mostrar para o usuário
    """
    lado = float(input("Digite o tamanho do lado do quadrado: "))
    area = lado ** 2
    area *= 2
    return print(f"O dobro da área do quadrado é {area}")

dobro_area()
