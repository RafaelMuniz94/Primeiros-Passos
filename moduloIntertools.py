'''
Conjunto de ferramentas poderosa

'''

from itertools import permutations
from itertools import combinations




def escrever(nome,palavra):
	nome = nome +'.txt'
	arquivo = open(nome,'a+')
	arquivo.write(palavra +  '\n')
	arquivo.write('==============================================\n')
	arquivo.close()



lista  = [1,2,3,4,5,6,7,8,9,10]

'''
for p in permutations(lista):
	print(p)
'''

qtd = 0
for p in permutations(lista):
	qtd = qtd + 1

print(qtd)


letras = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','w','u','v','x','y','z')
numeros = ('0','1','2','3','4','5','6','7','8','9')

#letras = ('a','b')
#numeros = ('1','2')

'''

Código perigoso, ele vai rodar até tentar todas as combinações possiveis das tuplas
de letras e números
for le in permutations(letras):
		for num in permutations(numeros):
			palavra = ''
			palavra = palavra.join(le)
			palavra = palavra.join(num)
			escrever(palavra)
'''



for combo in combinations(letras,6):
	palavra = ''
	palavra = palavra.join(combo)
	escrever('letras',palavra)


for combo in combinations(numeros,6):
	palavra = ''
	palavra = palavra.join(combo)
	escrever('numeros',palavra)