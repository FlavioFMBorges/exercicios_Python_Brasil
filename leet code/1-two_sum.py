"""class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Dado um array de números inteiros e um alvo inteiro, retorna os índices dos dois números de forma que eles se somam ao alvo.

Você pode presumir que cada entrada teria exatamente uma solução e não pode usar o mesmo elemento duas vezes.

Você pode retornar a resposta em qualquer ordem.

1 - pegar os numeros para a lista
2 - percorrer a lista e ver qual numero somado que da o valor do alvo
3 - guardar o valor do indice em duas variaveis
4 - retornar o valor dos indices

aprender tabela hash para este proble

nums = int(input("Write integers numbers: "))


lista de tamanho máximo(ver vídeos de entrevista)

"""
def twoSum():
    nums = [2, 7, 11, 15]
    target = 9
    list = []
    for number in nums:
        print(nums.index(number))
        list.append(nums.index(number))
        return print(list)

twoSum()