from tkinter import *
from tkinter import ttk

def tree_table(record,result):
    #treeview start

    # Set up Treeview
    tree = ttk.Treeview(record,height=len(result))
    tree["columns"] = ("user_id", "first_name", "last_name", "address1", "address2",
                       "city", "state", "zipcode","country","phone","email","payment",
                       "discount_code","price_paid") 

    # Set up custom style for the Treeview
    style = ttk.Style(record)    
    
    #set style for background
    style.configure("Treeview",
                    font=("Helvetica", 10), 
                    background="#fcc077",
                    foreground="#0c484b",
                    borderwidth =0,
                    relief = "flat",
                    padding=(5,5))
    # Set font size and style for headings
    style.configure("Treeview.Heading",
                    font=("Helvetica", 12, "bold"),foreground="#0c484b",)
    # Hide the index column
    tree.column("#0", width=0, stretch=NO)

    # Define headings
    tree.heading("user_id", text="user_id")
    tree.heading("first_name", text="first_name")
    tree.heading("last_name", text="last_name")
    tree.heading("address1", text="address1")
    tree.heading("address2", text="address2")
    tree.heading("city", text="city")
    tree.heading("state", text="state")
    tree.heading("zipcode", text="zipcode")
    tree.heading("country", text="country")
    tree.heading("phone", text="phone")
    tree.heading("email", text="email")
    tree.heading("payment", text="payment")
    tree.heading("discount_code", text="discount_code")
    tree.heading("price_paid", text="price_paid")


    # Define columns properties
    tree.column("user_id", width=100, anchor=CENTER)
    tree.column("first_name", width=100,anchor=CENTER)
    tree.column("last_name", width=100,anchor=CENTER)
    tree.column("address1", width=100,anchor=CENTER)
    tree.column("address2", width=100,anchor=CENTER)
    tree.column("city", width=100,anchor=CENTER)
    tree.column("state", width=100,anchor=CENTER)
    tree.column("zipcode", width=100,anchor=CENTER)
    tree.column("country", width=100,anchor=CENTER)
    tree.column("phone", width=100,anchor=CENTER)
    tree.column("email", width=150,anchor=CENTER)
    tree.column("payment", width=100,anchor=CENTER)
    tree.column("discount_code", width=100,anchor=CENTER)
    tree.column("price_paid", width=100,anchor=CENTER)

    # Insert data into Treeview
    for idx, row in enumerate(result):
        tree.insert("", "end", text=idx + 1, values=row)

    # Pack Treeview
    tree.pack(side="top", fill="x")

    #treeview end
