from tkinter import *
import tkinter as tk
import simpleaudio as s

sa = s.WaveObject.from_wave_file("tones\\C.wav")
ri = s.WaveObject.from_wave_file("tones\\D.wav")
ga = s.WaveObject.from_wave_file("tones\\E.wav")
ma = s.WaveObject.from_wave_file("tones\\F.wav")
pa = s.WaveObject.from_wave_file("tones\\G.wav")
ta = s.WaveObject.from_wave_file("tones\\A.wav")
ni = s.WaveObject.from_wave_file("tones\\B.wav")
saa = s.WaveObject.from_wave_file("tones\\C1.wav")


def Sa():
    sa.play()
def Ri():
    ri.play()
def Ga():
    ga.play()
def Ma():
    ma.play()
def Pa():
    pa.play()
def Ta():
    ta.play()
def Ni():
    ni.play()
def Ni():
    saa.play()

pia=tk.Tk()
pia.geometry('550x250')
pia.title('X-Piano')
pia.iconbitmap(r'pia.ico')
pia.config(bg='#333333')


A=Frame(pia,bg="#ffffff",bd=10)
A.pack(side=TOP)
b=Frame(A,bg='#333333',bd=10)
b.pack()
L=Label(b,text='Piano',font=("arial",19,"bold"),padx=5,pady=5,fg='#333333',bd=10,justify=CENTER)
L.grid(row=0,column=0)
c=Frame(pia,bd=15,bg='#333333')
c.pack()
'''
Bt1=Button(c,height=5,width=1,padx=5,pady=5).pack()
Bt2=Button(c,height=5,width=1,padx=5,pady=5).pack()
,font=("arial",7,"bold")
'''

Bt1=Button(c,height=7,width=3,bd=4,text="SA",fg="#333333",bg='#ffffff',justify=CENTER,font=("arial",7,"bold"),command=Sa).grid(row=0,column=0,padx=3,pady=3)
Bt2=Button(c,height=7,width=3,bd=4,text="RI",fg="#333333",bg='#ffffff',justify=CENTER,font=("arial",7,"bold"),command=Ri).grid(row=0,column=1,padx=3,pady=3)
Bt3=Button(c,height=7,width=3,bd=4,text="GA",fg="#333333",bg='#ffffff',justify=CENTER,font=("arial",7,"bold"),command=Ga).grid(row=0,column=2,padx=3,pady=3)
Bt4=Button(c,height=7,width=3,bd=4,text="MA",fg="#333333",bg='#ffffff',justify=CENTER,font=("arial",7,"bold"),command=Ma).grid(row=0,column=3,padx=3,pady=3)
Bt5=Button(c,height=7,width=3,bd=4,text="PA",fg="#333333",bg='#ffffff',justify=CENTER,font=("arial",7,"bold"),command=Pa).grid(row=0,column=4,padx=3,pady=3)
Bt6=Button(c,height=7,width=3,bd=4,text="DA",fg="#333333",bg='#ffffff',justify=CENTER,font=("arial",7,"bold"),command=Ta).grid(row=0,column=5,padx=3,pady=3)
Bt7=Button(c,height=7,width=3,bd=4,text="NI",fg="#333333",bg='#ffffff',justify=CENTER,font=("arial",7,"bold"),command=Ni).grid(row=0,column=6,padx=3,pady=3)
Bt8=Button(c,height=7,width=3,bd=4,text="SA",fg="#333333",bg='#ffffff',justify=CENTER,font=("arial",7,"bold"),command=Sa).grid(row=0,column=7,padx=3,pady=3)

pia.mainloop()
