#Exemplo de um método que será chamado pela criacao de Módulo

if __name__ == '__main__':
	print("Esse módulo está sendo executado")
else:
	print("Esse módulo está sendo importado")

def media(n1,n2):
	media = (n1 + n2)/2
	return media

def multiplicacao(n1,n2):
	mult = n1 * n2
	return mult

def potencia(n1,n2):
	pot = n1 ** n2
	return pot