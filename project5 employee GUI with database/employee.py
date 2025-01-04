'''
Add a new column into table => use Alter (Alter means Add)
    mycur.execute("ALTER TABLE table_name ADD(col_name datatype,....)")

IF NOT EXISTS => if table is not exit
    mycur.execute("CREATE TABLE IF NOT EXITS table_name()")

In mysql to show column description => describe table_name

#Send data to database
mycur.execute("insert into table_name (col_name, col_name,...) VALUES(%s,%s,.....)",(data,data,....))
mydb.commit()
%s => placeholder is a container where data is inserted into it and sent to the database.

#update the data from the database
mycur.execute("UPDATE table_name SET col_name=%s, col_name=%s WHERE col_name=%s",(data, data, data))
mydb.commit()

#Delete Data from database
mycur.execute("DELETE FROM table_name WHERE col_name=value")
mydb.commit()

#query (get the data from the table of database)
mycur.execute("SELECT * FROM table_name")
var_name =mycur.fetchall()

#if input data is empty, messagebox will pop up
if not data.get():
    messagebox.showerror("Error Info","input box need to be filled out")
    return



#try and except
try:
    # code that may raise exceptions
except ValueError:
    # handle ValueError
except TypeError:
    # handle TypeError
except Exception:
    # handle any other exception

'''


from tkinter import *
from tkinter import ttk, messagebox
import pymysql

window = Tk()
window.title("Employee GUI App")
window.geometry("650x270+400+200")
window.config(bg="#364430")

#database connection
mydb = pymysql.connect(
                host = "localhost",
                user = "root",
                passwd = "root",
                database = "employee_Facts"

    )

#create cursor
mycur = mydb.cursor()

'''
#create database
mycur.execute("CREATE DATABASE employee_Facts" )
'''

'''
#create table
mycur.execute("""CREATE TABLE empDetails(
                empID int AUTO_INCREMENT PRIMARY KEY,
                empName varchar(100),
                empDept varchar (100)) """)
'''

#function start

#insertData
def insertData():
    name = empName.get()
    dept = empDept.get()

    #if the input box is empty
    if (name=="" or dept==""):
        messagebox.showerror("Error Info","All the fields are required")
        return
        empName.focus()
        empDept.focus()
        
    else:    
        #insert employee data into database
        mycur.execute("INSERT INTO empDetails (empName,empDept) VALUES (%s,%s)",(name,dept))
        mydb.commit()

        #delete the data on the input box
        empName.delete(0,END)
        empDept.delete(0,END)

        #message for data insert sucessfully
        messagebox.showinfo("Status","Sucessfully inserted")


#record 
def showRecord():
    
    #get data from database
    mycur.execute("SELECT * FROM empdetails")
    result = mycur.fetchall()

    #display on the list box
    showData.delete(0,showData.size())   #delete previous record

    #insert data into the list box
    for row in result:
        showData.insert("end",f"     {row[0]}   {row[1]}  |  {row[2]}")

        
#edit start
#Edit box
def editBox():
    global edit_window
    edit_window = Tk()
    edit_window.title("Edit Employee Facts")
    edit_window.geometry("365x200+420+240")
    edit_window.config(bg="#364430")


    #change the employee data
    global id_input
    #edit label
    edit_ID = Label(edit_window, text="ID",font=("Serif",12),bg="#364430", fg="#ffdebc")
    edit_ID.place(x=20, rely=0.2, anchor="n")
    #id input box
    id_input = Entry(edit_window,width=23,font=("Serif",12),bg="#8bb585", fg="#364430")
    id_input.place(x=170,rely=0.2, anchor="n")
    id_input.focus()
    #submit btn
    submit = Button(edit_window, text="Submit",padx=15, bd=0, activebackground="#8bb585",font=("Sans",10), bg="#ffdebc", fg="#364430",command=editData)
    submit.place(relx=0.4, y=90)

#editData
def editData():
    
    #get Id from edit page
    global empId
    empId = id_input.get()

    if empId =="":
        messagebox.showerror("Error Info","ID need to be fill!",parent=edit_window)
    else:
        #get row from the database
        mycur.execute(f"SELECT * FROM empdetails WHERE empID={empId}")
        row = mycur.fetchall()

        #close the edit window
        edit_window.destroy()

        #insert into the input box (empName,empDept)
        for i in row:
            empName.insert(0,i[1])
            empDept.insert(0,i[2])
#edit end


#updateData function
def updateData():
    name = empName.get()
    dept = empDept.get()
    #if the input box is empty
    if (name=="" or dept==""):
        messagebox.showerror("Error Info","All the fields are required")
        return
        empName.focus()
        empDept.focus()  
    else:
        #update data into the database
        mycur.execute(f"UPDATE empDetails SET empName=%s, empDept=%s WHERE empID=%s",(name,dept,empId))
        #save change
        mydb.commit()
        
        #clear the input box
        empName.delete(0,END)
        empDept.delete(0,END)
        
        #messagebox
        messagebox.showinfo("Info","Successfully Updated")


#delete start
#delete box
def deleteBox():
    global delete_window
    delete_window = Tk()
    delete_window.title("Delete Employee Facts")
    delete_window.geometry("365x200+420+240")
    delete_window.config(bg="#364430")

    #change the employee data
    global id_input
    #edit label
    delete_ID = Label(delete_window, text="ID",font=("Serif",12),bg="#364430", fg="#ffdebc")
    delete_ID.place(x=20, rely=0.2, anchor="n")
    #id input box
    id_input = Entry(delete_window,width=23,font=("Serif",12),bg="#8bb585", fg="#364430")
    id_input.place(x=170,rely=0.2, anchor="n")
    id_input.focus()
    #submit btn
    submit = Button(delete_window, text="Submit",padx=15, bd=0, activebackground="#8bb585",font=("Sans",10), bg="#ffdebc", fg="#364430",command=deleteData)
    submit.place(relx=0.4, y=90)

#deleteData
def deleteData():
    #get id from the delete box
    deleteID = id_input.get()

    if deleteID=="":
        messagebox.showerror("Error Info","ID need to be fill!",parent=delete_window)
    else:    
        #delete from the database
        mycur.execute(f"DELETE FROM empDetails WHERE empID ={deleteID}")
        mydb.commit()
        
        #close the delete window
        delete_window.destroy()
        
        #message box
        messagebox.showinfo("Info","Successfully Deleted")
#delete end


#Reset
def reset():
    empName.delete(0,END)
    empDept.delete(0,END)

    

#search start
#search data
def searchData():
    sql=""
    drop_box = drop.get()
    search_box = search.get()
    
    if drop_box=="Search By":
        messagebox.showerror("Error","Wrong Selection",parent=search_window)
        return
    if search_box=="":
        messagebox.showerror("Error","Search box is empty",parent=search_window)
        return
    
    if drop_box =="empName":
        sql = "SELECT * FROM empDetails WHERE empName=%s"
    elif drop_box =="empDept":
        sql = "SELECT * FROM empDetails WHERE empDept=%s"

    #get data from database
    mycur.execute(sql,(search_box,))
    data = mycur.fetchall()

    #if no data is found in database
    if not data:
        showData.delete(0,showData.size())   #delete previous record
        messagebox.showerror("Error Info", "No Employee found", parent=search_window)
        return
    else:
        #display on the list box
        showData.delete(0,showData.size())   #delete previous record

        #insert data into the list box
        for idx, row in enumerate(data):
            showData.insert("end",f"     {row[0]}   {row[1]}  |  {row[2]}")
        #close the window
        search_window.destroy()

#search box
def searchBox():
    global search_window
    search_window = Tk()
    search_window.title("Edit Employee Facts")
    search_window.geometry("365x200+420+240")
    search_window.config(bg="#364430")


    global drop,search
    #drop box
    drop = ttk.Combobox(search_window,values=["Search By","empName","empDept"],font=("Serif",12))
    drop.place(x=210,y=30,anchor="n")
    drop.current(0)
    #search label
    search_label = Label(search_window, text="Search",font=("Serif",12),bg="#364430", fg="#ffdebc")
    search_label.place(x=50, y=100, )
    #search input box
    search = Entry(search_window,width=22,font=("Serif",12),bg="#8bb585", fg="#364430")
    search.place(x=210,y=100, anchor="n")
    search.focus()
    #submit btn
    submit = Button(search_window, text="Submit",padx=15, bd=0, activebackground="#8bb585",font=("Sans",10), bg="#ffdebc", fg="#364430",command=searchData)
    submit.place(relx=0.4, y=150)
#search end


#editData
def editData():
    
    #get Id from edit page
    global empId
    empId = id_input.get()

    if empId =="":
        messagebox.showerror("Error Info","ID need to be fill!",parent=edit_window)
    else:
        #get row from the database
        mycur.execute(f"SELECT * FROM empdetails WHERE empID={empId}")
        row = mycur.fetchall()

        #close the edit window
        edit_window.destroy()

        #insert into the input box (empName,empDept)
        for i in row:
            empName.insert(0,i[1])
            empDept.insert(0,i[2])
#edit end

    
#function end


#create GUI start
#input start
#name
empName_label = Label(window,text="Employee Name:", font=("Serif",12),bg="#364430", fg="#ffdebc")
empName_label.place(x=20, y=30)
empName = Entry(window,width=23,font=("Serif",12),bg="#8bb585", fg="#364430")
empName.place(x=170, y=30)
empName.focus()

#dept
empDept_label = Label(window, text="Employee Dept:",font=("Serif",12),bg="#364430", fg="#ffdebc")
empDept_label.place(x=20, y=80)
empDept = Entry(window,width=23,font=("Serif",12),bg="#8bb585", fg="#364430")
empDept.place(x=170, y=80)
#input end

#btn start
#insert btn
insert_btn = Button(window,text="Insert",padx=15, bd=0, activebackground="#8bb585",font=("Sans",10), bg="#ffdebc", fg="#364430", command=insertData)
insert_btn.place(x=20, y=160)
#update btn
update_btn = Button(window, text="Update",padx=15,bd=0, activebackground="#8bb585", font=("Sans",10), bg="#ffdebc", fg="#364430",command=updateData)
update_btn.place(x=110, y=160)
#get btn
get_btn = Button(window, text="Record",padx=13, bd=0, activebackground="#8bb585",font=("Sans",10), bg="#ffdebc", fg="#364430", command=showRecord)
get_btn.place(x=210,y=160)
#delete btn
delete_btn = Button(window, text="Delete",padx=15, bd=0, activebackground="#8bb585",font=("Sans",10), bg="#ffdebc", fg="#364430",command=deleteBox)
delete_btn.place(x=305, y=160)
#reset btn
reset_btn = Button(window, text="Reset",padx=14, bd=0, activebackground="#8bb585",font=("Sans",10), bg="#ffdebc", fg="#364430",command=reset)
reset_btn.place(x=20, y=210)
#edit btn
edit_btn = Button(window, text="Edit",padx=24, bd=0, activebackground="#8bb585",font=("Sans",10), bg="#ffdebc", fg="#364430", command=editBox)
edit_btn.place(x=110,y=210)
#search btn
search_btn = Button(window, text="Search",padx=13, bd=0, activebackground="#8bb585",font=("Sans",10), bg="#ffdebc", fg="#364430", command=searchBox)
search_btn.place(x=210,y=210)
#btn end

#List box start
showData = Listbox(window,height=11, width=30,bd=0, bg="#ffdebc", fg="#364430")
showData.place(x=430, y=30)






window.mainloop()
