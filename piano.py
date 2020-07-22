from tkinter import *
import tkinter as tk

pia=tk.Tk()
pia.geometry('550x250')
pia.title('Sup-Piano')
pia.iconbitmap(r'pia.ico')
pia.config(bg='#333333')


A=Frame(pia,bg="#ffffff",bd=20)
A.grid()
b=Frame(A,bg='red',bd=20)
b.grid()
L=Label(b,text='Sup-Piano',font=("arial",19,"bold"),padx=5,pady=5,fg='#333333',bd=20,justify=CENTER)
L.grid(row=0,column=0)


pia.mainloop()
