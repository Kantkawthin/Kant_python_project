'''
eval()
eval() is a function to calculate math
it can automatically calculate any math operation (+,-,*,/)
it can only work on string
'''



from tkinter import *

window = Tk()
window.title("Sample calculator")
window.configure(bg="#455054")

# Initialize expression
expression = ""

# Button click
def button_click(number):
    global expression
    expression += str(number)  # Append number to the expression
    input_box.delete(0, END)   # Clear input box
    input_box.insert(0, expression)  # Show updated expression

# Button clear
def button_clear():
    global expression
    expression = ""  # Reset expression
    input_box.delete(0, END)

#button backspace
def button_backspace():
    global expression
    expression =expression[:-1]
    input_box.delete(0, END)
    input_box.insert(0, expression)

# Button add
def button_add():
    global expression
    expression += "+"  # Append '+' to the expression
    input_box.delete(0, END)
    input_box.insert(0, expression)

# Button subtract
def button_subtract():
    global expression
    expression += "-"  # Append '-' to the expression
    input_box.delete(0, END)
    input_box.insert(0, expression)

# Button multiply
def button_multiply():
    global expression
    expression += "*"  # Append '*' to the expression
    input_box.delete(0, END)
    input_box.insert(0, expression)

# Button divide
def button_divide():
    global expression
    expression += "/"  # Append '/' to the expression
    input_box.delete(0, END)
    input_box.insert(0, expression)

# Button equal
def button_equal():
    global expression
    try:
        result = eval(expression)  # Evaluate the expression
        input_box.delete(0, END)
        input_box.insert(0, result)  # Show result
        expression = str(result)  # Update expression to result
    except Exception as e:
        input_box.delete(0, END)
        input_box.insert(0, "Error")  # Handle any evaluation errors
        expression = ""

# Input box
input_box = Entry(window,bg="#455054",fg="white", width=35, borderwidth=3)
input_box.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Buttons
button_1 = Button(window, text="1",bg="#455054",fg="white", padx=20, pady=10, command=lambda: button_click(1))
button_2 = Button(window, text="2",bg="#455054",fg="white", padx=20, pady=10, command=lambda: button_click(2))
button_3 = Button(window, text="3",bg="#455054",fg="white", padx=21, pady=10, command=lambda: button_click(3))
button_4 = Button(window, text="4",bg="#455054",fg="white", padx=20, pady=10, command=lambda: button_click(4))
button_5 = Button(window, text="5",bg="#455054",fg="white", padx=20, pady=10, command=lambda: button_click(5))
button_6 = Button(window, text="6",bg="#455054",fg="white", padx=21, pady=10, command=lambda: button_click(6))
button_7 = Button(window, text="7",bg="#455054",fg="white", padx=20, pady=10, command=lambda: button_click(7))
button_8 = Button(window, text="8",bg="#455054",fg="white", padx=20, pady=10, command=lambda: button_click(8))
button_9 = Button(window, text="9",bg="#455054",fg="white", padx=21, pady=10, command=lambda: button_click(9))
button_0 = Button(window, text="0",bg="#455054",fg="white", padx=20, pady=10, command=lambda: button_click(0))
button_dot = Button(window, text=".",bg="#455054",fg="white", padx=21, pady=10, command=lambda: button_click("."))
button_add = Button(window, text="+",bg="#455054",fg="white", padx=19, pady=10, command=button_add)
button_subtract = Button(window, text="-",bg="#455054",fg="white", padx=21, pady=10, command=button_subtract)
button_multiply = Button(window, text="x",bg="#455054",fg="white", padx=20, pady=10, command=button_multiply)
button_divide = Button(window, text="/",bg="#455054",fg="white", padx=22, pady=10, command=button_divide)
button_equal = Button(window, text="=", padx=19, pady=35, command=button_equal)
button_clear = Button(window, text="Clear",bg="#455054",fg="white", padx=41, pady=10, command=button_clear)
button_backspace = Button(window, text="<",bg="#455054",fg="white", padx=19, pady=10, command=button_backspace)

# Button grid layout
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_multiply.grid(row=3, column=3)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_subtract.grid(row=2, column=3)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_add.grid(row=1, column=3)

button_0.grid(row=4, column=0)
button_dot.grid(row=4, column=1)
button_divide.grid(row=4, column=2)
button_equal.grid(row=4, rowspan=2, column=3)

button_clear.grid(row=5, columnspan=2, column=1)
button_backspace.grid(row=5, column=0)

window.mainloop()
