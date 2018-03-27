#Função para abrir o arquivo, caso esteja na mesma pasta o primeiro parametro é apenas o nome
# o segundo parametro é o tipo de operação: 
# 'r' - Read(leitura)
# 'w' - Write(escrita)


arquivo = open("funcoesMatematicas.py","r")
print(arquivo.read())
arquivo.close()

print("====================================================================")
#Outra forma de ler um arquivo é com o uso do with

with open('variaveis.py','r') as file:
	print(file.read())
file.close()


#Para escrever um arquivo o processo é semelhante, porém passa-se o parametro w

arquivo = open("arquivo.txt",'w')
arquivo.write("Python sangue bom")
arquivo.close()


with open("arquivo2.txt","w") as file2:
	file2.write("Novamente sangue bom")
	file2.close()