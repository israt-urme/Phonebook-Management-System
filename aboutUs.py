from tkinter import *

class About(Toplevel):
    def __init__(self): #constructor
        Toplevel.__init__(self)
        
        self.geometry("550x300+350+200")
        self.title("About Us")
        self.resizable(False,False)
        
        #frame
        self.top=Frame(self,height=550,width=300,bg='#FA1515')
        self.top.pack(fill=BOTH) #fill x axis of top
        
        self.text=Label(self.top,text="This is about a page\n This application is made for educational purpose\nwhere we collect people information\ngather it on a phonebook\nyou can cntact us on\nu**********58@gmail.com",font='arial 14 bold',fg='white',bg='#FA1515')
        self.text.place(x=50,y=50)
        
