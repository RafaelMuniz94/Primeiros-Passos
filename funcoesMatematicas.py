#Para importar basta usar o comando import + nome do pacote
import math

#O comando ceil retorna o menor valor inteiro maior ou igual ao número nao inteiro passado
#print(math.ceil(float(input("Digite um número: "))))

print(math.ceil(6.3))


#O comando fabs retorna o valor absoluto de um número

print(math.fabs(-3))

#O comando factorial retorna o a funcao fatorial de um número


print(math.factorial(10))

#O comando floor retorna o inteiro menor ou igual ao passado

print(math.floor(3.6))

#O comando exp faz o exponencial neperiano

print(math.exp(5))

#O comando log, retorna um logaritimo na base e

print(math.log(3))

#Caso queira mudar a base do logaritimo, o comando fica assim:
#Base 2
print(math.log2(2))
#Base 10
print(math.log10(10))


#É possivel realizar exponenciação com o comando pow

print(math.pow(2,3))

#É possível realizar raiz quadrada com o comando sqrt

print(math.sqrt(2))

#É possivel realizar seno com o comando sin e cosseno com o comando cosseno

print("seno 10: ",math.sin(10))
print("cosseno 10: ",math.cos(10))



#Existem as constantes PI e e napieriano

print("PI: ", math.pi)
print("e: ",math.e)