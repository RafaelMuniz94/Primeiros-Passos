"""
Dicionários são o hashmap do python
Assim como os conjuntos, ele utiliza chaves( {} ) como representação,
porém é formado de um par de chave e valor
"""

dicionario = {'rafael':23,
			  'karen': 24,
			  'dimitri':18}


print(dicionario['rafael'])

print(dicionario['karen'])

print(dicionario['dimitri'])

#É possível vericar o valor das chaves com:

print(dicionario.keys())

#Para deletar basta:

del dicionario['dimitri']

print(dicionario)

#É possível descobrir se alguma chave está no dicionario com:

print('rafael' in dicionario)
print('dimitri' in dicionario)

#É possível descobrir os valores do dicionário sem ter que passar as chaves:

print(dicionario.values())