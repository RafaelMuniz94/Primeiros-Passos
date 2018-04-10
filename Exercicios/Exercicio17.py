"""
    17 - Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
    Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
            Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
            a. comprar apenas latas de 18 litros;
            b. comprar apenas galões de 3,6 litros;
            c. misturar latas e galões, de forma que o preço seja o menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

"""

def definirMenorPreco(litros):

    quantidadeLatas = int(litros/3.6) + 1
    quantidadeGaloes = int(litros/18) + 1

    total = (quantidadeLatas * 3.6) + (quantidadeGaloes * 18)
    precoL = quantidadeLatas * 25
    precoG = quantidadeGaloes * 80

    while total > litros:
        if precoG > precoL:
           quantidadeGaloes = quantidadeGaloes - 1
        else:
            quantidadeLatas = quantidadeLatas - 1

        precoL = quantidadeLatas * 25
        precoG = quantidadeGaloes * 80

        totalAtual = (quantidadeLatas * 3.6) + (quantidadeGaloes * 18)

        if totalAtual > litros:
            total = totalAtual
        else:
            break

    resposta = (quantidadeGaloes,quantidadeLatas)

    return resposta





area = int(input("Digite o tamanho em metros quadrados da área que será pintada: "))
litrosUsados = area/6

latas = 0
if litrosUsados % 18 == 0:
    latas = litrosUsados/18
else:
    latas = int(litrosUsados/18) + 1

total = latas * 80

print("Devem ser compradas ",latas," latas, totalizando R$ ",total)

galoes = 0

if litrosUsados % 3.6 == 0:
    galoes = litrosUsados/3.6
else:
    galoes = int(litrosUsados/3.6) + 1


    total = galoes * 25

print("Devem ser comprados ",galoes," galões, totalizando R$ ",total)

"""
latas = litrosUsados/18

galoes = int((litrosUsados - latas)/3.6) + 1

total = (latas * 80) + (galoes * 25)

"""

t = definirMenorPreco(litrosUsados)

galoes = t[0]
latas = t[1]

total = (galoes * 80) + (latas * 25) + (total * 0.01)

print("Devem ser compradas ",latas," latas e ",galoes," galões totalizando R$ ",total)