import tkinter as tk
import random

root = tk.Tk()
root.title('Par ou Ímpar')
root.resizable(False, False)
root.geometry('600x400')

labelTitle = tk.Label(root, font=("Arial", 12), text='Par ou Ímpar')
labelTitle.pack(pady=10)

vidas = 3
pontos = 0

def parOuImpar(aposta):
  global vidas, pontos

  number = random.randint(0, 201)
    
  if (aposta == "par" and number % 2 == 0 or aposta == "impar" and number % 2 != 0):
    pontos += 10
    labelStatus.config(text=f'Vidas: {vidas} | Pontos: {pontos}')
    labelCurrentNumber.config(text=f'Número: {number} - Acertou!')
  else:
    vidas -= 1
    labelStatus.config(text=f'Vidas: {vidas} | Pontos: {pontos}')
    labelCurrentNumber.config(text=f'Número: {number} - Errou!')

  if vidas == 0:
    labelResultado.config(text=f'Game Over! Pontos: {pontos}')
    evenBtn.config(state=tk.DISABLED)
    oddBtn.config(state=tk.DISABLED)
    restartBtn.pack(pady=10)

def reiniciarJogo():
    global vidas, pontos
    vidas = 3
    pontos = 0
    labelStatus.config(text=f'Vidas: {vidas} | Pontos: {pontos}')
    labelCurrentNumber.config(text='Número:')
    labelResultado.config(text='')
    evenBtn.config(state=tk.NORMAL)
    oddBtn.config(state=tk.NORMAL)
    restartBtn.pack_forget()

labelStatus = tk.Label(root, font=("Arial", 12), text=f'Vidas: {vidas} | Pontos: {pontos}')
labelStatus.pack(pady=10)

labelCurrentNumber = tk.Label(root, font=("Arial", 12), text='Número:')
labelCurrentNumber.pack(pady=10)

evenBtn = tk.Button(root, text='PAR', command=lambda: parOuImpar('par'))
evenBtn.pack(pady=10, padx=10)

oddBtn = tk.Button(root, text='IMPAR', command=lambda: parOuImpar('impar'))
oddBtn.pack(pady=10, padx=10)

labelResultado = tk.Label(root, font=("Arial", 12), text='')
labelResultado.pack(pady=10)

restartBtn = tk.Button(root, text='Recomeçar', width=15, command=reiniciarJogo)
restartBtn.pack_forget()

root.mainloop()
