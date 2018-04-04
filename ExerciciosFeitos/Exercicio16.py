"""
 16 - Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
      Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.
      Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
"""
#import math

area = int(input("Digite quantos metros quadrados tem a àrea a ser pintada:"))

litroTintaUsada = area/3

#latas = math.ceil(litroTintaUsada/18)

completar = (litroTintaUsada/18)

comp = ( completar * 100)

resto = 10 - comp

latas = (resto/10) + (comp/10)

total = latas * 80.00


print("Será necessário comprar ",latas,"(s) Dando um total de R$",total)