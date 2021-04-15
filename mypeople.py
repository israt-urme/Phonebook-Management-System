from tkinter import *
from addpeople import AddPeople
from updatepeople import Update
from displaypeople import Display
from tkinter import messagebox
import sqlite3 #database

con=sqlite3.connect('database.db')
cur=con.cursor()
# =============================================================================
# cur.execute("""CREATE TABLE peoplee (
#         person_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         name TEXT,
#         lastname TEXT,
#         email TEXT,
#         phone TEXT,
#         address TEXT
#         )""")
# con.commit()
# con.close()
# =============================================================================

class MyPeople(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        
        self.geometry("650x650+600+200")
        self.title("View My people")
        self.resizable(False,False)
        
        #frame
        self.top=Frame(self,height=150,bg='gray')
        self.top.pack(fill=X) #fill x axis of top
        
        self.bottom=Frame(self,height=550,bg='#F791C4')
        self.bottom.pack(fill=X) #fill x axis of bottom
        
        #top frame design
        self.top_image=PhotoImage(file='icons/pep.png')
        self.top_image_label=Label(self.top, image=self.top_image,bg='gray')
        self.top_image_label.place(x=100,y=35)
        
        #header title
        self.heading=Label(self.top, text='My People',font='arial 18 bold',bg='gray',fg='#1EE921')
        self.heading.place(x=180,y=50)
        
        #scrolling
        self.scroll=Scrollbar(self.bottom, orient=VERTICAL)
        
        #add listbox
        self.listBox=Listbox(self.bottom, width=50,height=27) #60 char,max 27lines will show
        self.listBox.grid(row=0,column=0,padx=(40,0))
        
        self.scroll.config(command=self.listBox.yview)
        self.listBox.config(yscrollcommand=self.scroll.set)
        
                #query to view
        persons=cur.execute("select * from peoplee").fetchall()
        print(persons)
        count=0
        for person in persons:
            self.listBox.insert(count, str(person[0])+". "+person[1]+" "+person[2])
            count+=1
            
        self.scroll.grid(row=0,column=1,sticky=N+S)
        #end off add listbox
        
        #button_of_my_people
        self.btnadd =Button(self.bottom, text="ADD",width=12,font='arial 12 bold',bg='#F7D22B',command=self.add_people)
        self.btnadd.grid(row=0,column=2,padx=20,pady=10,sticky=N)
        
        self.btnupdate =Button(self.bottom, text="UPDATE",width=12,font='arial 12 bold',bg='#F7D22B',command=self.update_people)
        self.btnupdate.grid(row=0,column=2,padx=20,pady=70,sticky=N)
        
        self.btndisplay =Button(self.bottom, text="DISPLAY",width=12,font='arial 12 bold',bg='#F7D22B',command=self.display_people)
        self.btndisplay.grid(row=0,column=2,padx=20,pady=130,sticky=N)
        
        self.btndelete =Button(self.bottom, text="DELETE",width=12,font='arial 12 bold',bg='#F7D22B',command=self.delete_people)
        self.btndelete.grid(row=0,column=2,padx=20,pady=190,sticky=N)
        
    def add_people(self):
        add_page=AddPeople()
        self.destroy()
        
    def update_people(self):
        selected_item=self.listBox.curselection()
        person=self.listBox.get(selected_item)
        person_id = person.split(".")[0]
        
        updatepage=Update(person_id)
        
    def display_people(self):
        selected_item=self.listBox.curselection()
        person=self.listBox.get(selected_item)
        person_id = person.split(".")[0]
        
        displaypage=Display(person_id)
        
    def delete_people(self):
        selected_item=self.listBox.curselection()
        person=self.listBox.get(selected_item)
        person_id = person.split(".")[0]
        
        query="delete from peoplee where person_id={}".format(person_id)
        string_for_mbox="are you sure\nyou want to delete ",person.split(".")[1],"?"
        answer=messagebox.askquestion("Warning",string_for_mbox)
        
        if answer=='yes':
            try:
                cur.execute(query)
                con.commit()
                messagebox.showinfo("message","successfully deleted!")
                self.destroy()
            except EXCEPTION as e:
                messagebox.showerror("error",str(e))
        
        
        
        
        
        
        