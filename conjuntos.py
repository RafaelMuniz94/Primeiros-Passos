#Conjuntos (set) são estruturas de dados que não permitem elementos repetidos
#não é ordenado;

conjunto = {2,2,20,'marcos','rafael', 'marcos'}

print(conjunto)


#É possível transformar listas em Conjuntos

lista = [1,2,1,3,5,4,2,6]

conjunto2 = set(lista)

print(conjunto2)

#Para adicionar valores á um conjunto basta utilizar o metodo add

conjunto.add(3)

#conjunto2.add(conjunto) -- Isso não funciona

print(conjunto)
print(conjunto2)

print(type(conjunto))
print(type(conjunto2))