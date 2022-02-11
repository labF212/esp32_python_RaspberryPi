# coding=utf-8

#https://likegeeks.com/python-gui-examples-tkinter-tutorial/
#import requests
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
    
#def handle_kb_interrupt(sig, frame):
#    stop_event.set()

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
        sleep(2)
        temp1 = random.randint(20,40)
        hum1 = random.randint(10,80)
        
        temp = str(temp1) + "ºC"
        temp1 = 99 - temp1
        
        temperatura.config(text=temp)
        print("temperatura ", temp)
        hum = str(hum1) + "%"
        hum2 = 99 - hum1
        #hum = "%"
        print("humidade    ", hum)
        humidade.config(text=hum)
        
        
        can_temp.create_rectangle(100, 100, 0, 0, outline="#101", fill="GREY", width=0)
        can_temp.create_rectangle(99, 99, 1, temp1, outline="#f11", fill="BLUE", width=2)
        can_temp.create_text(50,91,font="Times 20", text=temp,tag='temperatura', fill="WHITE")
        
        can_hum.create_rectangle(100, 100, 0, 0, outline="#101", fill="GREY", width=0)
        can_hum.create_rectangle(99, 99, 1, hum2, outline="#f11", fill="BLUE", width=2)
        can_hum.create_text(50,91,font="Times 20", text=hum,tag='humidade', fill="WHITE")
        
        #Definição de limites min e max do sensor de humidade
        spin_low = Spinbox(window, from_=0, to=50, width=3, textvariable=var,justify="center",font="Times 15")
        spin_high = Spinbox(window, from_=51, to=100, width=3,textvariable=var1,font=("Times", 15), justify="center")
        spin_low.grid(column=4,row=2,columnspan=1,rowspan=1, pady=120,sticky=N)
        spin_high.grid(column=4,row=2,columnspan=1,rowspan=1, pady=150,sticky=N)
        minimo= var.get()
        maximo= var1.get()
        
        if hum1<minimo:
            print("Fora do limite")
            green_label.config(text="Fora do limite")
            GreenLedImage = PhotoImage(file='redoffline.png')
        elif hum1>=minimo and hum1<=maximo:
            green_label.config(text="OK")
            GreenLedImage = PhotoImage(file='greenledon.png')
            print("OK")
        else:
            green_label.config(text="Humidade Elevada")
            GreenLedImage = PhotoImage(file='greenledoff.png')
            print("Humidade Elevada")
        
        #GreenLedImage = PhotoImage(file='redoffline.png')
        GreenLedImage = GreenLedImage.subsample(2, 2) #reduz 50%
        GreenLedLabel = Label(image=GreenLedImage)
        GreenLedLabel.grid(row=2,column=2, padx=10, pady=40,rowspan=1,columnspan=2,sticky=N)

window = Tk()
window.bind("<Escape>", quit)
window.bind("x", quit)


window.geometry("720x620")
window.title("Leitura de Dados")

icon = PhotoImage(file='ico.png')
window.iconphoto(True,icon)
window.config(background="#5cfcff")

var =IntVar()
var.set(30)

var1 =IntVar()
var1.set(60)


hotImage = PhotoImage(file='temperatura.png')
hotLabel = Label(image=hotImage)
hotLabel.grid(row=0,column=0,padx=10,rowspan=1)


can_temp = Canvas(window,width=100,height=100)
can_temp.grid(row=0,column=1, padx=10, pady=10,rowspan=1)



humImage = PhotoImage(file='humidade.png')
humLabel = Label(image=humImage)
humLabel.grid(row=0,column=3, padx=10, pady=10,rowspan=1)

can_hum = Canvas(window,width=100,height=100)
can_hum.grid(row=0,column=4, padx=10, pady=10,rowspan=1)


label_temperatura = Label(window,text="Temperatura",font=("Ink Free",20))
label_temperatura.grid(row=1,column=0,columnspan=2, sticky=N, padx=10)

label_humidade = Label(window,text="Humidade",font=("Ink Free",20))
label_humidade.grid(row=1,column=3,columnspan=2, sticky=N, padx=10)

temperatura = Label(window,font=("Ink Free",30))
temperatura.grid(row=2,column=0,columnspan=2, sticky=N, padx=10, pady=10)

humidade = Label(window,font=("Ink Free",30))
humidade.grid(row=2,column=4,columnspan=1, sticky=N, padx=10, pady=10)



green_label = Label(window,font=("Ink Free",10))
green_label.grid(row=2,column=3,columnspan=1, sticky=N, padx=10, pady=10)

label_sensor_hummin = Label(window,text="Reg Sensor Hum Min",font=("Ink Free",10))
label_sensor_hummin.grid(row=2,column=4,columnspan=1, sticky=N, padx=10, pady=90)

label_sensor_hummax = Label(window,text="Reg Sensor Hum Max",font=("Ink Free",10))
label_sensor_hummax.grid(row=2,column=4,columnspan=1, sticky=N, padx=10, pady=180)

date_label = Label(window,font=("Ink Free",30))
date_label.grid(row=2,column=0,columnspan=2, sticky=N, padx=10, pady=300)

time_label = Label(window,font=("Ink Free",30))
time_label.grid(row=2,column=3,columnspan=2, sticky=N, padx=10, pady=300)

#t1 = threading.Thread(target=atualiza_dados)
#t1.daemon = True
#t1.start()

#t2 = threading.Thread(target=start)
#t2.daemon = True
#t2.start()

threading.Thread(target=atualiza_dados).start()
threading.Thread(target=update).start()


window.mainloop()