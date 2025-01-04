'''
sqlite3
import sqlite3

connect or create a database
myDB= sqlite3.connect('address_book.db')

#cursor (send data to database)
myCur= myDB.cursor()

#create table
myCur.execute(""" CREATE TABLE address(

                first_name text,
                last_name text,
                address text,
                city text,
                state text,
                zipcode integer)""")

#insert into table
myCur.execute("INSERT INTO table_name values(:input_box, :input_box,....)")

#query from the database
myCur.execute("SELECT *,oid FROM table_name")   => oid = primary key
#get all the data form database
myCur.fetchall() , myCur.fetchone(), myCur.fetchmany(number_of_record)

#update the record of database
myCur.execute("""UPDATE table_name SET
               col_name = :value_assign
               first_name = :first,
               .,
               .,
               .
               WHERE col_name = value""",
                {
                    'first' = f_name_edit.get()
                }
               )

#delete the record of database
myCur.execute("DELETE FROM address WHERE col_name")

#save database
myDB.commit()

#close database connection
myDB.close()

'''

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image
import sqlite3

window = Tk()
window.title("create a database")
window.config(bg="#fffdd0")
#window.geometry("400x400")

#connect
myDB = sqlite3.connect('address_book.db')

#create cursor
myCur = myDB.cursor()

'''
#create table execute
myCur.execute(""" CREATE TABLE address(
                first_name text,
                last_name text,
                address text,
                city text,
                state text,
                zipcode integer)""")
'''
# Declare the treeview globally
tree = None

#save edit record on database
def save():
    #connect
    myDB = sqlite3.connect("address_book.db")
    #cursor
    myCur = myDB.cursor()

    #update record
    myCur.execute(""" UPDATE address SET
                    first_name = :first,
                    last_name = :last,
                    address = :address,
                    city = :city,
                    state = :state,
                    zipcode = :zipcode
                    WHERE oid = :oid """,

                  {     'first'   : f_name_edit.get(),
                        'last'    : l_name_edit.get(),
                        'address' : address_edit.get(),
                        'city'    : city_edit.get(),
                        'state'   : state_edit.get(),
                        'zipcode' : zipcode_edit.get(),
                        'oid'     : id_box.get()
                    
                        })
    
    #commit
    myDB.commit()
    #close
    myDB.close()
    #exit from the editor window
    editor.destroy()

#edit function
def edit():
    global editor
    editor = Tk()
    editor.title("Edit Field")
    editor.config(bg="#fffdd0")
    editor.geometry("350x350")

    #create global variables for edit text box name
    global f_name_edit
    global l_name_edit
    global address_edit
    global city_edit
    global state_edit
    global zipcode_edit

    f_name_label = Label(editor, text="First Name")
    f_name_label.grid(row=0, column=0,padx=10, pady=(20,10),sticky=W)
    f_name_edit = Entry(editor,width=40)
    f_name_edit.grid(row=0, column=1, columnspan=2, padx=10, pady=(20,10))

    l_name_label = Label(editor, text="Last Name")
    l_name_label.grid(row=1, column=0,padx=10, pady=10,sticky=W)
    l_name_edit= Entry(editor,width=40)
    l_name_edit.grid(row=1, column=1, columnspan=2, padx=10, pady=5)

    address_label = Label(editor, text="Address")
    address_label.grid(row=2, column=0,padx=10, pady=10,sticky=W)
    address_edit= Entry(editor,width=40)
    address_edit.grid(row=2, column=1, columnspan=2, padx=10, pady=5)

    city_label = Label(editor, text="City")
    city_label.grid(row=3, column=0,padx=10, pady=10,sticky=W)
    city_edit = Entry(editor,width=40)
    city_edit.grid(row=3, column=1, columnspan=2, padx=10, pady=5)

    state_label = Label(editor, text="State")
    state_label.grid(row=4, column=0,padx=10, pady=10,sticky=W)
    state_edit = Entry(editor,width=40)
    state_edit.grid(row=4, column=1, columnspan=2, padx=10, pady=5)

    zipcode_label = Label(editor, text="Zipcode")
    zipcode_label.grid(row=5, column=0,padx=10, pady=10,sticky=W)
    zipcode_edit = Entry(editor,width=40)
    zipcode_edit.grid(row=5, column=1, columnspan=2, padx=10, pady=5)

    #save btn
    save_btn = Button(editor, text="Save",bg="#ffa756", command=save)
    save_btn.grid(row=6,column=0,columnspan=3, padx=10,pady=10, sticky="we")
        

    #connect database
    myDB = sqlite3.connect("address_book.db")
    #create cursor
    myCur = myDB.cursor()

    #put the record into the box
    record_id = id_box.get()
    myCur.execute("SELECT * FROM address WHERE oid=" + record_id )
    #get all column with the id number
    records= myCur.fetchall()

    #insert into the input box
    for record in records:
        f_name_edit.insert(0,record[0])
        l_name_edit.insert(0,record[1])
        address_edit.insert(0,record[2])
        city_edit.insert(0,record[3])
        state_edit.insert(0,record[4])
        zipcode_edit.insert(0,record[5])
    
    #commit
    myDB.commit()
    #close
    myDB.close()


#submit function
def submit():
    #connect
    myDB = sqlite3.connect('address_book.db')
    #create cursor
    myCur = myDB.cursor()
    #insert into database
    #if input is empty
    if not f_name.get() or not l_name.get() or not address.get() or not city.get() or not state.get() or not zipcode.get():
        messagebox.showerror("Error Info","input box need to be filled out")
        return
    myCur.execute("INSERT INTO address values(:f_name, :l_name, :address, :city, :state, :zipcode)",
                    {
                        'f_name':f_name.get(),
                        'l_name':l_name.get(),
                        'address':address.get(),
                        'city':city.get(),
                        'state' : state.get(),
                        'zipcode' :zipcode.get()
                        })
    #commit
    myDB.commit()
    #close
    myDB.close()

    #clear all the thing in the input box when submit button is clicked
    #input_box.delete(0,END)
    f_name.delete(0,END)
    l_name.delete(0,END)
    address.delete(0,END)
    city.delete(0,END)
    state.delete(0,END)
    zipcode.delete(0,END)


#query function
def query():
    # Clear previous records
    for record in tree.get_children():
        tree.delete(record)  # Remove all existing records in the Treeview
        
    #connect to database
    myDB = sqlite3.connect('address_book.db')
    #create cursor
    myCur = myDB.cursor()

    #query
    myCur.execute("SELECT *,oid FROM address")
    #get all the data
    records = myCur.fetchall()

    #insert the data on the tkinter column
    for record in records:
        tree.insert("", END, values=record)

    #commit (save data to the database)
    myDB.commit()
    #close database
    myDB.close()

  

# Treeview for displaying records
columns = ("First Name", "Last Name", "Address", "City", "State", "Zipcode","ID")
tree = ttk.Treeview(window, columns=columns, show='headings')
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, anchor="center")
tree.grid(row=10, column=0, columnspan=7, padx=10, pady=10)
# Set the treeview height
tree.config(height=10)


#delete function
def delete():
    #connect database
    myDB = sqlite3.connect('address_book.db')
    #create cursor
    myCur = myDB.cursor()
    #delete
    myCur.execute("DELETE FROM address WHERE oid=" + id_box.get() )

    #clear the input box
    id_box.delete(0,END)
    
    #commit
    myDB.commit()
    #close
    myDB.close()
    



#GUI
f_name_label = Label(window, text="First Name")
f_name_label.grid(row=0, column=2,padx=10, pady=(20,10),sticky=W)
f_name = Entry(window,width=40)
f_name.grid(row=0, column=3, columnspan=2, padx=10, pady=(20,10))

l_name_label = Label(window, text="Last Name")
l_name_label.grid(row=1, column=2,padx=10, pady=10,sticky=W)
l_name= Entry(window,width=40)
l_name.grid(row=1, column=3, columnspan=2, padx=10, pady=5)

address_label = Label(window, text="Address")
address_label.grid(row=2, column=2,padx=10, pady=10,sticky=W)
address= Entry(window,width=40)
address.grid(row=2, column=3, columnspan=2, padx=10, pady=5)

city_label = Label(window, text="City")
city_label.grid(row=3, column=2,padx=10, pady=10,sticky=W)
city = Entry(window,width=40)
city.grid(row=3, column=3, columnspan=2, padx=10, pady=5)

state_label = Label(window, text="State")
state_label.grid(row=4, column=2,padx=10, pady=10,sticky=W)
state = Entry(window,width=40)
state.grid(row=4, column=3, columnspan=2, padx=10, pady=5)

zipcode_label = Label(window, text="Zipcode")
zipcode_label.grid(row=5, column=2,padx=10, pady=10,sticky=W)
zipcode = Entry(window,width=40)
zipcode.grid(row=5, column=3, columnspan=2, padx=10, pady=5)

id_label = Label(window, text="ID")
id_label.grid(row=8,column=2, padx=10, pady=5,sticky=W)
id_box = Entry(window,width=40)
id_box.grid(row=8,column=2, padx=10, pady=5)

#submit btn
submit_btn = Button(window, text="Submit",bg="#ffa756",  command=submit)
submit_btn.grid(row=6,column=2,columnspan=3, padx=10,pady=10, sticky="we")

#query btn
query_btn = Button(window, text="Show Records",bg="#ffa756" ,command=query)
query_btn.grid(row=7, column=2, columnspan=3, padx=10, pady=10, sticky="we")

#delete btn
delete_btn = Button(window, text="Delete",bg="#ffa756" ,command=delete)
delete_btn.grid(row=8, column=4,padx=10,pady=10, sticky="we")

#update (edit) btn
edit_btn = Button(window, text="Edit",bg="#87c55f", command=edit)
edit_btn.grid(row=8, column=3, padx=10, pady=10, sticky="we")



#commit (save to the database)
myDB.commit()

#close
myDB.close()



window.mainloop()


