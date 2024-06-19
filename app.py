import tkinter as tk

root = tk.Tk()
root.title("Calculator")

def showClick():
    print(display.get())

display = tk.Entry(root)
display.grid(row=0, column=0, padx=20, pady=20)

btn = tk.Button(root, text="click me!", command=showClick)
btn1 = tk.Button(root, text="click me!", command=showClick)
btn2 = tk.Button(root, text="click me!", command=showClick)

btn.grid(row=1, column=0, padx=20, pady=20)
btn1.grid(row=1, column=1, padx=20, pady=20)
btn2.grid(row=1, column=2, padx=20, pady=20)

root.mainloop()