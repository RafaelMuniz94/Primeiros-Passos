#Classes são objetos com propriedades e métodos semelhantes

class Pessoa:

	def __init__(self,nome,idade,peso): # Construtor do objeto
		self.nome = nome
		self.idade = idade
		self.peso = peso


	def retornarPessoa(self):
		pessoa = "Nome: ",self.nome," Idade: ",self.idade," Peso: ",self.peso
		return pessoa

	def setNome(self,nome):
		self.nome = nome



pessoa1 = Pessoa("Rafael",23,110)

print(pessoa1.retornarPessoa())
pessoa1.setNome("Rodrigo")

print(pessoa1.retornarPessoa())