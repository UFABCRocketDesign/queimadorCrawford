import tkinter as tk
import time

inicio = time.time()


root = tk.Tk()
#Número do experimento e data
root.title('Experimento número {}, {}/{}/{}'.format(0,1,2,3))
#Tamanho em pixels. Largura por comprimento
root.geometry("1000x550")

#Nome do operador
label_nome_operador = tk.Label(master=root, text="Nome:")
entrada_nome_operador = tk.Entry(root)
label_nome_operador.pack()
entrada_nome_operador.pack()
nome_operador = entrada_nome_operador.get()

#Data
#Pegar data e horário automaticamente do relógio do computador

#Meio que um título de seção
label_parametros = tk.Label(master=root, text="Parâmetros do Corpo de Prova")
label_parametros.pack()

#diâmetro do corpo de prova
label_diametro = tk.Label(master=root, text="Diâmetro:")
entrada_diametro = tk.Entry(master=root)
label_diametro.pack()
entrada_diametro.pack()
diametro = entrada_diametro.get()

#comprimento do corpo de prova
label_comprimento = tk.Label(master=root, text="Comprimento:")
entrada_comprimento = tk.Entry(master=root)
label_comprimento.pack()
entrada_comprimento.pack()
comprimento = entrada_comprimento.get()

#massa do corpo de prova
label_massa = tk.Label(master=root, text="Massa:")
entrada_massa = tk.Entry(master=root)
label_massa.pack()
entrada_massa.pack()
massa = entrada_massa.get()

#Título da seção
label_parametros_experimento = tk.Label(master=root, text="Parâmetros do Experimento")
label_parametros_experimento.pack()






fim = time.time()
print(fim - inicio)