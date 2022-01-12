# coding=utf-8

import requests
import threading
from tkinter import *
from time import *
import random
import sys

def quit(*args):
    window.destroy()
    #threading.Thread(target=atualiza_dados)._stop()
    #threading.Thread(target=update)._stop()
    #t1.daemon = True
    sys.exit()
    
def handle_kb_interrupt(sig, frame):
    stop_event.set()

def update():
    while 1:
        sleep(1)
        #ver tabela de letras que correspodem ao formato do relogio
        #https://www.programiz.com/python-programming/datetime/strftime
        time_string = strftime("%H:%M:%S")
        time_label.config(text=time_string)
        
            
        #date_string = strftime("%d %B %Y") dia mes ano
        date_month = strftime("%B")
        months_eng =   ["January",
                        "February",
                        "March",
                        "April",
                        "May",
                        "June",
                        "July",
                        "August",
                        "September",
                        "October",
                        "November",
                        "December"]
        meses_pt = ["Janeiro",
                    "Fevereiro",
                    "Março",
                    "Abril",
                    "Maio",
                    "Junho",
                    "Julho",
                    "Agosto",
                    "Setembro",
                    "Outubro",
                    "Novembro",
                    "Dezembro"]
        
        months_day_len = len (months_eng)
        
        for f in range (0,months_day_len):
            if date_month == months_eng[f]:
                date_month = meses_pt[f]
                
        date_string = strftime("%d ") + date_month + strftime(" %Y")
        
        date_label.config(text=date_string)

def atualiza_dados():
    while 1:
        sleep(3)
        resposta = requests.get('http://192.168.1.1/')
        dados = resposta.text
        
        if resposta.status_code==200:
            print("OK") #se diferente de 200 erro de ligação
            connection.config(text="OK")
        else:
            print(resposta.status_code) #se diferente de 200 erro de ligação
            connection.config(text="ERROR")
        
        dados_separados = dados.split("e")  
        temp = dados_separados[0] + "ºC"
        temp1 = 99 - int(dados_separados[0])
        
        temperatura.config(text=temp)
        print("temperatura ", temp)
        hum = dados_separados[1] + "%"
        hum1 = 99 - int(dados_separados[1])
        #hum = "%"
        print("humidade    ", hum)
        humidade.config(text=hum)
        feedback="teste"
        envio = requests.put('http://192.168.1.1/saida',feedback)
        #resposta_b = requests.get('http://192.168.1.1/')
        #dadosb = respostab.text
        #print(dadosb)
        can_temp.create_rectangle(100, 100, 0, 0, outline="#101", fill="GREY", width=0)
        can_temp.create_rectangle(99, 99, 1, temp1, outline="#f11", fill="BLUE", width=2)
        can_temp.create_text(50,91,font="Times 20", text=temp,tag='temperatura', fill="WHITE")
        #scaleTemp.set(dados_separados[0])
        can_hum.create_rectangle(100, 100, 0, 0, outline="#101", fill="GREY", width=0)
        can_hum.create_rectangle(99, 99, 1, hum1, outline="#f11", fill="BLUE", width=2)
        can_hum.create_text(50,91,font="Times 20", text=hum,tag='humidade', fill="WHITE")

window = Tk()
window.bind("<Escape>", quit)
window.bind("x", quit)


window.geometry("720x620")
window.title("Leitura de Dados")

icon = PhotoImage(file='ico.png')
window.iconphoto(True,icon)
window.config(background="#5cfcff")


hotImage = PhotoImage(file='temperatura.png')
hotLabel = Label(image=hotImage)
hotLabel.grid(row=0,column=0,padx=10,rowspan=1)


can_temp = Canvas(window,width=100,height=100)
can_temp.grid(row=0,column=1, padx=10, pady=10,rowspan=1)
'''
scaleTemp = Scale(window,
                from_=100,to=0,length=200, orient=VERTICAL, tickinterval=10, resolution=1,sliderlength=20,width=100,
                troughcolor='BLUE',fg='YELLOW',bg='GREY')


scaleTemp.grid(row=0,column=2, padx=10, pady=10,rowspan=1)
'''


humImage = PhotoImage(file='humidade.png')
humLabel = Label(image=humImage)
humLabel.grid(row=0,column=3, padx=10, pady=10,rowspan=1)

can_hum = Canvas(window,width=100,height=100)
can_hum.grid(row=0,column=4, padx=10, pady=10,rowspan=1)


label_temperatura = Label(window,text="temperatura",font=("Ink Free",20))
label_temperatura.grid(row=1,column=0,columnspan=2, sticky=N, padx=10)

label_humidade = Label(window,text="humidade",font=("Ink Free",20))
label_humidade.grid(row=1,column=4,columnspan=1, sticky=N, padx=10)

temperatura = Label(window,font=("Ink Free",30))
temperatura.grid(row=2,column=0,columnspan=2, sticky=N, padx=10, pady=10)

humidade = Label(window,font=("Ink Free",30))
humidade.grid(row=2,column=4,columnspan=1, sticky=N, padx=10, pady=10)

date_label = Label(window,font=("Ink Free",30))
date_label.grid(row=7,column=0,columnspan=2, sticky=N, padx=10, pady=10)

connection = Label(window,font=("Ink Free",30))
connection.grid(row=8,column=1,columnspan=2, sticky=N, padx=10, pady=10)

time_label = Label(window,font=("Ink Free",30))
time_label.grid(row=7,column=3,columnspan=2, sticky=N, padx=10, pady=10)


#t1 = threading.Thread(target=atualiza_dados)
#t1.daemon = True
#t1.start()

#t2 = threading.Thread(target=start)
#t2.daemon = True
#t2.start()

threading.Thread(target=atualiza_dados).start()
threading.Thread(target=update).start()


window.mainloop()
#sys.exit()

