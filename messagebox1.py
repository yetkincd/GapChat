#!/usr/bin/python3

#!/usr/bin/python3

#kaynak: https://www.geeksforgeeks.org/python-tkinter-scrolledtext-widget/
import sys
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
  
# Creating tkinter main window
win = tk.Tk()
win.title("GapChat 0.1 Cansu Yetkin & Baran Gunal")
  
# Title Label
ttk.Label(win, 
          text = "Gizli İçerik",
          font = ("Times New Roman", 15), 
          background = 'green', 
          foreground = "white").grid(column = 0,
                                     row = 0)
  
# Creating scrolled text 
# area widget
text_area = scrolledtext.ScrolledText(win, 
                                      wrap = tk.WORD, 
                                      width = 40, 
                                      height = 10, 
                                      font = ("Times New Roman",
                                              72))

mesaj=sys.argv[1]
mesaj.strip('\"')
text_area.insert(tk.INSERT,mesaj)
  
text_area.grid(column = 0, pady = 10, padx = 10)
text_area.configure(state ='disabled')
  
# Placing cursor in the text area
text_area.focus()
win.mainloop()
