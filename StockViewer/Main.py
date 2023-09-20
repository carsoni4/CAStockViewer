import tkinter
from tkinter import *

def searchapi():
    print("Hello")

    #this will search the api

#Setting up main window in tkinter
home = Tk()
home.geometry("1000x800")
home.title("CA Stock Viewer")
title_label = tkinter.Label(master = home, text = "CA STOCK VIEWER", font='Calibri 24').pack()
#stock symbol entry
input_frame = tkinter.Frame(master=home).pack()
sse = tkinter.Entry(master=input_frame).pack()
search_button = Button(master=input_frame, text="Search", command=lambda:searchapi()).pack()



home.mainloop()