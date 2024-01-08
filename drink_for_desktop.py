# Author: Neywa
# This is a short program to count the amount of liquids you drink during a day.
# The db file (drank.txt) needs to be cleared every day before new use.

import os
from tkinter import *
from tkinter import ttk

# Check if the drank.txt file (the db) exists.
PATH = './drank.txt'
def checkfile():
    if os.path.isfile(PATH):
        pass
    else:
        file=open("drank.txt", "w")
        file.write("0")
        file.close()

checkfile()

goal = 2500

# Function to calculate the daily water consumption. It's called by the 'Add to pool' button.
# - Reads the data from drank file
# - Checks the value inserted in the enter field
# - Adds the inserted value to already consumed water and adds the sum to the file
def calculate(*args):
    try:
        pool = int(open("drank.txt", "r").read())
        value = int(drank.get())
        poolupdate.set(pool+value)
        file = open("drank.txt", "w")
        file.write(poolupdate.get())
        file.close()
        drank.set('')
    except ValueError:
        pass

# Function to reset the daily pool. It's called by the 'Reset pool' button.
def resetpool(*args):
    file = open("drank.txt", "w")
    file.write("0")
    file.close()
    poolupdate.set("0")

# Creating the graphical interface
root = Tk()
root.title("Drink your water")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

drank = StringVar()
drank_entry = ttk.Entry(mainframe, width=7, textvariable=drank)
drank_entry.grid(column=2, row=1, sticky=(W, E))

# Check if the db file already exists and contains some data.
# If yes, the data are displayed as the amount af water already drinked today.
with open("drank.txt", "r") as file:
    poolcheck=file.read().rstrip()

poolupdate = StringVar(root, poolcheck)
ttk.Label(mainframe,textvariable=poolupdate).grid(column=2, row=2, sticky=(W, E))

ttk.Button(mainframe, text="Add to pool", command=calculate).grid(column=4, row=1, sticky=W)
ttk.Button(mainframe, text="Reset pool", command=resetpool).grid(column=4, row=2, sticky=W)

ttk.Label(mainframe, text="ml").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="Today you drank").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="ml").grid(column=3, row=2, sticky=W)

# Prep work for 'remains from goal' feature.
#remains = StringVar()
#ttk.Label(mainframe, textvariable=remains).grid(column=1, row=3, sticky=W)
#ttk.Label(mainframe, text="Remains from goal").grid(column=1, row=3, sticky=W)

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)
drank_entry.focus()
root.bind('<Return>', calculate)
root.bind('<KP_Enter>', calculate)

root.mainloop()
