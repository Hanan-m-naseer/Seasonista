from tkinter import *
from tkinter import messagebox
top=Tk()
top.geometry('300x300')

agreement=StringVar()
def agreement_state():
    messagebox.showinfo(message=agreement.get())

Checkbutton(top,text="i agree",command=agreement_state,variable=agreement,onvalue="i agree",offvalue="disagree").pack()
top.mainloop()