'''
TKinter é o módulo de interface gráfico padrão do python,
ele já vem instalado no python para windows
'''


from tkinter import *
from tkinter import messagebox


def clique_btn():
	msg = messagebox.showinfo("Clicou no botão", "Seja bem vindo(a)")



t = Tk() # Cria a instancia do módulo tkinter
t.geometry('800x600') # define o tamanho da janela a ser criada
btn = Button(t, text = "Clique", command = clique_btn) #cria um botão passando a instancia onde deverá ficar, o texto que irá mostrar e o método a ser executado

btn.place(x = 400, y = 300) # Insere o botão na interface nas coordenadas x e y

t.mainloop() #Coloca em loop a interface, para que ela espere por eventos de tela