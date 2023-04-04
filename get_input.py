#!/usr/bin/python

#kaynak: https://stackoverflow.com/questions/38725442/how-to-use-tkinter-entry-like-raw-input
import tkinter as tk
w = 800 # width for the Tk root
h = 650 # height for the Tk root

#https://stackoverflow.com/questions/35817/how-to-escape-os-system-calls
def sh_escape(s):
   return s.replace("(","\\(").replace(")","\\)").replace(" ","\\ ")

def gui_input(prompt):

    root = tk.Tk()
    w = 600 # width for the Tk root
    h = 100 # height for the Tk root

    # get screen width and height
    ws = root.winfo_screenwidth() # width of the screen
    hs = root.winfo_screenheight() # height of the screen
    x=20
    y=20

# set the dimensions of the screen 
# and where it is placed
    #print('%dx%d+%d+%d' % (w, h, x,y))
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    # this will contain the entered string, and will
    # still exist after the window is destroyed
    var = tk.StringVar()

    # create the GUI
    label = tk.Label(root, text=prompt)
    entry = tk.Entry(root, textvariable=var)
    label.pack(side="left", padx=(20, 0), pady=20)
    entry.pack(side="right", fill="x", padx=(0, 20), pady=20, expand=True)

    # Let the user press the return key to destroy the gui 
    entry.bind("<Return>", lambda event: root.destroy())

    # this will block until the window is destroyed
    root.mainloop()

    # after the window has been destroyed, we can't access
    # the entry widget, but we _can_ access the associated
    # variable
    value = var.get()
    return value

mesaj = gui_input("Sifrelenecek Mesaj").encode('utf-8')

print(mesaj)
