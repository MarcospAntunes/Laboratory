from tkinter import *

def calcula_imc(peso: Entry, altura: Entry):
    try:
      imc = 0
      imc = float(peso.get()) / (float(altura.get())) ** 2
      resultado["text"]= f"o seu IMC é {imc}"
    except:
       resultado["text"] = "Valores invalidos."

    return imc

janela = Tk()
janela.title("Calculadora de IMC")
frame = Frame(janela, padx=40, pady=40).grid(column=0, row=0)

Label(frame, text="Para saber seu IMC, digite os valores abaixo.", justify="center").grid(column=0, row=1, columnspan=3)
Label(frame, text="Qual o seu peso em Kg?").grid(column=1, row=2)
peso = Entry(frame)
peso.grid(column=2,row=2)
Label(frame, text="Qual a sua Altura em metros?").grid(column=1, row=3)
altura = Entry(frame)
altura.grid(column=2, row=3)
Button(janela, text="Calcular", justify="center", command=lambda: calcula_imc(peso, altura)).grid(column=2, row=4)
resultado = Label(frame)
resultado.grid(column=1, row=5, columnspan=2)

janela.mainloop()