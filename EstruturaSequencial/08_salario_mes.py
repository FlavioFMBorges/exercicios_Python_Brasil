def salario_mes():
    """
    Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
    Calcule e mostre o total do seu salário no referido mês.
    1 - Peça o valor do salário do usuário por hora
    2 - Peça o número de horas trabalhadas no mês
    3 - Multiplique o salário pelas horas e depois por 30 dias
    4 - retorne para a função o salário do mês
    5 - chame a função

    :return: float
    """
    salario_hora = float(input("Digite o valor do seu salário por hora em reais: R$"))
    horas_trabalhadas = float(input("Digite a quantidade de horas trabalhadas no dia: "))
    sal_horas_trab = salario_hora * horas_trabalhadas
    salario_mes = sal_horas_trab * 30
    return print(f"O seu salário no mês é R$ {salario_mes}")

salario_mes()
