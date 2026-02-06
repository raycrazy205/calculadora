# importando tkinter
from tkinter import *
from tkinter import ttk

# cores

cor1 = "#3b3b3b"  # preta
cor2 = "#feffff"  # branca
cor3 = "#38576b"  # azul
cor4 = "#ECEFF1"  # cinzanta
cor5 = "#FFAB40"  # laranja


janela = Tk()
janela.title("Calculadora")
janela.geometry("235x318")
janela.config(bg=cor1)



# cirando frames
frame_tela = Frame(janela, width=235, height=50, bg=cor3)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=235, height=268)
frame_corpo.grid(row=1, column=0)

# criando botoes

b_1 = Button

janela.mainloop()
