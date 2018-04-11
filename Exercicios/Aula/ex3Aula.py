#verificar se um número é par:


def verificarPar(numero):
	if numero / 2 == 1 or numero == 0:
		return True
	else:
		return False
	return verificarPar(numero/2)






def resp(valor):
	if verificarPar(valor):
		print(valor, "é Par")
	else:
		print(valor, "é Inpar")



resp(0)
resp(1)
resp(2)
resp(3)
resp(4)
resp(5)
resp(6)
resp(7)
resp(8)
resp(9)
resp(10)


