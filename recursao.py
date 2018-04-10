'''
Fatorial 
0! = 1
3! = 3 * 2 * 1 = 6
4! = 4 * 3 * 2 * 1 = 24

Não é possivel obter o fatorial de 1000
'''


def fatorial(numero):
	if numero == 0:
		return 1
	return numero * fatorial(numero - 1)



print(fatorial(0))
print(fatorial(1))
print(fatorial(4))
print(fatorial(100))