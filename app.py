# coding: utf-8
import tkinter as tk
from tkinter import *
import tkinter.scrolledtext
from tkinter.ttk import *
from tkinter.scrolledtext import ScrolledText
import banco as bco
import datetime
import time
import os



app = tk.Tk()
app.geometry('800x600')
app.title("ExecHoras")
tk = tkinter
ttk = tkinter



def center(win):
    # :param win: the main window or Toplevel window to center

    # Apparently a common hack to get the window size. Temporarily hide the
    # window to avoid update_idletasks() drawing the window in the wrong
    # position.
    win.update_idletasks()  # Update "requested size" from geometry manager

    # define window dimensions width and height
    width = win.winfo_width()
    frm_width = win.winfo_rootx() - win.winfo_x()
    win_width = width + 2 * frm_width

    height = win.winfo_height()
    titlebar_height = win.winfo_rooty() - win.winfo_y()
    win_height = height + titlebar_height + frm_width

    # Get the window position from the top dynamically as well as position from left or right as follows
    x = win.winfo_screenwidth() // 2 - win_width // 2
    y = win.winfo_screenheight() // 2 - win_height // 2

    # this is the line that will center your window
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    # This seems to draw the window frame immediately, so only call deiconify()
    # after setting correct window position
    win.deiconify()



def inicio():
    servico = bco.select_servico()
    print(servico)
    numero = bco.select_status()
    num = numero[0]
    n = num[0]
    print(n)

    horarios_inicio = bco.select_horainicio()

    for i in horarios_inicio:
        hor1 = (i[0])
        hor2 = (i[1])
        hor3 = (i[2])
        hor4 = (i[3])
        hor5 = (i[4])
        hor6 = (i[5])
        hor7 = (i[6])
        hor8 = (i[7])
        hor9 = (i[8])
        hor10 = (i[9])
        hor11 = (i[10])
        hor12 = (i[11])

    horarios_termino = bco.select_horatermino()

    for i in horarios_termino:
        hor13 = (i[0])
        hor14 = (i[1])
        hor15 = (i[2])
        hor16 = (i[3])
        hor17 = (i[4])
        hor18 = (i[5])
        hor19 = (i[6])
        hor20 = (i[7])
        hor21 = (i[8])
        hor22 = (i[9])
        hor23 = (i[10])
        hor24 = (i[11])

    while n == 1:
        print("entrou no while")
        hora = datetime.datetime.now()
        print(hora)
        agora = hora.strftime("%H:%M")
        print(agora)
        print(f'dentro do while')
        print('esta parando aqui')
        if agora == hor1:
            print(f'agora é:' + hor1 + 'vai rodar o start do serviço')
        if agora == hor2:
            print(f'agora é:' + hor2 + 'vai rodar o start do serviço')
        if agora == hor3:
            print(f'agora é:' + hor3 + 'vai rodar o start do serviço')
        if agora == hor4:
            print(f'agora é:' + hor4 + 'vai rodar o start do serviço')
        if agora == hor5:
            print(f'agora é:' + hor5 + 'vai rodar o start do serviço')
        if agora == hor6:
            print(f'agora é:' + hor6 + 'vai rodar o start do serviço')
            #os.system(f'netstart {servico}')
        if agora == hor7:
            print(f'agora é:' + hor7 + 'vai rodar o start do serviço')
            #os.system(f'netstart {servico}')
        if agora == hor8:
            print(f'agora é:' + hor8 + 'vai rodar o start do serviço')
            #os.system(f'netstart {servico}')
        if agora == hor9:
            print(f'agora é:' + hor9 + 'vai rodar o start do serviço')
            #os.system(f'netstart {servico}')
        if agora == hor10:
            print(f'agora é:' + hor10 + 'vai rodar o start do serviço')
            #os.system(f'netstart {servico}')
        if agora == hor11:
            print(f'agora é:' + hor11 + 'vai rodar o start do serviço')
            #os.system(f'netstart {servico}')
        if agora == hor12:
            print(f'agora é:' + hor12 + 'vai rodar o start do serviço')
            #os.system(f'netstart {servico}')
        if agora == hor13:
            print(f'agora é:' + hor13 + 'vai rodar o stop do serviço')
            #os.system(f'netstop {servico}')
        if agora == hor14:
            print(f'agora é:' + hor14 + 'vai rodar o stop do serviço')
            #os.system(f'netstop {servico}')
        if agora == hor15:
            print(f'agora é:' + hor15 + 'vai rodar o stop do serviço')
            #os.system(f'netstop {servico}')
        if agora == hor16:
            print(f'agora é:' + hor16 + 'vai rodar o stop do serviço')
            #os.system(f'netstop {servico}')
        if agora == hor17:
            print(f'agora é:' + hor17 + 'vai rodar o stop do serviço')
            #os.system(f'netstop {servico}')
        if agora == hor18:
            print(f'agora é:' + hor18 + 'vai rodar o stop do serviço')
            #os.system(f'netstop {servico}')
        if agora == hor19:
            print(f'agora é:' + hor19 + 'vai rodar o stop do serviço')
            #os.system(f'netstop {servico}')
        if agora == hor20:
            print(f'agora é:' + hor20 + 'vai rodar o stop do serviço')
            #os.system(f'netstop {servico}')
        if agora == hor21:
            print(f'agora é:' + hor21 + 'vai rodar o stop do serviço')
            #os.system(f'netstop {servico}')
        if agora == hor22:
            print(f'agora é:' + hor22 + 'vai rodar o stop do serviço')
            #os.system(f'netstop {servico}')
        if agora == hor23:
            print(f'agora é:' + hor23 + 'vai rodar o stop do serviço')
            #os.system(f'netstop {servico}')
        if agora == hor24:
            print(f'agora é:' + hor24 + 'vai rodar o stop do serviço')
            #os.system(f'netstop {servico}')
        print(f'terminou os ifs {n}')
        time.sleep(5)
        if n == 1:
            numero = bco.select_status()
            num = numero[0]
            n = num[0]
            print(n)


def batstart():
    print('start do serviço')
    numero = 1
    bco.update_cad_status(numero)
    inicio()

def batstop():
    print('stop do serviço')
    numero = 0
    bco.update_cad_status(numero)


def bat():
    print('entrou na bat')
    variavel = app.campo_s1.get()
    numero = 1
    bco.insert_cad_executor(variavel)
    bco.insert_cad_status(numero)

def arqhorario():
    #horarios de inicio
    print('entrou no arqhorario')
    varhor1 = app.campo_m1.get()
    varhor2 = app.campo_m2.get()
    varhor3 = app.campo_m3.get()
    varhor4 = app.campo_m4.get()
    varhor5 = app.campo_m5.get()
    varhor6 = app.campo_m6.get()
    varhor7 = app.campo_m7.get()
    varhor8 = app.campo_m8.get()
    varhor9 = app.campo_m9.get()
    varhor10 = app.campo_m10.get()
    varhor11 = app.campo_m11.get()
    varhor12 = app.campo_m12.get()
    # horarios de parada
    varhor13 = app.campo_m13.get()
    varhor14 = app.campo_m14.get()
    varhor15 = app.campo_m15.get()
    varhor16 = app.campo_m16.get()
    varhor17 = app.campo_m17.get()
    varhor18 = app.campo_m18.get()
    varhor19 = app.campo_m19.get()
    varhor20 = app.campo_m20.get()
    varhor21 = app.campo_m21.get()
    varhor22 = app.campo_m22.get()
    varhor23 = app.campo_m23.get()
    varhor24 = app.campo_m24.get()

    bco.insert_cad_inicio(varhor1, varhor2, varhor3, varhor4, varhor5, varhor6, varhor7, varhor8, varhor9, varhor10, varhor11, varhor12)
    bco.insert_cad_termino(varhor13, varhor14, varhor15, varhor16, varhor17, varhor18, varhor19, varhor20, varhor21, varhor22, varhor23, varhor24)

def horario():
    print('entrou no horario')
    newWindow = Toplevel(app)
    newWindow.title("Horário")
    newWindow.minsize(630, 250)
    center(newWindow)

    label_m0 = tk.Label(newWindow, text="Horários de Inicio")
    label_m0.place(x=265, y=10)


    label_m1 = tk.Label(newWindow, text="hora1")
    label_m1.place(x=20, y=40)
    app.campo_m1 = StringVar()
    app.campo_m1 = tk.Entry(newWindow, bd=3, textvariable=app.campo_m1)
    app.campo_m1.place(x=20, y=60, w=45, h=20)

    label_m2 = tk.Label(newWindow, text="hora2")
    label_m2.place(x=70, y=40)
    app.campo_m2 = StringVar()
    app.campo_m2 = tk.Entry(newWindow, bd=3, textvariable=app.campo_m2)
    app.campo_m2.place(x=70, y=60, w=45, h=20)

    label_m3 = tk.Label(newWindow, text="hora3")
    label_m3.place(x=120, y=40)
    app.campo_m3 = StringVar()
    app.campo_m3 = tk.Entry(newWindow,bd=3, textvariable=app.campo_m3)
    app.campo_m3.place(x=120, y=60, w=45, h=20)

    label_m4 = tk.Label(newWindow, text="hora4")
    label_m4.place(x=170, y=40)
    app.campo_m4 = StringVar()
    app.campo_m4 = tk.Entry(newWindow, bd=3, textvariable=app.campo_m4)
    app.campo_m4.place(x=170, y=60, w=45, h=20)

    label_m5 = tk.Label(newWindow, text="hora5")
    label_m5.place(x=220, y=40)
    app.campo_m5 = StringVar()
    app.campo_m5 = tk.Entry(newWindow, bd=3, textvariable=app.campo_m5)
    app.campo_m5.place(x=220, y=60, w=45, h=20)

    label_m6 = tk.Label(newWindow, text="hora6")
    label_m6.place(x=270, y=40)
    app.campo_m6 = StringVar()
    app.campo_m6 = tk.Entry(newWindow, bd=3, textvariable=app.campo_m6)
    app.campo_m6.place(x=270, y=60, w=45, h=20)

    label_m7 = tk.Label(newWindow, text="hora7")
    label_m7.place(x=320, y=40)
    app.campo_m7 = StringVar()
    app.campo_m7 = tk.Entry(newWindow, bd=3, textvariable=app.campo_m7)
    app.campo_m7.place(x=320, y=60, w=45, h=20)

    label_m8 = tk.Label(newWindow, text="hora8")
    label_m8.place(x=370, y=40)
    app.campo_m8 = StringVar()
    app.campo_m8 = tk.Entry(newWindow, bd=3, textvariable=app.campo_m8)
    app.campo_m8.place(x=370, y=60, w=45, h=20)

    label_m9 = tk.Label(newWindow, text="hora9")
    label_m9.place(x=420, y=40)
    app.campo_m9 = StringVar()
    app.campo_m9 = tk.Entry(newWindow, bd=3, textvariable=app.campo_m9)
    app.campo_m9.place(x=420, y=60, w=45, h=20)

    label_m10 = tk.Label(newWindow, text="hora10")
    label_m10.place(x=470, y=40)
    app.campo_m10 = StringVar()
    app.campo_m10 = tk.Entry(newWindow, bd=3, textvariable=app.campo_m10)
    app.campo_m10.place(x=470, y=60, w=45, h=20)

    label_m11 = tk.Label(newWindow, text="hora11")
    label_m11.place(x=520, y=40)
    app.campo_m11 = StringVar()
    app.campo_m11 = tk.Entry(newWindow, bd=3, textvariable=app.campo_m11)
    app.campo_m11.place(x=520, y=60, w=45, h=20)

    label_m12 = tk.Label(newWindow, text="hora12")
    label_m12.place(x=570, y=40)
    app.campo_m12 = StringVar()
    app.campo_m12 = tk.Entry(newWindow, bd=3, textvariable=app.campo_m12)
    app.campo_m12.place(x=570, y=60, w=45, h=20)

    label_m13 = tk.Label(newWindow, text="hora13")
    label_m13.place(x=20, y=140)
    app.campo_m13 = StringVar()
    app.campo_m13 = tk.Entry(newWindow, bd=3, textvariable=app.campo_m13)
    app.campo_m13.place(x=20, y=160, w=45, h=20)

    label_m14 = tk.Label(newWindow, text="hora14")
    label_m14.place(x=70, y=140)
    app.campo_m14 = StringVar()
    app.campo_m14 = tk.Entry(newWindow, bd=3, textvariable=app.campo_m14)
    app.campo_m14.place(x=70, y=160, w=45, h=20)

    label_m15 = tk.Label(newWindow, text="hora15")
    label_m15.place(x=120, y=140)
    app.campo_m15 = StringVar()
    app.campo_m15 = tk.Entry(newWindow, bd=3, textvariable=app.campo_m15)
    app.campo_m15.place(x=120, y=160, w=45, h=20)

    label_m16 = tk.Label(newWindow, text="hora16")
    label_m16.place(x=170, y=140)
    app.campo_m16 = StringVar()
    app.campo_m16 = tk.Entry(newWindow, bd=3, textvariable=app.campo_m16)
    app.campo_m16.place(x=170, y=160, w=45, h=20)

    label_m17 = tk.Label(newWindow, text="hora17")
    label_m17.place(x=220, y=140)
    app.campo_m17 = StringVar()
    app.campo_m17 = tk.Entry(newWindow, bd=3, textvariable=app.campo_m17)
    app.campo_m17.place(x=220, y=160, w=45, h=20)

    label_m18 = tk.Label(newWindow, text="hora18")
    label_m18.place(x=270, y=140)
    app.campo_m18 = StringVar()
    app.campo_m18 = tk.Entry(newWindow, bd=3, textvariable=app.campo_m18)
    app.campo_m18.place(x=270, y=160, w=45, h=20)

    label_m19 = tk.Label(newWindow, text="hora19")
    label_m19.place(x=320, y=140)
    app.campo_m19 = StringVar()
    app.campo_m19 = tk.Entry(newWindow, bd=3, textvariable=app.campo_m19)
    app.campo_m19.place(x=320, y=160, w=45, h=20)

    label_m20 = tk.Label(newWindow, text="hora20")
    label_m20.place(x=370, y=140)
    app.campo_m20 = StringVar()
    app.campo_m20 = tk.Entry(newWindow, bd=3, textvariable=app.campo_m20)
    app.campo_m20.place(x=370, y=160, w=45, h=20)

    label_m21 = tk.Label(newWindow, text="hora21")
    label_m21.place(x=420, y=140)
    app.campo_m21 = StringVar()
    app.campo_m21 = tk.Entry(newWindow, bd=3, textvariable=app.campo_m21)
    app.campo_m21.place(x=420, y=160, w=45, h=20)

    label_m22 = tk.Label(newWindow, text="hora22")
    label_m22.place(x=470, y=140)
    app.campo_m22 = StringVar()
    app.campo_m22 = tk.Entry(newWindow, bd=3, textvariable=app.campo_m22)
    app.campo_m22.place(x=470, y=160, w=45, h=20)

    label_m23 = tk.Label(newWindow, text="hora23")
    label_m23.place(x=520, y=140)
    app.campo_m23 = StringVar()
    app.campo_m23 = tk.Entry(newWindow, bd=3, textvariable=app.campo_m23)
    app.campo_m23.place(x=520, y=160, w=45, h=20)

    label_m24 = tk.Label(newWindow, text="hora24")
    label_m24.place(x=570, y=140)
    app.campo_24 = StringVar()
    app.campo_m24 = tk.Entry(newWindow, bd=3, textvariable=app.campo_24)
    app.campo_m24.place(x=570, y=160, w=45, h=20)

    label_m25 = tk.Label(newWindow, text="Horários de Termino")
    label_m25.place(x=255, y=100)

    botao_m26 = Button(newWindow, text='Salvar', command=arqhorario)
    botao_m26.place(x=165, y=200, w=100, h=25)

    botao_m26 = Button(newWindow, text='Fechar', command=newWindow.destroy)
    botao_m26.place(x=365, y=200, w=100, h=25)


def iniciar():
    print('entrou no iniciar')
    newWindow = Toplevel(app)
    newWindow.title("iniciar")
    newWindow.minsize(530, 150)
    center(newWindow)

    botao_s1 = Button(newWindow, text='iniciar', command=batstart)
    botao_s1.place(x=115, y=130, w=100, h=25)

    botao_s2 = Button(newWindow, text='parar', command=batstop)
    botao_s2.place(x=315, y=130, w=100, h=25)


def servico():
    print('entrou no servico')
    newWindow = Toplevel(app)
    newWindow.title("Serviço")
    newWindow.minsize(530, 150)
    center(newWindow)

    label_s1 = tk.Label(newWindow, text="Digite o nome exato do Serviço:")
    label_s1.place(x=180, y=20)

    app.campo_s1 =StringVar()
    app.campo_s1 = tk.Entry(newWindow, textvariable=app.campo_s1)
    app.campo_s1.place(x=140, y=70, w=240, h=25)

    botao_s1 = Button(newWindow, text='Salvar', command=bat)
    botao_s1.place(x=115, y=130, w=100, h=25)

    botao_s2 = Button(newWindow, text='Fechar', command=newWindow.destroy)
    botao_s2.place(x=315, y=130, w=100, h=25)


def sobre():
    print('entrou no sobre')
    newWindow = Toplevel(app)
    newWindow.title("Sobre Executor")
    newWindow.minsize(530, 250)
    center(newWindow)

    label_s1 = tk.Label(newWindow, text="InfoNarc 2023.1.0")
    label_s1.place(x=180, y=20)
    label_s2 = tk.Label(newWindow, text="Build#v1.0,build on March 04, 2023")
    label_s2.place(x=180, y=40)
    label_s3 = tk.Label(newWindow, text="Copyright@ 2020-2023 InfoNarc")
    label_s3.place(x=180, y=60)
    label_s4 = tk.Label(newWindow, text="e-mail: infonarc@infonarc.com.br")
    label_s4.place(x=180, y=80)



menubar = tk.Menu(app)

filemenu_a = tk.Menu(menubar, tearoff=0)
filemenu_b = tk.Menu(menubar, tearoff=0)
filemenu_c = tk.Menu(menubar, tearoff=0)
filemenu_d = tk.Menu(menubar, tearoff=0)
filemenu_a.add_command(label="Horários", command=horario)
filemenu_a.add_command(label="Serviço", command=servico)
filemenu_a.add_command(label="Iniciar Serviço", command=iniciar)
filemenu_a.add_command(label="Exit", command=exit)

filemenu_b.add_command(label="Sobre", command=sobre)

menubar.add_cascade(label="Menu", menu=filemenu_a)
menubar.add_cascade(label="Ajuda", menu=filemenu_b)

print('o sistema chegou aqui')
arquivo = open('config.txt')
arq = arquivo.readline()
start = arq[6]
st = start
print(f"leu o arquivo {start}")
if st == '1':
    print('sistema entrou no if do start')
    inicio()
print('sistema esta na ultima linha')



app.config(menu=menubar)

app.mainloop()


