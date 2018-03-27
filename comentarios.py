
# Comentario de uma linha usar o #

def fib(n):
	if n == 1 or n ==2:
		return 1
		# Vale notar que para o else funcionar a identação dele teve que ser 
		# perfeita, ou seja ele teve que estar alinhado fora do if
	return fib(n-1) + fib(n - 2)


#Comentario de varias linhas usar o '''

'''

def fib(n):
	if n == 1 or n ==2:
		return 1
	return fib(n-1) + fib(n - 2)

'''


print(fib(3))
print(fib(4))
print(fib(5))
print(fib(6))