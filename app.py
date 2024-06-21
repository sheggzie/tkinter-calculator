import tkinter as tk

root = tk.Tk()
root.title("Calculator")
root.geometry("310x160")

equation = tk.StringVar()

expression = ""

def showClick(input):
    global expression
    expression += str(input)
    equation.set(expression)

display = tk.Entry(root, textvariable=equation)
display.grid(row=0, column=0, columnspan=4, ipadx=80)

one = tk.Button(root, text="1", command=lambda: showClick(1), width=8)
two = tk.Button(root, text="2", command=lambda: showClick(2), width=8)
three = tk.Button(root, text="3", command=lambda: showClick(3), width=8)
four = tk.Button(root, text="4", command=lambda: showClick(4), width=8)
five = tk.Button(root, text="5", command=lambda: showClick(5), width=8)
six = tk.Button(root, text="6", command=lambda: showClick(6), width=8)
seven = tk.Button(root, text="7", command=lambda: showClick(7), width=8)
eight = tk.Button(root, text="8", command=lambda: showClick(8), width=8)
nine = tk.Button(root, text="9", command=lambda: showClick(9), width=8)
zero = tk.Button(root, text="0", command=lambda: showClick(0), width=18)
add = tk.Button(root, text="+", command=lambda: showClick('+'), width=8)
subtract = tk.Button(root, text="-", command=lambda: showClick('-'), width=8)
divide = tk.Button(root, text="/", command=lambda: showClick('/'), width=8)
multiply = tk.Button(root, text="x", command=lambda: showClick('x'), width=8)
decimal = tk.Button(root, text=".", command=lambda: showClick('.'), width=8)
equalsto = tk.Button(root, text="=", command=lambda: showClick('='), width=28)
clear = tk.Button(root, text="Clear", command="", width=8)

seven.grid(row=1, column=0)
eight.grid(row=1, column=1)
nine.grid(row=1, column=2)
multiply.grid(row=1, column=3)
four.grid(row=2, column=0)
five.grid(row=2, column=1)
six.grid(row=2, column=2)
subtract.grid(row=2, column=3)
one.grid(row=3, column=0)
two.grid(row=3, column=1)
three.grid(row=3, column=2)
add.grid(row=3, column=3)
zero.grid(row=4, column=0, columnspan=2)
decimal.grid(row=4, column=2)
divide.grid(row=4, column=3)
equalsto.grid(row=5, column=0, columnspan=3)
clear.grid(row=5, column=3)











root.mainloop()