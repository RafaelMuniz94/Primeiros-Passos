# Criar uma recursão para saber se um número é primo ou não
# Primos são divisiveis apenas por 1 e por ele mesmo

def descobrirPrimo(numero, idx):
	divisoes = []
	if idx > 0:
		if numero%idx == 0:
			divisoes.append(idx)
		return descobrirPrimo(numero, idx - 1)
	else:
		return divisoes



def printar(numero):
	divisoes = descobrirPrimo(numero,numero)

	if(len(divisoes) > 2):
		print("O ",numero," não é primo")
	else:
		print("O ",numero," é primo")


# for p in range(1,42):
# 	printar(p)


printar(4)