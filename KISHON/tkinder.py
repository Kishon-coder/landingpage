import tkinter as tk
from tkinter import ttk

win=tk.Tk()
win.geometry('1350x700')
win.title('student management system')


title_label=tk.Label(win,text='Library Management System',font=('Arial',30,'bold'),bd=12,relief=tk.GROOVE,bg='brown')
title_label.pack(side=tk.TOP,fill=tk.X)

deatil_frame=tk.LabelFrame(win,text='Enter details',font=('Arial',20,'bold'),bd=12,relief=tk.GROOVE,bg='brown')
deatil_frame.place(x=20,y=90,width=420,height=575)

data_frame=tk.Frame(win,bd=12,relief=tk.GROOVE,bg='brown')
data_frame.place(x=100,y=90,width=600,height=575)
