import tkinter as tk 
import numpy as np 
import matplotlib.pyplot as plt

HEIGHT = 600
WIDTH = 800

root = tk.Tk()
root.title("Trabalho de Comunicação de Dados - 2021/1")

msg_codificada = tk.StringVar()
msg_codificada.set("")

def codificarMensagem():
    label_msg_codificada.config(text="oi")

def binarizarMensagem():
    label_msg_binarizada.config(text="opa")

def aplicarPrincipio():
    label_msg_principio.config(text="principio aplicado")

def gerarGrafico():
    bindata = [0, 1, 0, 1, 1, 1, 0]
    x = np.arange(len(bindata))
    y = np.array(bindata)
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

btn_codificar = tk.Button(frame, text="Codificar mensagem", command = codificarMensagem)
btn_codificar.grid(row=1, column=1)

label_cod = tk.Label(frame, text="Mensagem codificada:")
label_cod.grid(row=2, column=0)

label_msg_codificada = tk.Label(frame, text= msg_codificada.get())
label_msg_codificada.config(text="<aguardando codificação>")
label_msg_codificada.grid(row=3, column=0)

btn_binarizar = tk.Button(frame, text="Binarizar mensagem", command = binarizarMensagem)
btn_binarizar.grid(row=3, column=1)

label_msg_binarizada = tk.Label(frame, text= msg_codificada.get())
label_msg_binarizada.config(text="<aguardando binarização>")
label_msg_binarizada.grid(row=4, column=0)

btn_aplicar_principio = tk.Button(frame, text="Aplicar princípio", command = aplicarPrincipio)
btn_aplicar_principio.grid(row=4, column=1)

label_msg_principio = tk.Label(frame, text= msg_codificada.get())
label_msg_principio.config(text="<aguardando aplicação>")
label_msg_principio.grid(row=5, column=0)

btn_gerar_grafico = tk.Button(frame, text="Gerar gráfico", command = gerarGrafico)
btn_gerar_grafico.grid(row=6, column=0)

btn_enviar = tk.Button(frame, text="Enviar", command = enviar)
btn_enviar.grid(row=6, column=1)

# Separação

frame_separate = tk.Frame(frame, bg='#282828', width=50, height=20)
frame_separate.grid(row=0, column=2)

# Receptor

label_recebida = tk.Label(frame, text= "Mensagem recebida:")
label_recebida.grid(row=0, column=3)

label_msg_recebida = tk.Label(frame, text= "")
label_msg_recebida.config(text="<aguardando receber mensagem>")
label_msg_recebida.grid(row=1, column=3)

root.mainloop()