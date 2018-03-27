#Listas, forma simples de estrutura de dados
#Os elementos devem estar dentro de conchetes [] para identificar que são listas
#Listas podem possuir tipos diferentes de dados
#O index começa em zero, Graças a Deus




lista1 = [1,2,3,4,5,6]
print("Lista homogenea: ",lista1)

lista2 = [1,2,3,"Rafael","Karen", 1.5,2.6,True,False]
print("Lista heterogenea: ",lista2)


print(lista1[2])
print(lista2[3])


#Inserir elementos em uma lista
#Comando append insere ao final

lista1.append("3")
print(lista1)

#Para acessar o ultimo elemento de uma lista, basta buscar por ela na posição -1

print(lista2[-1])

#Para contar os elementos da lista basta passa-la como parametro na função len


print("Tamanho da lista 1: ",len(lista1))
print("Tamanho da lista 2: ",len(lista2))


#É possivel extender uma lista com elementos de outra, com o comando extend

lista1.extend(lista2)

print(lista1)

#É possivel adicionar elementos em pontos aleatórios de uma lista, com o comando 
#insert

lista2.insert(3,"LoL")

print(lista2)

#É possivel criar uma lista vazia

listaVazia = []

print(listaVazia)


#Para remover um elemento basta passar qual elemento (valor) é para a função remover

listaVazia.append("Cirex")
listaVazia.append("Duck Dodgers")
listaVazia.append("Teixeira")

listaVazia.insert(2,3.2)

print(listaVazia)

listaVazia.remove(3.2)

print(listaVazia)

#Para remover pela posição basta usar o comando pop

listaVazia.pop(2)

print(listaVazia)

#Para limpar a lista basta usar o comando clear

listaVazia.clear()

print(listaVazia)

#É possivel retornar um index com o comando index

print(lista1.index("Karen"))

#O comando count("valor a ser contado") retorna a quantidade de elementos repetidos
#na lista
print("Lista1: ", lista1)
print(lista1.count(1))

#Caso utilizar um count(1), ele irá considerar True para o calculo