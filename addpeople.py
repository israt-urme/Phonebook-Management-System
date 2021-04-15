from tkinter import *
import sqlite3
from tkinter import messagebox

con=sqlite3.connect('database.db')
cur=con.cursor()

class AddPeople(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        
        self.geometry("650x550+350+200")
        self.title("Add People")
        self.resizable(False,False)
        
        #frame
        self.top=Frame(self,height=150,bg='gray')
        self.top.pack(fill=X) #fill x axis of top
        
        self.bottom=Frame(self,height=550,bg='#428CC3')
        self.bottom.pack(fill=X) #fill x axis of bottom
        
        #top frame design
        self.top_image=PhotoImage(file='icons/add.png')
        self.top_image_label=Label(self.top, image=self.top_image,bg='gray')
        self.top_image_label.place(x=100,y=35)
        
        #header title
        self.heading=Label(self.top, text='Add new person',font='arial 18 bold',bg='gray',fg='#FED805')
        self.heading.place(x=180,y=50)
        
        #data entry
        #firstname
        self.label_name= Label(self.bottom, text="First Name",font='arial 15 bold',bg='white' )
        self.label_name.place(x=40,y=40)
        
        self.entry_name = Entry(self.bottom, width=40,bd=4) #bd=border
        self.entry_name.insert(0,"enter first name")
        self.entry_name.place(x=150,y=40)
        
        #lastname
        self.label_lname= Label(self.bottom, text="Last Name",font='arial 15 bold',bg='white' )
        self.label_lname.place(x=40,y=80)
        
        self.entry_lname = Entry(self.bottom, width=40,bd=4) #bd=border
        self.entry_lname.insert(0,"enter last name")
        self.entry_lname.place(x=150,y=80)
        
        #email
        self.label_email= Label(self.bottom, text="Email",font='arial 15 bold',bg='white' )
        self.label_email.place(x=40,y=120)
        
        self.entry_email = Entry(self.bottom, width=40,bd=4) #bd=border
        self.entry_email.insert(0,"enter email")
        self.entry_email.place(x=150,y=120)
        
        #phone number
        self.label_pn= Label(self.bottom, text="Phone No.",font='arial 15 bold',bg='white' )
        self.label_pn.place(x=40,y=160)
        
        self.entry_pn = Entry(self.bottom, width=40,bd=4) #bd=border
        self.entry_pn.insert(0,"enter phone number")
        self.entry_pn.place(x=150,y=160)
        
        #address
        self.label_adr= Label(self.bottom, text="Address",font='arial 15 bold',bg='white' )
        self.label_adr.place(x=40,y=200)
        
        self.entry_adr = Text(self.bottom, width=30,bd=4,height=4) #bd=border
        self.entry_adr.place(x=150,y=200)
        #end data entry
        
        #button
        btn=Button(self.bottom, text="  ADD  ",command=self.add_people)
        btn.place(x=270,y=300)
        
    def add_people(self):
        name=self.entry_name.get()
        lname=self.entry_lname.get()
        email=self.entry_email.get()
        phone=self.entry_pn.get()
        address=self.entry_adr.get(1.0,'end-1c') #1st char to last char
        
        if name and lname and email and phone and address !="":
            try:
                #add to database
                query="INSERT INTO `peoplee`(`name`, `lastname`, `email`, `phone`, `address`) VALUES (?,?,?,?,?)"
                cur.execute(query,(name,lname,email, phone, address))
                con.commit()
                messagebox.showinfo("message","Successfully added...!")
            except EXCEPTION as e:
                messagebox.showerror("error",str(e))
        else:
            messagebox.showerror("error","fill all the fields", icon='warning' )
            
        
        
        

