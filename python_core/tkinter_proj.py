from tkinter import *
top = Tk()

top.geometry('750x750')

radio=IntVar()

def perform_operation():
    n1=int(e1.get())
    n2=int(e2.get())

    if radio.get()==1:
        res=add(n1,n2)
    elif radio.get()==2:
        res=sub(n1,n2)
    elif radio.get()==3:
        res=mul(n1,n2)
    elif radio.get()==4:
        res=div(n1,n2)

    result.delete(1.0,END)    
    result.insert(END,f'result is:{res}')       

def add(num1,num2):
    return num1+num2

def sub(num1,num2):
    return num1-num2

def mul(num1,num2):
    return num1*num2

def div(num1,num2):
    return num1/num2


first_number = Label(top,text='first number')
first_number.grid(row=0,column=0)

e1 = Entry(top)
e1.grid(row=0,column=1)

second_number = Label(top,text='second number')
second_number.grid(row=1,column=0)

e2 = Entry(top)
e2.grid(row=1,column=1)

r1=Radiobutton(top,text='addition',variable=radio,value=1)
r1.grid(row=3,column=1)
r2=Radiobutton(top,text='subtraction',variable=radio,value=2)
r2.grid(row=3,column=3)
r3=Radiobutton(top,text='multiplication',variable=radio,value=3)
r3.grid(row=3,column=5)
r4=Radiobutton(top,text='division',variable=radio,value=4)
r4.grid(row=3,column=7)

button = Button(top,text='submit',command=perform_operation)
button.grid(row=4,column=1)

result=Text(top,height=3,width=30)
result.grid(row=6,column=1)



top.mainloop()