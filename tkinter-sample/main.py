from tkinter import *
from util.userDAO import UserDAO
from util.entities.user import User

class MyWindow:
    def __init__(self, win):
        self.lbl1=Label(win, text='Firstname')
        self.lbl2=Label(win, text='Lastname')
        self.lbl3=Label(win, text='Age')
        self.lbl4=Label(win, text='Email')
        self.lbl5=Label(win, text='Phone')
        self.t1=Entry(bd=3)
        self.t2=Entry()
        self.t3=Entry()
        self.t4=Entry()
        self.t5=Entry()
        self.btn1 = Button(win, text='Submit')
        self.lbl1.place(x=100, y=50)
        self.t1.place(x=200, y=50)
        self.lbl2.place(x=100, y=100)
        self.t2.place(x=200, y=100)
        self.lbl3.place(x=100, y=150)
        self.t3.place(x=200, y=150)
        self.lbl4.place(x=100, y=200)
        self.t4.place(x=200, y=200)
        self.lbl5.place(x=100, y=250)
        self.t5.place(x=200, y=250)
        self.b1=Button(win, text='Add', command=self.add)
        self.b1.place(x=100, y=300)        
    def add(self):
        user = User(self.t1.get(),self.t2.get(),int(self.t3.get()),self.t4.get(),self.t5.get())
        userDAO = UserDAO()
        userDAO.insertUser(user)

window=Tk()
mywin=MyWindow(window)
window.title('Hello Python')
window.geometry("400x400+10+10")
window.mainloop()