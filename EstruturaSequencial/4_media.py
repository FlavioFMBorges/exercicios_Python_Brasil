def media_notas():
    """
    Faça um Programa que peça as 4 notas bimestrais e mostre a média.
    1 - pedir notas
    2 - somar notas
    3 - dividir pela quantidade de notas
    4 - mostrar a média
    """
    soma = 0
    lista = []
    while True:
        nota = eval(input("Digite uma nota e 0 para a media: "))
        lista.append(nota)
        if nota == 0:
            break

    for x in lista:
        soma += x

    media = soma/4
    return print(f"A média das notas é: {media}")


media_notas()