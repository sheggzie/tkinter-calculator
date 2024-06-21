import tkinter as tk

root = tk.Tk()
root.title("Calculator")
root.geometry("280x160")

equation = tk.StringVar()

expression = ""

def showClick(input):
    global expression
    expression += str(input)
    equation.set(expression)

display = tk.Entry(root, textvariable=equation)
display.grid(row=0, column=0, columnspan=3, ipadx=60)

one = tk.Button(root, text="1", command=lambda: showClick(1), width=8)
two = tk.Button(root, text="2", command=lambda: showClick(2), width=8)
three = tk.Button(root, text="3", command=lambda: showClick(3), width=8)
four = tk.Button(root, text="4", command=lambda: showClick(4), width=8)
five = tk.Button(root, text="5", command=lambda: showClick(5), width=8)
six = tk.Button(root, text="6", command=lambda: showClick(6), width=8)
seven = tk.Button(root, text="7", command=lambda: showClick(7), width=8)
eight = tk.Button(root, text="8", command=lambda: showClick(8), width=8)
nine = tk.Button(root, text="9", command=lambda: showClick(9), width=8)
zero = tk.Button(root, text="0", command=lambda: showClick(0), width=8)

one.grid(row=1, column=0)
two.grid(row=1, column=1)
three.grid(row=1, column=2)
four.grid(row=2, column=0)
five.grid(row=2, column=1)
six.grid(row=2, column=2)
seven.grid(row=3, column=0)
eight.grid(row=3, column=1)
nine.grid(row=3, column=2)
zero.grid(row=4, column=0)

root.mainloop()