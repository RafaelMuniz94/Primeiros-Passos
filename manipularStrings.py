#São representadas por aspas duplas ou simples

aspasDuplas = "''"
aspasSimples = '""'

print(aspasSimples)
print(aspasDuplas)

# É possível acessar os caracteres de uma string como se buscasse um valor em um array

textao = "É possível acessar os caracteres de uma string como se buscasse um valor em um array"

print("Primeira letra: ",textao[0])
print("Segunda letra: ",textao[1])
print("Terceira letra: ",textao[2])
print("Ultima letra: ",textao[-1])

#É possivel transformar strings em listas

lista = list(textao)

print(lista)

#Com isso é possivel modificar os valores da lista

lista[1] = 'X'
lista[2] = 'X'
lista[4] = 'X'
lista[7] = 'X'

#para unir a string novamente:

textao = ''.join(lista)

print(textao)

#É possivel descobrir o tamanho de uma string com a função len

print(len(textao))



nome = "Rafael"

lista = []
for letra in range(len(nome),0,-1):
	lista.append(nome[letra-1])	

nome = ''.join(lista)

print(nome)