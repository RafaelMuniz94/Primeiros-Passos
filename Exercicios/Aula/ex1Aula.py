# fibonacci
# 1,1,2,3,5,8 ....
# Resolver de forma Recursiva:



def fibonacci(numero):
	if numero == 1 or numero == 2:
		return 1
	return fibonacci(numero - 1) + fibonacci(numero - 2)



#print(fibonacci(6))

resposta = []
numero = 8

for p in range(1,numero + 1):
	resposta.append(fibonacci(p))

print(resposta)
