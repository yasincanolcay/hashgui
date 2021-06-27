#https://md5.gromweb.com/?md5={}
#"em",attrs={"class":"long-content string"

#https://sha1.gromweb.com/?hash={}


import tkinter
from tkinter import Tk
from tkinter import messagebox
import requests
from time import sleep
from threading import Thread
from tkinter import *
from bs4 import BeautifulSoup

master = Tk()
master.geometry('500x300+200+200')
master.resizable(False,False)
#-----------------------#
#-----------------------#
frame1 = Frame(master,bg='dodgerblue')
frame1.place(relx=0,rely=0,relwidth=1.0,relheight=0.2)

l1 = Label(frame1,text="Lütfen Format Seçiniz:",bg="dodgerblue",fg="black",font="Arial 12 bold")
l1.pack(padx=5,pady=5,side=LEFT)

var = IntVar()

r1 = Radiobutton(frame1,text="MD5",bg="dodgerblue",fg="black",font="Arial 12 bold",variable = var,value=1)
r1.pack(padx=5,pady=5,side=LEFT)

r2 = Radiobutton(frame1,text="SHA1",bg="dodgerblue",fg="black",font="Arial 12 bold",variable = var,value=2)
r2.pack(padx=5,pady=5,side=LEFT)

#-----------------------#
frame2 = Frame(master,bg='dodgerblue')
frame2.place(relx=0,rely=0.21,relwidth=1.0,relheight=0.2)

l2 = Label(frame2,text="Lütfen Hash Giriniz: ",bg="dodgerblue",fg="black",font="Arial 12 bold")
l2.pack(padx=5,pady=5,side=LEFT)
e1 = Entry(frame2,bd=2)
e1.pack(padx=5,pady=5,side=LEFT)

from tkinter import messagebox
def start():

    uyari = ""
    if var.get():
        l3["text"] = "LÜTFEN BEKLEYİNİZ..."

        if var.get() == 1:

            def d1():

                md5 = e1.get()
                sorgula = "https://md5.gromweb.com/?md5={}".format(md5)
                sorgulama_istegi = requests.get(sorgula)
                sleep(3)
                soup = BeautifulSoup(sorgulama_istegi.content,"lxml")
                bilgi = soup.find_all("em",attrs={"class":"long-content string"})

                for hash in bilgi:

                    l3["text"] = "HASH SONUCU: {}".format(hash.text)

            t1 = Thread(target=d1)
            t1.start()

        elif var.get() == 2:

            def d1():

                sha1 = e1.get()
                sorgula = "https://sha1.gromweb.com/?hash={}".format(sha1)
                sorgulama_istegi = requests.get(sorgula)
                sleep(3)
                soup = BeautifulSoup(sorgulama_istegi.content,"lxml")
                bilgi = soup.find_all("em",attrs={"class":"long-content string"})

                for hash in bilgi:

                    l3["text"] = "HASH SONUCU: {}".format(hash.text)

            t1 = Thread(target=d1)
            t1.start()

    else:

        uyari += "LÜTFEN GEÇERLİ SEÇİM YAPINIZ !!"
        messagebox.showerror("seçim yapılmadı!",uyari)







btn = Button(frame2,text="Sorgula",bg="green",fg="white",font="Arial 12 bold",command=start)
btn.pack(padx=5,pady=5,side=LEFT)


#-----------------------#
frame3 = Frame(master,bg='dodgerblue')
frame3.place(relx=0,rely=0.42,relwidth=1.0,relheight=0.58)

l3 = Label(frame3,text="SONUÇLAR BURADA GÖRÜNÜR...",bg="dodgerblue",fg="black",font="Arial 20 bold")
l3.pack(pady=25,anchor=S)




#-----------------------#






master.mainloop()



