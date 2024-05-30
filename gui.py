import tkinter as tk
import tkinter.ttk as ttk


window = tk.Tk() #initializes an instance of tkinter window

greeting = tk.Label(text="Name:",  #the actual text
                     foreground= "white", #text color
                     background= "blue",   #text background
                     width=10,
                     height=10
                     )

greeting.pack()


button = tk.Button(
    text="Click me!",
    width=25,
    height=5,
    bg="red",
    fg="white",
)

'''button machanics'''
button.pack()

entry = tk.Entry()

entry.pack()
name = entry.get()
name
window.mainloop()

