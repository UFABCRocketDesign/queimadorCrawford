import tkinter as tk
import datetime as dt
import serial

root = tk.Tk()
dia_atual = dt.date.today()

#Número do experimento e data
root.title("Interface Queimador Crawford")
#Tamanho em pixels. Largura por comprimento
root.geometry("600x480")

#Nome do combustível
label_nome_combustivel = tk.Label(master=root, text="Nome:")
entrada_nome_combustivel = tk.Entry(root)
label_nome_combustivel.place(x=40, y=40)
entrada_nome_combustivel.place(x=110, y=50)
nome_combustivel = entrada_nome_combustivel.get()
label_combustivel = tk.Label(master=root, text="do combustível")
label_combustivel.place(x=20, y=60)

#Data
#Pegar data e horário automaticamente do relógio do computador

#Meio que um título de seção
label_parametros = tk.Label(master=root, text="Parâmetros do Corpo de Prova")
label_parametros.place(x=40, y=80)

#diâmetro do corpo de prova
label_diametro = tk.Label(master=root, text="Diâmetro:")
entrada_diametro = tk.Entry(master=root)
label_diametro.place(x=40, y=110)
entrada_diametro.place(x=100, y=110)
diametro = entrada_diametro.get()

#comprimento do corpo de prova
label_comprimento = tk.Label(master=root, text="Comprimento:")
entrada_comprimento = tk.Entry(master=root)
label_comprimento.place(x=40, y=140)
entrada_comprimento.place(x=125, y=140)
comprimento = entrada_comprimento.get()

#massa do corpo de prova
label_massa = tk.Label(master=root, text="Massa:")
entrada_massa = tk.Entry(master=root)
label_massa.place(x=40, y=170)
entrada_massa.place(x=80, y=170)
massa = entrada_massa.get()

#Título da seção
label_parametros_experimento = tk.Label(master=root, text="Parâmetros do Experimento:")
label_parametros_experimento.place(x=40, y=210)

#Distância entre os fios
label_distancia_entre_os_fios = tk.Label(master=root, text="Distância Entre os Fios:")
label_distancia_entre_os_fios.place(x=60, y=230)

label_distancia01 = tk.Label(master=root, text="d0~d1")
entrada_distancia01 = tk.Entry(master=root)
label_distancia01.place(x=80, y=250)
entrada_distancia01.place(x=120, y=250)
distancia01 = entrada_distancia01.get()

label_distancia12 = tk.Label(master=root, text="d1~d2")
entrada_distancia12 = tk.Entry(master=root)
label_distancia12.place(x=80, y=270)
entrada_distancia12.place(x=120, y=270)
distancia12 = entrada_distancia12.get()

label_distancia23 = tk.Label(master=root, text="d2~d3")
entrada_distancia23 = tk.Entry(master=root)
label_distancia23.place(x=80, y=290)
entrada_distancia23.place(x=120, y=290)
distancia23 = entrada_distancia23.get()

label_distancia34 = tk.Label(master=root, text="d3~d4")
entrada_distancia34 = tk.Entry(master=root)
label_distancia34.place(x=80, y=310)
entrada_distancia34.place(x=120, y=310)
distancia34 = entrada_distancia34.get()

label_distancia45 = tk.Label(master=root, text="d4~d5")
entrada_distancia45 = tk.Entry(master=root)
label_distancia45.place(x=80, y=330)
entrada_distancia45.place(x=120, y=330)
distancia45 = entrada_distancia45.get()

#Tipo de gás
label_gas = tk.Label(master=root, text="Tipo do gás:")
entrada_gas = tk.Entry(master=root)
label_gas.place(x=60, y=370)
entrada_gas.place(x=130, y=370)
gas = entrada_gas.get()

#Pressao interna
label_pressao_interna = tk.Label(master=root, text="Pressão interna:")
entrada_pressao_interna = tk.Entry(master=root)
label_pressao_interna.place(x=60, y=400)
entrada_pressao_interna.place(x=150, y=400)
pressao_interna = entrada_pressao_interna.get()

#Delay
label_delay = tk.Label(master=root, text="Delay")
label_delay.place(x=410, y=10)

#Checagem de ignição
label_start = tk.Label(master=root, text="Start:")
entrada_start = tk.Entry(master=root)
label_start.place(x=340, y=40)
entrada_start.place(x=370, y=40)
start = entrada_start.get()

#tempo de queima entre os fios
label_offset = tk.Label(master=root, text="Offset:")
entrada_offset = tk.Entry(master=root)
label_offset.place(x=340, y=70)
entrada_offset.place(x=380, y=70)
offset = entrada_offset.get()

#Número de ignições
label_ignocoes = tk.Label(master=root, text="Ignições:")
entrada_ignicoes = tk.Entry(master=root)
label_ignocoes.place(x=340, y=100)
entrada_ignicoes.place(x=390, y=100)
ignicoes = entrada_ignicoes.get()

#Largura do pulso
label_largura_pulso = tk.Label(master=root, text="Largura")
entrada_largura_pulso = tk.Entry(master=root)
label_largura_pulso.place(x=340, y=130)
entrada_largura_pulso.place(x=390, y=130)
largura_pulso = entrada_largura_pulso.get()
label_pulso = tk.Label(master=root, text="dos pulsos")
label_pulso.place(x=330, y=147)

#Vale
label_vale = tk.Label(master=root, text="Vale")
label_vale.place(x=390, y=170)

#Tempo entre os pulsos
label_offtiming = tk.Label(master=root, text="Offtiming:")
entrada_offtiming = tk.Entry(master=root)
label_offtiming.place(x=340, y=200)
entrada_offtiming.place(x=398, y=200)
offtiming = entrada_offtiming.get()

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#Período = largura dos pulsos + offtiming
#periodo = largura_pulso + offtiming
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#inicio = número de ignições * período
#inicio = float(ignicoes) * float(periodo)
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

botao_START = tk.Button(
    master=root,
    text="START",
    width=25,
    height=5,
    bg="grey",
    fg="black"
)
botao_START.place(x=330, y=280)


root.mainloop()