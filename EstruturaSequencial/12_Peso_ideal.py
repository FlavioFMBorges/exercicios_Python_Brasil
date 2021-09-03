def peso_ideal():
    """
    Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal,
    usando a seguinte fórmula: (72.7*altura) - 58
    1 - Pedir altura
    2 - usar fórmula
    3 - retornar peso
    4 - Chamar função
    """
    altura = float(input("Digite sua altura: "))
    peso = (72.7 * altura) - 58
    return print(f"O seu peso ideal é {peso:.2f} quilos")

peso_ideal()