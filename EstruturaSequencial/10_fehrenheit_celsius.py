def fah_celsius():
    """
    Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit
    C = 5 * ((F-32) / 9)
    (C × 9/5) + 32 = 35,6 °F
    1 - Peça a temperatura em graus Celsius
    2 - transformar em Fahrenheit
    3 - retornar o Fahrenheit para a função
    4 - Chamar a função
    """
    celsius = float(input("Digite a temperatura em graus Celsius: "))
    fahrenheit = celsius * (9 / 5) + 32
    return print(f"{celsius}°C equivalem a {fahrenheit}°F")

fah_celsius()
