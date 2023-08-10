from tkinter import messagebox
from tkinter import ttk
import customtkinter as ctk
from MainFunction import appender
import sqlite3


background='#008080'

root=ctk.CTk()
root.title('Expense Tracker')
root.geometry('600x450')
root.resizable(False,False)
root.attributes('-alpha', 0.7)
root.config(relief='groove',bg=background)


frame=ctk.CTkFrame(root,fg_color='#008080',bg_color='#008080',width=600,height=160)
frame.place(y=320,x=1)

NameOfProduct=ctk.CTkEntry(frame,width=120,height=20,fg_color='#008080',placeholder_text="Product Name",font=('Arial',18))
NameOfProduct.place(y=60,x=20)

Amount=ctk.CTkEntry(frame,width=120,height=20,fg_color='#008080',placeholder_text="Amount",font=('Arial',18))
Amount.place(y=60,x=170)

Location=ctk.CTkEntry(frame,width=120,height=20,fg_color='#008080',placeholder_text="Location",font=('Arial',18))
Location.place(y=60,x=325)

Date=ctk.CTkEntry(frame,width=120,height=20,fg_color='#008080',placeholder_text="Date",font=('Arial',17))
Date.place(y=60,x=475)

Frame=ctk.CTkFrame(root,width=600,height=320,fg_color='#008080')
Frame.pack()



tree=ttk.Treeview(Frame)
tree['columns']=("Purchase id",'Name Of Product','Amount','Location','Date')
tree['show']='headings'

tree.column('Purchase id',width=100,minwidth=50,anchor=ctk.CENTER)
tree.column('Name Of Product',width=100,minwidth=50,anchor=ctk.CENTER)
tree.column('Amount',width=100,minwidth=50,anchor=ctk.CENTER)
tree.column('Location',width=100,minwidth=50,anchor=ctk.CENTER)
tree.column('Date',width=100,minwidth=50,anchor=ctk.CENTER)

tree.heading('Purchase id',text='Purchase id',anchor=ctk.CENTER)
tree.heading('Name Of Product',text='Name Of Product',anchor=ctk.CENTER)
tree.heading('Amount',text='Amount',anchor=ctk.CENTER)
tree.heading('Location',text='Location',anchor=ctk.CENTER)
tree.heading('Date',text='Date',anchor=ctk.CENTER)

def update(rows):
    for i in rows:
        tree.insert('', 'end', values=i)

con=sqlite3.connect('receipt.db')
cursor=con.cursor()

query = "SELECT * FROM ProductRecords"
cursor.execute(query)
rows = cursor.fetchall()
update(rows)

tree.place(width=600,height=320,x=0.1,y=1)



def save_record():
    
    name=NameOfProduct.get()
    amount=Amount.get()
    location=Location.get()
    date=Date.get()
    
    if name == "":
        messagebox.showerror(root,'Erorr','Please Enter Something')
    elif amount == "":
        messagebox.showerror(root,'Erorr','Please Enter Something')
    elif location == "":
        messagebox.showerror(root,'Erorr','Please Enter Something')
    elif date =="":
        messagebox.showerror(root,'Erorr','Please Enter Something')
        
    elif not name.isdigit:
        messagebox.showerror(root,'Erorr','Please Enter a Name')
        
    
    
    Records=(name,amount,location,date)
    
    
    appender(Records)
    

button=ctk.CTkButton(frame,text='Save Record',font=('Arial',16),command=save_record)
button.place(y=15,x=220)


    


    

root.mainloop()