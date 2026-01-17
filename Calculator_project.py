from tkinter import *

Window = Tk()
Window.title("Calculator")
Window.geometry("490x500")

# Entry Box
user_input = Entry(Window, 
                   borderwidth=10,
                   width=21, 
                   font=("Arial", 30, "bold"),
                   justify=RIGHT)
user_input.place(x=0, y=0, height=100)

# Functions 
def button(num):
    user_input.insert(END, str(num))

def equal():
    try:
        expression = user_input.get()
        result = eval(expression)
        user_input.delete(0, END)
        user_input.insert(END, str(result))
    except Exception:
        user_input.delete(0, END)
        user_input.insert(END, "Error")

def clear():
    user_input.delete(0, END)

def backspace():
    user_input.delete(len(user_input.get())-1, END)

# Font 
btn_font = ("Arial", 22, "bold")

# Buttons 

# Row 1 (y=100): 7, 8, 9, +, %
Button(Window, text="7", bg="black", fg="white", font=btn_font, command=lambda:button(7)).place(x=10, y=100, height=90, width=80)
Button(Window, text="8", bg="black", fg="white", font=btn_font, command=lambda:button(8)).place(x=100, y=100, height=90, width=80)
Button(Window, text="9", bg="black", fg="white", font=btn_font, command=lambda:button(9)).place(x=200, y=100, height=90, width=80)
Button(Window, text="+", bg="black", fg="white", font=btn_font, command=lambda:button("+")).place(x=300, y=100, height=90, width=80)
Button(Window, text="%", bg="black", fg="white", font=btn_font, command=lambda:button("/100")).place(x=400, y=100, height=90, width=80)

# Row 2 (y=200): 4, 5, 6, -, Backspace
Button(Window, text="4", bg="black", fg="white", font=btn_font, command=lambda:button(4)).place(x=10, y=200, height=90, width=80)
Button(Window, text="5", bg="black", fg="white", font=btn_font, command=lambda:button(5)).place(x=100, y=200, height=90, width=80)
Button(Window, text="6", bg="black", fg="white", font=btn_font, command=lambda:button(6)).place(x=200, y=200, height=90, width=80)
Button(Window, text="-", bg="black", fg="white", font=btn_font, command=lambda:button("-")).place(x=300, y=200, height=90, width=80)
Button(Window, text="⌫", bg="black", fg="white", font=btn_font, command=backspace).place(x=400, y=200, height=90, width=80)

# Row 3 (y=300): 1, 2, 3, *, . (Decimal)
Button(Window, text="1", bg="black", fg="white", font=btn_font, command=lambda:button(1)).place(x=10, y=300, height=90, width=80)
Button(Window, text="2", bg="black", fg="white", font=btn_font, command=lambda:button(2)).place(x=100, y=300, height=90, width=80)
Button(Window, text="3", bg="black", fg="white", font=btn_font, command=lambda:button(3)).place(x=200, y=300, height=90, width=80)
Button(Window, text="*", bg="black", fg="white", font=btn_font, command=lambda:button("*")).place(x=300, y=300, height=90, width=80)
# Added Decimal (.) to fill the gap above Equal
Button(Window, text=".", bg="black", fg="white", font=btn_font, command=lambda:button(".")).place(x=400, y=300, height=90, width=80)

# Row 4 (y=400): 0 (Wide), C, /, = (Below Backspace)
# Zero button is now Wide (width=170)
Button(Window, text="0", bg="black", fg="white", font=btn_font, command=lambda:button(0)).place(x=10, y=400, height=90, width=170)
Button(Window, text="C", bg="black", fg="white", font=btn_font, command=clear).place(x=200, y=400, height=90, width=80)
Button(Window, text="/", bg="black", fg="white", font=btn_font, command=lambda:button("/")).place(x=300, y=400, height=90, width=80)
# Equal button moved to column 5 (x=400)
Button(Window, text="=", bg="gray", fg="white", font=btn_font, command=equal).place(x=400, y=400, height=90, width=80)

mainloop()