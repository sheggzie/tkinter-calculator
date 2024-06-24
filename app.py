import tkinter as tk

# Sets up the main tk window
root = tk.Tk()
root.title("Calculator")
root.geometry("310x160") # Specifies window's size: width by height

# Global variables
expression = ""
last_output = ""

# StringVar is often used in conjunction with Entry widgets to track 
# and update the text displayed in the widget.
equation = tk.StringVar() 

# Display value of buttons to the Entry widget
def showClick(input):
    global expression
    expression += str(input)
    equation.set(expression)

# Clear contents of the entry widget display, assigned to the "Clear" button.
def clear_display():
    global expression, last_output
    expression = ""
    equation.set(expression)
    last_output = ""

# Evaluate and calculate entry widget entries and inputs.
def calculate():
    global expression, last_output
    try:
        # The logic here means if the first item in the Entry widget display 
        # is a sign, the following expressions should be evaluated with the 
        # previous answer if theres one.
        signs = ["+", "-", "*", "/"]
        if expression[0] in signs:
            join = str(last_output) + str(expression)
            total = str(eval(join))
        else:
            total = str(eval(expression))
        
        equation.set(total)
        last_output = total
        expression = ""
    except:
        equation.set("error")
        expression = ""

# Create entry display widget.
display = tk.Entry(root, textvariable=equation)
display.grid(row=0, column=0, columnspan=4, ipadx=80)


# Create buttons and assign click event functions.
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
add = tk.Button(root, text="+", fg="black", bg="yellow", command=lambda: showClick('+'), width=8)
subtract = tk.Button(root, text="-", fg="black", bg="yellow", command=lambda: showClick('-'), width=8)
divide = tk.Button(root, text="/", fg="black", bg="yellow", command=lambda: showClick('/'), width=8)
multiply = tk.Button(root, text="x", fg="black", bg="yellow", command=lambda: showClick('*'), width=8)
decimal = tk.Button(root, text=".", command=lambda: showClick('.'), width=8)
equalsto = tk.Button(root, text="=", fg="black", bg="green", command=lambda: calculate(), width=28)
clear = tk.Button(root, text="Clear", fg="black", bg="red", command=lambda: clear_display(), width=8)

# Assign each button to a grid
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

# Run the tkinter mainloop event
root.mainloop()