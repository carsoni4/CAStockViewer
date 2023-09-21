import tkinter
import pandas as pd
import matplotlib.pyplot as plt
from alpha_vantage.timeseries import TimeSeries
from tkinter import *

# alpha vantage api
apikey = 'LETN3J076QRUX8EW'


# Method to search the api from string
def searchapi():
    ts = TimeSeries(key=apikey, output_format='pandas')
    data, meta = ts.get_intraday(symbol=entryString.get(), interval='1min', outputsize='full')
    data.head()
    print(entryString.get())
    plt.plot(data['4. close'])
    plt.show()
    # this will search the api


# Setting up main window in tkinter
home = Tk()
home.geometry("1000x800")
home.title("CA Stock Viewer")
tkinter.Label(master=home, text="CA STOCK VIEWER", font='Calibri 24').pack()

# stock symbol entry
input_frame = tkinter.Frame(master=home)
input_frame.pack()
entryString = tkinter.StringVar()
entry = tkinter.Entry(master=input_frame, textvariable=entryString)
entry.pack()
search_button = Button(master=input_frame, text="Search", command=lambda: searchapi())
search_button.pack()

home.mainloop()
