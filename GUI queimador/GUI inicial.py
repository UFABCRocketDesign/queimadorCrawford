import tkinter as tk
import datetime as dt

root = tk.Tk()
dia_atual = dt.date.today()

#Número do experimento e data
root.title('Experimento número {}, {}/{}/{}'.format(0, dia_atual.day, dia_atual.month, dia_atual.year))
#Tamanho em pixels. Largura por comprimento
root.geometry("1000x1000")

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

#Distância entre os fios
label_distancia_entre_os_fios = tk.Label(master=root, text="Distância Entre os Fios")
label_distancia_entre_os_fios.pack()

label_distancia01 = tk.Label(master=root, text="d0~d1")
entrada_distancia01 = tk.Entry(master=root)
label_distancia01.pack()
entrada_distancia01.pack()
distancia01 = entrada_distancia01.get()

label_distancia12 = tk.Label(master=root, text="d1~d2")
entrada_distancia12 = tk.Entry(master=root)
label_distancia12.pack()
entrada_distancia12.pack()
distancia12 = entrada_distancia12.get()

label_distancia23 = tk.Label(master=root, text="d2~d3")
entrada_distancia23 = tk.Entry(master=root)
label_distancia23.pack()
entrada_distancia23.pack()
distancia23 = entrada_distancia23.get()

label_distancia34 = tk.Label(master=root, text="d3~d4")
entrada_distancia34 = tk.Entry(master=root)
label_distancia34.pack()
entrada_distancia34.pack()
distancia34 = entrada_distancia34.get()

label_distancia45 = tk.Label(master=root, text="d4~d5")
entrada_distancia45 = tk.Entry(master=root)
label_distancia45.pack()
entrada_distancia45.pack()
distancia45 = entrada_distancia45.get()

#Tipo de gás
label_gas = tk.Label(master=root, text="Tipo do gás:")
entrada_gas = tk.Entry(master=root)
label_gas.pack()
entrada_gas.pack()
gas = entrada_gas.get()

#Pressao interna
label_pressao_interna = tk.Label(master=root, text="Pressão interna:")
entrada_pressao_interna = tk.Entry(master=root)
label_pressao_interna.pack()
entrada_pressao_interna.pack()
pressao_interna = entrada_pressao_interna.get()

root.mainloop()