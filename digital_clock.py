# Python program to make Digital Clock

import time
from tkinter import Label
from tkinter import *

def time_current():
    t = time.strftime("%I:%M:%S %p")    # 12-Hour clock
    # t = time.strftime("%H:%M:%S")     # 24-Hour clock
    time_display.config(text = t)
    time_display.after(200, time_current)

tk_window = Tk()
tk_window.title("My Digital Clock")

time_display = Label(tk_window, font = ("Consolas", 150, "bold"), bg = "black", fg = "red")
time_display.pack()

time_current()

tk_window.mainloop()
