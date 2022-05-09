from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
import backEnd
import os



def launchWindow():
    root = Tk()
    frm = ttk.Frame(root, padding=10)
    frm.grid()
    ttk.Button(frm, text="Add area", command=addAreaWindows).grid(column=0, row=0)
    ttk.Button(frm, text="quit", command=root.destroy).grid(column=1, row=0)
    ttk.Button(frm, text="Clicking script", command=clickingWindows).grid(column=2, row=0)
    ttk.Button(frm, text="Load CS", command= selectFile).grid(column=0, row=1)
    root.mainloop()

def addAreaWindows():
    area = Tk()
    frm2= ttk.Frame(area, padding=10)
    frm2.grid()
    ttk.Button(frm2, text="select area", command=lambda : backEnd.retrievingMouseCoord(4)).grid(column=0, row=1)
    ttk.Label(frm2, text="enter coords").grid(row=2, column=0)
    e = ttk.Entry(frm2)
    en = ttk.Entry(frm2)
    e.grid(row=2, column=1)
    en.grid(row=2, column=2)
    ttk.Button(frm2, text="submitcoords", command=backEnd.setCoords).grid(column=0, row=3)
    ttk.Button(frm2, text="done", command=area.destroy).grid(column=1, row=3)

def clickingWindows():
    area = Tk()
    frm2 = ttk.Frame(area, padding=10)
    frm2.grid()
    ttk.Button(frm2, text="select area", command=lambda:backEnd.retrievingMouseCoord(8)).grid(column=0, row=1)
    ttk.Label(frm2, text="time between click (s)").grid(row=2, column=0)
    entry = ttk.Entry(frm2)
    entry.grid(row=2, column=1)
    ttk.Button(frm2, text="submit", command=lambda :backEnd.submitClickingScript(entry)).grid(column=0, row=3)
    ttk.Button(frm2, text="done", command=area.destroy).grid(column=1, row=3)

def selectFile():
    #dirname = ttk.askdirectory()
    filename = fd.askopenfilename(initialdir = os.getcwd())
