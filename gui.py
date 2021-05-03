import tkinter as tk 
import numpy as np 
import matplotlib.pyplot as plt

HEIGHT = 600
WIDTH = 800
DATA_TESTE_ENVIO = ["+", "-", "0", "-", "+", "+", "+"]
DATA_TESTE_RECEBIDO = ["+", "-", "0", "-", "+", "+", "+"]

root = tk.Tk()
root.title("Trabalho de Comunicação de Dados - 2021/1")

def graficalizar(data):
    bin_data = []
    for i in range (len(data)):
        if (data[i] == '+'):
            bin_data.append(1)
        if (data[i] == '-'):
            bin_data.append(-1)
        if (data[i] == '0'):
            bin_data.append(0)
    return bin_data

msg_codificada = tk.StringVar()
msg_codificada.set("")

msg_descodificada = tk.StringVar()
msg_descodificada.set("")

def criptografarMensagem():
    label_msg_criptografada.config(text="oi")

def binarizarMensagem():
    label_msg_binarizada.config(text="opa")

def aplicarCodificacao():
    label_msg_aplicar_codificacao.config(text="codificação aplicada")

def aplicarDescodificacao():
    label_msg_principio.config(text="descodificacao aplicada")


def gerarGraficoEnvio():
    data = DATA_TESTE_ENVIO
    bin_data = graficalizar(data)
    x = np.arange(len(bin_data))
    y = np.array(bin_data)
    plt.step(x,y)
    plt.show()

def gerarGraficoRecebido():
    data = DATA_TESTE_RECEBIDO
    bin_data = graficalizar(data)
    x = np.arange(len(bin_data))
    y = np.array(bin_data)
    plt.step(x,y)
    plt.show()

def enviar():
    print()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = tk.Frame(root, bg='#282828')
frame.place(relx = 0.005, rely = 0.01, relwidth=0.99, relheight=0.98)

label_ins_msg = tk.Label(frame, text="Insira a mensagem")
label_ins_msg.grid(row=0, column=0)

entry_msg = tk.Entry(frame, bd = 5, textvariable = msg_codificada)
entry_msg.grid(row=1, column=0)

btn_criptografar = tk.Button(frame, text="Criptografar mensagem", command = criptografarMensagem)
btn_criptografar.grid(row=1, column=1)

label_cript = tk.Label(frame, text="Mensagem criptografada:")
label_cript.grid(row=2, column=0)

label_msg_criptografada = tk.Label(frame, text= msg_codificada.get())
label_msg_criptografada.config(text="<aguardando criptografia>")
label_msg_criptografada.grid(row=3, column=0)

btn_binarizar = tk.Button(frame, text="Transformar em binário", command = binarizarMensagem)
btn_binarizar.grid(row=3, column=1)

label_msg_binarizada = tk.Label(frame, text= msg_codificada.get())
label_msg_binarizada.config(text="<aguardando binarização>")
label_msg_binarizada.grid(row=4, column=0)

btn_aplicar_codificacao = tk.Button(frame, text="Aplicar codificação", command = aplicarCodificacao)
btn_aplicar_codificacao.grid(row=4, column=1)

label_msg_aplicar_codificacao = tk.Label(frame, text= msg_codificada.get())
label_msg_aplicar_codificacao.config(text="<aguardando codificação>")
label_msg_aplicar_codificacao.grid(row=5, column=0)

btn_gerar_grafico = tk.Button(frame, text="Gerar gráfico", command = gerarGraficoEnvio)
btn_gerar_grafico.grid(row=6, column=0)

btn_enviar = tk.Button(frame, text="Enviar", command = enviar)
btn_enviar.grid(row=6, column=1)

# Separação

frame_separate = tk.Frame(frame, bg='#282828', width=50, height=20)
frame_separate.grid(row=0, column=2)
frame_separate = tk.Frame(frame, bg='#282828', width=50, height=20)
frame_separate.grid(row=1, column=2)

# Receptor

label_recebida = tk.Label(frame, text= "Mensagem recebida:")
label_recebida.grid(row=0, column=3)

label_msg_recebida = tk.Label(frame, text= "")
label_msg_recebida.config(text="<aguardando receber mensagem>")
label_msg_recebida.grid(row=1, column=3)

btn_gerar_grafico_recebido = tk.Button(frame, text="Gerar gráfico", command = gerarGraficoRecebido)
btn_gerar_grafico_recebido.grid(row=2, column=3)


root.mainloop()