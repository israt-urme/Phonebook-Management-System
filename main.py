# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from tkinter import *
from mypeople import MyPeople
from addpeople import AddPeople
from aboutUs import About
import datetime

date=datetime.datetime.now().date()
date=str(date)

class Application(object):
    def __init__(self,master):
        self.master=master
        
        #frame
        self.top=Frame(master,height=150,bg='gray')
        self.top.pack(fill=X) #fill x axis of top
        
        self.bottom=Frame(master,height=550,bg='#FF5733')
        self.bottom.pack(fill=X) #fill x axis of bottom
        
        #top frame design
        self.top_image=PhotoImage(file='icons/book.png')
        self.top_image_label=Label(self.top, image=self.top_image,bg='gray')
        self.top_image_label.place(x=100,y=35)
        
        #header title
        self.heading=Label(self.top, text='Phonebook Management System',font='arial 18 bold',bg='gray',fg='#1EE921')
        self.heading.place(x=180,y=50)
        
        #date
        self.date_lbl=Label(self.top, text="date: "+date,font='arial 12 bold',fg='black',bg='gray')
        self.date_lbl.place(x=500,y=120)
        
        #button
        self.viewButton =Button(self.bottom, text="  My People ",font='arial 12 bold',bg='#F7D22B',command=self.my_people)
        self.viewButton.place(x=250,y=70)
        
        self.viewButton =Button(self.bottom, text=" Add People",font='arial 12 bold',bg='#F7D22B',command=self.add_peoplefunc)
        self.viewButton.place(x=250,y=130)
        
        self.viewButton =Button(self.bottom, text="  About Us   ",font='arial 12 bold',bg='#F7D22B',command=self.about_us)
        self.viewButton.place(x=250,y=190)
        
    def my_people(self):
        people=MyPeople()
        
    def add_peoplefunc(self):
        people1=AddPeople()
        
    def about_us(self):
        people2=About()
        
        
        

def main():
    root=Tk() #create window
    
    app=Application(root)
    
    root.title("phonebook")
    root.geometry("650x550+350+200")
    root.resizable(False, False)
    root.mainloop() #run window code
    
if __name__=='__main__':
     main()

# =============================================================================
# root=Tk() #create window
# theLabel=Label(root,text="hey! ")
# theLabel.pack()
# root.mainloop() #run window code
# 
# =============================================================================
