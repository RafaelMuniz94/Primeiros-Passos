'''
potencia
2 ** 3 = 2 * 2 * 2 = 8
2 ** 0 = 1
'''



def potencia(numero,expoente):
	if expoente == 0:
		return 1
	return numero * potencia(numero, expoente - 1)




print(potencia(1000,0))

print(potencia(2,256))