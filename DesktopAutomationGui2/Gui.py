import tkinter

import backEnd
import os,sys, tempfile
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import filedialog as fd
from subprocess import call
from functools import partial

#import main


class Gui:
    infoMsg="tato"
    msgArea="Please select area before submitting"
    mainFile = None


    def launchWindow(self):
        m_w = tk.Tk()
        frm = ttk.Frame(m_w, padding=10)

        frm.grid()
        tk.Button(frm, text="Add area", command=self.addAreaWindows).grid(column=0, row=0)
        b1=tk.Button(frm, text="quit", command=m_w.destroy)
        b1.grid(column=1,row=0)

        tk.Button(frm, text="Clicking script", command=self.clickingWindows).grid(column=2, row=0)
        tk.Button(frm, text="Load CS", command=self.selectFile).grid(column=0, row=1)
        tk.Button(frm, text="Clear File", command=self.clearFile).grid(column=1, row=1)
        tk.Button(frm, text="Let's Go", command=lambda :backEnd.clickProcess(self.mainFile)).grid(column=2, row=1)

        #msgGUI.trace('w',my_r)
        tk.mainloop()

    def addAreaWindows(self):
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

    def clearFile(self):
        filename = fd.askopenfilename(initialdir=os.getcwd())
        f = open(filename, "w")  # Create a blank file
        f.truncate()  # Clear previous content
        f.close()  # Close file
        print("suppressed successfully")

    def clickingWindows(self):
        def updateAreaInfo(*args):
            print("called method" + self.msgArea)
            selectedArea.set(self.msgArea)
            print(selectedArea.get())
        def my_r(*args): #args avoid error of passing arguments
            print("got it")
            msgGUI.set("Submited " + str(timeBetweenClick.get()) + " " + str(entryNB) + " " + str(entryDelay) + " " + str(timePressed))
            print(msgGUI.get())  # Print when variable changes.
        def selection(*args):
            print("You selected the option " + str(clickMode.get()))
            if(str(clickMode.get())=="1"):
                timeBetweenClick.config(state="enabled")
                entryNB.config(state="enabled")
                timePressed.config(state="disabled")
            if (str(clickMode.get()) == "2"):
                timeBetweenClick.config(state="disabled")
                entryNB.config(state="disabled")
                timePressed.config(state="enabled")

        clickingWindow= Tk()
        msgGUI = tk.StringVar(clickingWindow)
        msgGUI.set("")
        clickMode = tk.StringVar(clickingWindow)
        selectedArea = tk.StringVar(clickingWindow)

        selectedArea.set(self.msgArea)

        clickMode.set("Multiple Clicks")

        #adding trace to bind stringvar to actions trigger by GUI
        clickMode.trace('w', selection)
        msgGUI.trace('w', my_r)
        selectedArea.trace('w', updateAreaInfo)
        frm2 = ttk.Frame(clickingWindow, padding=10)
        frm2.grid()

        ttk.Button(frm2, text="select area", command=lambda:[backEnd.retrievingMouseCoord(4), selectedArea.set(self.msgArea)]).grid(column=1, row=1)
        ttk.Label(frm2, textvariable=selectedArea).grid(row=1, column=2)

        r1 = ttk.Radiobutton(frm2, text='Multiple Clicks', variable=clickMode, value=1, command=lambda: clickMode.set("Multiple Clicks"))
        r1.grid(column=1, row=2)
        r1['command'] = partial(selection)
        r2 = ttk.Radiobutton(frm2, text='Single Click' , variable=clickMode, value=2, command=lambda: clickMode.set("Single Click"))
        r2.grid(column=2, row=2)
        r2['command'] = partial(selection)

        ttk.Label(frm2, text="Time between click (s)").grid(row=3, column=0)
        timeBetweenClick = ttk.Entry(frm2)
        timeBetweenClick.grid(row=3, column=1)
        timeBetweenClick.config(state="disabled")

        ttk.Label(frm2, text="Delay after click(s)").grid(row=3, column=2)
        entryDelay = ttk.Entry(frm2)
        entryDelay.grid(row=3, column=3)
        ttk.Label(frm2, text="Number of click (s)").grid(row=4, column=0)
        entryNB = ttk.Entry(frm2)
        entryNB.grid(row=4, column=1)
        entryNB.config(state="disabled")

        ttk.Label(frm2, text="Time maintaining click").grid(row=4, column=2)
        timePressed = ttk.Entry(frm2)
        timePressed.grid(row=4, column=3)
        timePressed.config(state="disabled")

        b1=ttk.Button(frm2, text="submit", command=lambda
        :[backEnd.submitClickingScript(timeBetweenClick, entryNB,entryDelay,timePressed,clickMode), msgGUI.set("Submited ")])
        b1.grid(column=1, row=5)
        ttk.Button(frm2, text="done", command=clickingWindow.destroy).grid(column=2, row=5)
        l1=tk.Label(clickingWindow, textvariable=msgGUI)
        l1.grid(row=6, column=0)

        tk.mainloop()

    def onButton(self,msg):
        msg.set("yep")
        print("info msg " +self.infoMsg)
        self.output_label.config(text="yep")

    def selectFile(self):
        #dirname = ttk.askdirectory()
        self.mainFile = fd.askopenfilename(initialdir = os.getcwd())
        if os.name == "nt":
            EDITOR = os.environ.get('EDITOR', 'notepad')
        else:
            EDITOR = os.environ.get('EDITOR', 'nano')
        call([EDITOR, self.mainFile])