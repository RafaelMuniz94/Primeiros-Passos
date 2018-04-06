"""
11 - Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
        a. o produto do dobro do primeiro com metade do segundo .
        b. a soma do triplo do primeiro com o terceiro.
        c. o terceiro elevado ao cubo.
"""


a = int(input("Digite o valor A: "))
b = int(input("Digite o valor B: "))
c = float(input("Digite o valor C: "))


resp1 = (2 * a)*(b/2)

resp2 = (3 * a) + c

resp3 = c ** 3

print("O produto do dobro do primeiro com metade do segundo: ",resp1)

print("A soma do triplo do primeiro com o terceiro: ",resp2)

print("O terceiro elevado ao cubo: ",resp3)
