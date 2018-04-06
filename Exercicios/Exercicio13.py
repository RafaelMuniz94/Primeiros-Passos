"""
13 - Tendo como dados de entrada a altura e o sexo de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
        a. Para homens: (72.7*h) - 58
        b. Para mulheres: (62.1*h) - 44.7 (h = altura)
        c. Peça o peso da pessoa e informe se ela está dentro, acima ou abaixo do peso.

"""



def pesoIdeal(sexo,altura):
    peso = 0
    if sexo == 'M' or sexo == 'Masculino' or sexo == 'm' or sexo == 'masculino':
            peso = (72.7 * altura) - 58
    elif sexo == 'F' or sexo == 'Feminino' or sexo == 'f' or sexo == 'feminino':
        peso = (62.1 * altura) - 44.7
    else:
        print("Digite um sexo válido (Masculino ou Feminino!")

    return peso


altura = float(input("Digite sua altura: "))
sexo = input("Digite o seu sexo: ")

ideal = pesoIdeal(sexo,altura)

if ideal > 0:
    print("Seu peso ideal é: ",ideal," Kg.")