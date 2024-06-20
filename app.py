import tkinter as tk

root = tk.Tk()
root.title("Calculator")

def showClick():
    print(display.get())

display = tk.Entry(root)
display.grid(row=0, padx=20, pady=20)

one = tk.Button(root, text="1", command=showClick)
two = tk.Button(root, text="2", command=showClick)
three = tk.Button(root, text="3", command=showClick)
four = tk.Button(root, text="4", command=showClick)
five = tk.Button(root, text="5", command=showClick)
six = tk.Button(root, text="6", command=showClick)
seven = tk.Button(root, text="7", command=showClick)
eight = tk.Button(root, text="8", command=showClick)
nine = tk.Button(root, text="9", command=showClick)
zero = tk.Button(root, text="0", command=showClick)

one.grid(row=1, column=0, pady=20)
two.grid(row=1, column=1, pady=20)
three.grid(row=1, column=2, pady=20)
four.grid(row=2, column=0, pady=20)
five.grid(row=2, column=1, pady=20)
six.grid(row=2, column=2, pady=20)
seven.grid(row=3, column=0, pady=20)
eight.grid(row=3, column=1, pady=20)
nine.grid(row=3, column=2, pady=20)
zero.grid(row=4, column=0, pady=20)

root.mainloop()