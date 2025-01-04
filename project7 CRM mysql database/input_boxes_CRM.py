'''
Add a new column into table => use Alter (Alter means Add)
    mycur.execute("ALTER TABLE table_name ADD(col_name datatype,....)")

IF NOT EXISTS => if table is not exit
    mycur.execute("CREATE TABLE IF NOT EXITS table_name()")

In mysql to show column description => describe table_name

#Send data to database
mycur.execute("insert into table_name (col_name, col_name,...) VALUES(%s,%s,.....)",(data,data,....))
%s => placeholder is a container where data is inserted into it and sent to the database.

#update the data from the database
mycur.execute("UPDATE table_name SET col_name=%s, col_name=%s WHERE col_name=%s",(data, data, data))

#if input data is empty, messagebox will pop up
if not data.get():
    messagebox.showerror("Error Info","input box need to be filled out")
    return

#query (get the data from the table of database)
mycur.execute("SELECT * FROM table_name")
var_name =mycur.fetchall()

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
from tkinter import ttk,messagebox
import pymysql #database connection
import tree_view_table_all    #show record file
import table_search_item    #search item and show record
import csv

window = Tk()
window.title("Input box to database")
window.geometry("500x730+500+30")
window.configure(bg="#0c484b")
#window.resizable(False,False)


'''#window full screen
window.attributes('-fullscreen',True)'''


#db connect
mydb = pymysql.connect(
            host = "localhost",
            user = "root",
            passwd = "root",
            database ="codemy"
            
    )

#create cursor
mycur = mydb.cursor()

'''
#create database
mycur.execute("CREATE DATABASE codemy")
'''


'''
#DELETE existing table
mycur.execute("DROP TABLE customers")
'''


#CREATE TABLE
mycur.execute("""
                CREATE TABLE IF NOT EXISTS customers(
                user_id INT AUTO_INCREMENT PRIMARY KEY,
                first_name VARCHAR(255),
                last_name VARCHAR(255),
                address1 VARCHAR(255),
                address2 VARCHAR(255))""")

#ADD COLUMN


'''
#Add column in customer table using "Alter"
mycur.execute("""
                ALTER TABLE customers ADD(
                city varchar(255),
                state varchar(255),
                zipcode int(10),
                country varchar(255),
                phone varchar(255),
                email varchar(255),
                payment varchar(255),
                discount_code varchar(255),
                price_paid float(10,2))""")

'''

#SHOW COLUMN DESCRIPTION
'''
#show column
mycur.execute("select * FROM customers")
for des in mycur.description:
    print(des)
'''

#send input to the database, submit function start
def submit():
    
    #empty box check start
    #if input box is empty
    if (not first_name_box.get()
        or not last_name_box.get()
        or not address1_box.get()
        or not address2_box.get()
        or not city_box.get()
        or not state_box.get()
        or not zipcode_box.get()
        or not country_box.get()
        or not phone_box.get()
        or not email_box.get()
        or not payment_box.get()
        or not discount_code_box.get()
        or not price_paid_box.get()):
        messagebox.showerror("Error info","input box need to be fill out")
        return
    #empty box check end
    
    
    #zipcode and price_paid check start
    #if zipcode is not number
    zipcode = zipcode_box.get()
    if not zipcode.isdigit():
        messagebox.showerror("Error info","zipcode need to be integer between 0 and 9")
        return
        zipcode_box.focus_set()
    #if price_paid is not float or integer
    try:
        price_paid = float( price_paid_box.get())       # Convert to float
        if price_paid <0:
            messagebox.showerror("Error info","Price Paid cannot be negative")
            return
            price_paid_box.focus_set()
    except ValueError:
        messagebox.showerror("Error", "Price Paid must be a valid number.")
        return
        price_paid_box.focus_set()
    #zipcode and price_paid check end
    

    #insert into database start
    #col_name and placeholder %s 
    sql_column = """INSERT INTO customers (first_name,last_name,address1,address2,city,
                    state,zipcode,country,phone,email,payment,discount_code,price_paid)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    #user input
    data = (first_name_box.get(), last_name_box.get(), address1_box.get(), address2_box.get(),
            city_box.get(), state_box.get(), zipcode_box.get(), country_box.get(), phone_box.get(),
            email_box.get(), payment_box.get(), discount_code_box.get(), price_paid_box.get())
    #insert into the database
    mycur.execute(sql_column,data)
    #save the change to the database
    mydb.commit()
    
    #call clear_field() to clear the input box
    clear_field()
    #insert into database end
    
#submit function end
    

#clear text field function start
def clear_field():
    first_name_box.delete(0,END)
    last_name_box.delete(0,END)
    address1_box.delete(0,END)
    address2_box.delete(0,END)
    city_box.delete(0,END)
    state_box.delete(0,END)
    zipcode_box.delete(0,END)
    country_box.delete(0,END)
    phone_box.delete(0,END)
    email_box.delete(0,END)
    payment_box.delete(0,END)
    discount_code_box.delete(0,END)
    price_paid_box.delete(0,END)
#clear text field function end


#show_record function start
def show_record():
    record = Tk()
    record.title("Show User Records")
    record.geometry("1600x900")
    record.configure(bg="#0c484b")
        
    #get the data from the table of database (query)
    mycur.execute("SELECT * FROM customers")
    result = mycur.fetchall()

    #send to excel
    def excel():
        header = ['user_id','first_name','last_name','address1','address2','city',
                    'state','zipcode','country','phone','email','payment','discount_code','price_paid']
        # Open (or create) a file called 'output.csv' in write mode
        with open('export_excel.csv', mode='w', newline='') as file:  
            w = csv.writer(file)
            w.writerow(header)
            w.writerows(result)
        
    #frame
    excel_frame = Frame(record,bg="#0c484b")
    excel_frame.pack(fill="x")
    #create excel btn
    excel_btn = Button(excel_frame, text="Export Excel",bg="#fa9b43", fg="#0c484b" ,padx=10,pady=5, font=("Helvetica",10,"bold"),command=excel)
    excel_btn.pack(side="left",padx=20, pady=20)

    
    
    #call tree_table function from tree_view_table_all.file start
    #(record , result) parameter is needed to attach to use in tree_view_table file
    tree_view_table_all.tree_table(record,result)
    #call tree_table function from tree_view_table_all.file end

    
#show_record function end


#search customer start
def search_customer():
    
    #create another window
    global  search_w
    search_w = Tk()
    search_w.title("Search Customer")
    search_w.geometry("1600x900")
    search_w.configure(bg="#0c484b")
    def search_now():
        sql =""
        drop_box = drop.get()
        if drop_box == "Search By":
            messagebox.showerror("Error Info","Wrong Selection",parent=search_w)
            return
        elif drop_box == "First Name":
            sql = "SELECT * FROM customers WHERE first_name=%s"            
        elif drop_box == "Last Name":
            sql = "SELECT * FROM customers WHERE last_name=%s" 
        elif drop_box == "City":
            sql = "SELECT * FROM customers WHERE city=%s"
        elif drop_box == "Zipcode":
            sql = "SELECT * FROM customers WHERE zipcode=%s"
        #data from database
        search = customer_box.get()
        mycur.execute(sql, (search,))
        data = mycur.fetchall()
        if not data:
            data = []
            #Remove previous treeview table if it exits
            for widget in search_w.winfo_children():
                if isinstance(widget,ttk.Treeview):
                    widget.destroy()
            messagebox.showerror("Error Info", "No Customer found", parent=search_w)
        else:
            #display with table
              table_search_item.search_item(search_w, data)
            
    #create btn and input box, drop box (in frame1) start 
    #create frame1
    frame1 = Frame(search_w,bg="#0c484b")
    frame1.pack(fill="x")
    #search btn
    search = Button(frame1, text="Search",padx=10,bg="#fa9b43",fg="#0c484b" , font=("Helvetica",10,"bold"),command=search_now)
    search.pack(side="left", padx=(30,0), pady=20)
    #input box
    customer_box = Entry(frame1, width=40, bg="#577a7d",fg="#fa9b43",font=("Helvetica",10,"bold"))
    customer_box.pack(side="left", padx=20, pady=10)
    #drop box
    drop = ttk.Combobox(frame1,values=["Search By","First Name", "Last Name","City","Zipcode"])
    drop.pack(side="left", padx=(50,0), pady=10)
    drop.current(0)
    #create btn and input box, drop box (in frame1) end
    
    #create edit btn and user_id input box (in frame2) start
    #create frame2
    frame2 = Frame(search_w,bg="#0c484b")
    frame2.pack(fill="x", pady=(0,10))
    #edit btn
    edit_btn = Button(frame2, text="Edit",bg="#fa9b43",fg="#0c484b", font=("Helvetica",10,"bold"), width=8,command=edit)
    edit_btn.pack(side="left", padx=(30,0),pady=(0,10))
    #user_id_input box
    global user_id_box
    user_id_box = Entry(frame2, width=40,bg="#577a7d",fg="#fa9b43",font=("Helvetica",10,"bold"))
    user_id_box.pack(side="left",padx=20,pady=(0,10))
    #user_id label
    user_id = Label(frame2, text="ID",bg="#0c484b", fg="#fa9b43",font=("Helvetica",10,"bold"))
    user_id.pack(side="left")
    #create edit btn and user_id input box (in frame2) start
#search customer end

#edit function start
def edit():
    
    #get id 
    userID = user_id_box.get()
    #if user_id_box is not number
    if not userID.isdigit():
        messagebox.showerror("Error info", "ID is invalid", parent=search_w)
        return
        userID.focus()

    #create new window
    global edit_w
    edit_w = Tk()
    edit_w.title("Edit Customer records")
    edit_w.geometry("1600x900")
    edit_w.configure(bg="#0c484b")

    '''#close search customer window
    search_w.destroy()'''
    

    #get records from database
    mycur.execute("SELECT * FROM customers WHERE user_id=%s",(userID,))
    customer_edit = mycur.fetchall()
   

    # Get the first customer (there should only be one based on the user_id)
    customer = customer_edit[0]  # Extract the first tuple
    
    

    #create edit lable and input box on tkinter
    title = Label(edit_w,text="Update Customer Records",bg="#0c484b", fg="#f7f5f2", font=("Helvetica",16,"bold"))
    title.grid(row=0, column=0, columnspan=2, pady=10)
    #create edit_label
    first_name_edit_label = Label(edit_w, text="First Name",bg="#0c484b",fg="#ccdcdd", font=("Helvetica",12))
    first_name_edit_label.grid(row=1, column=0, sticky=W, padx=(10,20),pady=(0,10))

    last_name_edit_label = Label(edit_w, text="Last Name",bg="#0c484b",fg="#ccdcdd", font=("Helvetica",12))
    last_name_edit_label.grid(row=2, column=0, sticky=W, padx=(10,20),pady=(0,10))

    address1_edit_label = Label(edit_w, text="Address1",bg="#0c484b",fg="#ccdcdd", font=("Helvetica",12))
    address1_edit_label.grid(row=3, column=0, sticky=W, padx=(10,20),pady=(0,10))

    address2_edit_label = Label(edit_w, text="Address2",bg="#0c484b",fg="#ccdcdd", font=("Helvetica",12))
    address2_edit_label.grid(row=4, column=0, sticky=W, padx=(10,20),pady=(0,10))

    city_edit_label = Label(edit_w, text="City",bg="#0c484b",fg="#ccdcdd", font=("Helvetica",12))
    city_edit_label.grid(row=5, column=0, sticky=W, padx=(10,20),pady=(0,10))

    state_label = Label(edit_w, text="State",bg="#0c484b",fg="#ccdcdd", font=("Helvetica",12))
    state_label.grid(row=6, column=0, sticky=W, padx=(10,20),pady=(0,10))

    zipcode_edit_label = Label(edit_w, text="Zipcode",bg="#0c484b",fg="#ccdcdd", font=("Helvetica",12))
    zipcode_edit_label.grid(row=7, column=0, sticky=W, padx=(10,20),pady=(0,10))

    country_edit_label = Label(edit_w, text="Country",bg="#0c484b",fg="#ccdcdd", font=("Helvetica",12))
    country_edit_label.grid(row=8, column=0, sticky=W, padx=(10,20),pady=(0,10))

    phone_edit_label = Label(edit_w, text="Phone",bg="#0c484b",fg="#ccdcdd", font=("Helvetica",12))
    phone_edit_label.grid(row=9, column=0, sticky=W, padx=(10,20),pady=(0,10))

    email_label = Label(edit_w, text="Email",bg="#0c484b",fg="#ccdcdd", font=("Helvetica",12))
    email_label.grid(row=10, column=0, sticky=W, padx=(10,20),pady=(0,10))

    payment_edit_label = Label(edit_w, text="Payment",bg="#0c484b",fg="#ccdcdd", font=("Helvetica",12))
    payment_edit_label.grid(row=11, column=0, sticky=W, padx=(10,20),pady=(0,10))

    discount_code_label = Label(edit_w, text="Discount_code",bg="#0c484b",fg="#ccdcdd", font=("Helvetica",12))
    discount_code_label.grid(row=12, column=0, sticky=W, padx=(10,20),pady=(0,10))

    price_paid_edit_label = Label(edit_w, text="Price_paid",bg="#0c484b",fg="#ccdcdd", font=("Helvetica",12))
    price_paid_edit_label.grid(row=13, column=0, sticky=W, padx=(10,20),pady=(0,10))
    
    #create input box
    global first_name_edit_box
    first_name_edit_box = Entry(edit_w,width=40,bg="#577a7d",fg="#fa9b43",font=("Helvetica", 10,"bold"))
    first_name_edit_box.grid(row=1, column=1)

    global last_name_edit_box
    last_name_edit_box = Entry(edit_w,width=40,bg="#577a7d",fg="#fa9b43",font=("Helvetica", 10,"bold"))
    last_name_edit_box.grid(row=2, column=1)

    global address1_edit_box
    address1_edit_box = Entry(edit_w,width=40,bg="#577a7d",fg="#fa9b43",font=("Helvetica", 10,"bold"))
    address1_edit_box.grid(row=3, column=1)

    global address2_edit_box
    address2_edit_box = Entry(edit_w,width=40,bg="#577a7d",fg="#fa9b43",font=("Helvetica", 10,"bold"))
    address2_edit_box.grid(row=4, column=1)

    global city_edit_box
    city_edit_box = Entry(edit_w,width=40,bg="#577a7d",fg="#fa9b43",font=("Helvetica", 10,"bold"))
    city_edit_box.grid(row=5, column=1)

    global state_edit_box
    state_edit_box = Entry(edit_w,width=40,bg="#577a7d",fg="#fa9b43",font=("Helvetica", 10,"bold"))
    state_edit_box.grid(row=6, column=1)

    global zipcode_edit_box
    zipcode_edit_box = Entry(edit_w,width=40,bg="#577a7d",fg="#fa9b43",font=("Helvetica", 10,"bold"))
    zipcode_edit_box.grid(row=7, column=1)

    global country_edit_box
    country_edit_box = Entry(edit_w,width=40,bg="#577a7d",fg="#fa9b43",font=("Helvetica", 10,"bold"))
    country_edit_box.grid(row=8, column=1)

    global phone_edit_box
    phone_edit_box = Entry(edit_w,width=40,bg="#577a7d",fg="#fa9b43",font=("Helvetica", 10,"bold"))
    phone_edit_box.grid(row=9, column=1)

    global email_edit_box
    email_edit_box = Entry(edit_w,width=40,bg="#577a7d",fg="#fa9b43",font=("Helvetica", 10,"bold"))
    email_edit_box.grid(row=10, column=1)

    global payment_edit_box
    payment_edit_box = Entry(edit_w,width=40,bg="#577a7d",fg="#fa9b43",font=("Helvetica", 10,"bold"))
    payment_edit_box.grid(row=11, column=1)

    global discount_code_edit_box
    discount_code_edit_box = Entry(edit_w,width=40,bg="#577a7d",fg="#fa9b43",font=("Helvetica", 10,"bold"))
    discount_code_edit_box.grid(row=12, column=1)

    global price_paid_edit_box
    price_paid_edit_box = Entry(edit_w,width=40,bg="#577a7d",fg="#fa9b43",font=("Helvetica", 10,"bold"))
    price_paid_edit_box.grid(row=13, column=1)

    # Insert customer data into entry boxes
    first_name_edit_box.insert(0, customer[1])
    last_name_edit_box.insert(0, customer[2])
    address1_edit_box.insert(0, customer[3])
    address2_edit_box.insert(0, customer[4])
    city_edit_box.insert(0, customer[5])
    state_edit_box.insert(0, customer[6])
    zipcode_edit_box.insert(0, customer[7])
    country_edit_box.insert(0, customer[8])
    phone_edit_box.insert(0, customer[9])
    email_edit_box.insert(0, customer[10])
    payment_edit_box.insert(0, customer[11])
    discount_code_edit_box.insert(0, customer[12])
    price_paid_edit_box.insert(0, customer[13])

    #save btn
    save_edit_btn = Button(edit_w, text="Save", padx=10, width=30,bg="#fa9b43", fg="#0c484b" ,font=("Helvetica", 10,"bold"), command=save)
    save_edit_btn.grid(row=15, column=1, pady=10)
#edit function end

#save function
def save():
    #USER ID
    userID = user_id_box.get()
    
    #empty box check start
    #if input box is empty
    if (not first_name_edit_box.get()
        or not last_name_edit_box.get()
        or not address1_edit_box.get()
        or not address2_edit_box.get()
        or not city_edit_box.get()
        or not state_edit_box.get()
        or not zipcode_edit_box.get()
        or not country_edit_box.get()
        or not phone_edit_box.get()
        or not email_edit_box.get()
        or not payment_edit_box.get()
        or not discount_code_edit_box.get()
        or not price_paid_edit_box.get()):
        messagebox.showerror("Error info","input box need to be fill out", parent=edit_w)
        return
    #empty box check end
    
    #zipcode and price_paid check start
    #if zipcode is not number
    zipcode = zipcode_edit_box.get()
    if not zipcode.isdigit():
        messagebox.showerror("Error info","zipcode need to be integer between 0 and 9", parent=edit_w)
        zipcode_edit_box.focus_set()        
        return
        
    #if price_paid is not float or integer
    try:
        price_paid = float( price_paid_edit_box.get())       # Convert to float
        if price_paid <0:
            messagebox.showerror("Error info","Price Paid cannot be negative",parent=edit_w)
            price_paid_edit_box.focus_set()
            return
            
    except ValueError:
        messagebox.showerror("Error", "Price Paid must be a valid number.",parent=edit_w)
        price_paid_edit_box.focus_set()        
        return
        
    #zipcode and price_paid check end

    #insert update data into database start
    sql_update = """
                    UPDATE customers SET
                    first_name=%s, last_name=%s, address1=%s,
                    address2=%s,city=%s,state=%s,zipcode=%s,country=%s,phone=%s,
                    email=%s,payment=%s,discount_code=%s,price_paid=%s
                    WHERE user_id=%s
                """
    #user input
    data = (first_name_edit_box.get(),last_name_edit_box.get(),address1_edit_box.get(),
            address2_edit_box.get(),city_edit_box.get(),state_edit_box.get(),zipcode_edit_box.get(),
            country_edit_box.get(),phone_edit_box.get(),email_edit_box.get(),payment_edit_box.get(),
            discount_code_edit_box.get(),price_paid_edit_box.get(), user_id_box.get() 
            )
    #insert to database
    mycur.execute(sql_update,data)
    #save change
    mydb.commit()

    #close edit_w(update data) and search_w(search customer) window
    search_w.destroy()
    edit_w.destroy()
    

#create Label and input box on tkinter start
#create title
title = Label(window,text="Codemy Customer Database",bg="#0c484b", fg="#f7f5f2", font=("Helvetica",16,"bold"))
title.grid(row=0, column=0, columnspan=2, pady=10)
#create label
first_name_label = Label(window, text="First Name",bg="#0c484b",fg="#ccdcdd", font=("Helvetica",12))
first_name_label.grid(row=1, column=0, sticky=W, padx=(10,20),pady=(0,10))

last_name_label = Label(window, text="Last Name",bg="#0c484b",fg="#ccdcdd", font=("Helvetica",12))
last_name_label.grid(row=2, column=0, sticky=W, padx=(10,20),pady=(0,10))

address1_label = Label(window, text="Address1",bg="#0c484b",fg="#ccdcdd", font=("Helvetica",12))
address1_label.grid(row=3, column=0, sticky=W, padx=(10,20),pady=(0,10))

address2_label = Label(window, text="Address2",bg="#0c484b",fg="#ccdcdd", font=("Helvetica",12))
address2_label.grid(row=4, column=0, sticky=W, padx=(10,20),pady=(0,10))

city_label = Label(window, text="City", bg="#0c484b",fg="#ccdcdd",font=("Helvetica",12))
city_label.grid(row=5, column=0, sticky=W, padx=(10,20),pady=(0,10))

state_label = Label(window, text="State", bg="#0c484b",fg="#ccdcdd",font=("Helvetica",12))
state_label.grid(row=6, column=0, sticky=W, padx=(10,20),pady=(0,10))

zipcode_label = Label(window, text="Zipcode",bg="#0c484b",fg="#ccdcdd", font=("Helvetica",12))
zipcode_label.grid(row=7, column=0, sticky=W, padx=(10,20),pady=(0,10))

country_label = Label(window, text="Country",bg="#0c484b",fg="#ccdcdd", font=("Helvetica",12))
country_label.grid(row=8, column=0, sticky=W, padx=(10,20),pady=(0,10))

phone_label = Label(window, text="Phone",bg="#0c484b", fg="#ccdcdd",font=("Helvetica",12))
phone_label.grid(row=9, column=0, sticky=W, padx=(10,20),pady=(0,10))

email_label = Label(window, text="Email",bg="#0c484b",fg="#ccdcdd", font=("Helvetica",12))
email_label.grid(row=10, column=0, sticky=W, padx=(10,20),pady=(0,10))

payment_label = Label(window, text="Payment",bg="#0c484b",fg="#ccdcdd", font=("Helvetica",12))
payment_label.grid(row=11, column=0, sticky=W, padx=(10,20),pady=(0,10))

discount_code_label = Label(window, text="Discount_code",bg="#0c484b",fg="#ccdcdd", font=("Helvetica",12))
discount_code_label.grid(row=12, column=0, sticky=W, padx=(10,20),pady=(0,10))

price_paid_label = Label(window, text="Price_paid",bg="#0c484b", fg="#ccdcdd",font=("Helvetica",12))
price_paid_label.grid(row=13, column=0, sticky=W, padx=(10,20),pady=(0,10))

#create input box
first_name_box = Entry(window,width=40, bg="#577a7d",fg="#fa9b43", font=("Helvetica", 10,"bold"))
first_name_box.grid(row=1, column=1)

last_name_box = Entry(window,width=40,bg="#577a7d",fg="#fa9b43",font=("Helvetica", 10,"bold"))
last_name_box.grid(row=2, column=1)

address1_box = Entry(window,width=40,bg="#577a7d",fg="#fa9b43",font=("Helvetica", 10,"bold"))
address1_box.grid(row=3, column=1)

address2_box = Entry(window,width=40,bg="#577a7d",fg="#fa9b43",font=("Helvetica", 10,"bold"))
address2_box.grid(row=4, column=1)

city_box = Entry(window,width=40,bg="#577a7d",fg="#fa9b43",font=("Helvetica", 10,"bold"))
city_box.grid(row=5, column=1)

state_box = Entry(window,width=40,bg="#577a7d",fg="#fa9b43",font=("Helvetica", 10,"bold"))
state_box.grid(row=6, column=1)

zipcode_box = Entry(window,width=40,bg="#577a7d",fg="#fa9b43",font=("Helvetica", 10,"bold"))
zipcode_box.grid(row=7, column=1)

country_box = Entry(window,width=40,bg="#577a7d",fg="#fa9b43",font=("Helvetica", 10,"bold"))
country_box.grid(row=8, column=1)

phone_box = Entry(window,width=40,bg="#577a7d",fg="#fa9b43",font=("Helvetica", 10,"bold"))
phone_box.grid(row=9, column=1)

email_box = Entry(window,width=40,bg="#577a7d",fg="#fa9b43",font=("Helvetica", 10,"bold"))
email_box.grid(row=10, column=1)

payment_box = Entry(window,width=40,bg="#577a7d",fg="#fa9b43",font=("Helvetica", 10,"bold"))
payment_box.grid(row=11, column=1)

discount_code_box = Entry(window,width=40,bg="#577a7d",fg="#fa9b43",font=("Helvetica", 10,"bold"))
discount_code_box.grid(row=12, column=1)

price_paid_box = Entry(window,width=40,bg="#577a7d",fg="#fa9b43",font=("Helvetica", 10,"bold"))
price_paid_box.grid(row=13, column=1)
#create Label and input box on tkinter end


#Button start
#crate btn frame
btn_frame = Frame(window, padx=20, pady=20,bg="#0c484b")
btn_frame.grid(row=14, column=0,columnspan=3, sticky="ew")
#submit buttom
submit = Button(btn_frame, text="Submit",bg="#fa9b43", fg="#0c484b" ,font=("Helvetica", 10), padx=20, width=10, command = submit )
submit.grid(row=0, column=0,padx=10)

#clear button
clear = Button(btn_frame, text="Clear",bg="#fa9b43", fg="#0c484b",font=("Helvetica", 10), padx=20, width=10, command=clear_field )
clear.grid(row=0, column=1, padx=10)

#show record button
record = Button(btn_frame, text="Show Record",bg="#fa9b43", fg="#0c484b", font=("Helvetica",10), padx=20, command=show_record)
record.grid(row=0, column=2, padx=10)

#search btn
search_btn = Button(btn_frame, text="Search Customer",bg="#fa9b43", fg="#0c484b",font=("Helvetica",10), padx=10,command=search_customer )
search_btn.grid(row=1, column=0,pady=20)



window.mainloop()
