import pyautogui as pyautogui

import Sources.backEnd as backEnd
import os
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import filedialog as fd
from subprocess import call
from functools import partial

#import main

import pyautogui
import time
class Gui:
    infoMsg="tato"
    msgArea="Please select area before submitting"
    mainFile = None

    class Parameters:
        timeBetweenClick=-1
        entryNB=-1
        entryDelay=-1
        timePressed=-1
        clickMode=None
        durationMode=None
        keyboardEntry=""
    """
    First window to appear only basic operation can be done here
    Add area : not used anymore
    Quit : close the window
    Adding command let usef add clicks/keyboard script parametrizing with a new window
    Load CS : let user load a script already created and open it on a text editor automaticaly.
    Clear file : let user remove the content of a created file
    Let's Go : launch a selected script, if no script selected the app ask for a file.
    """
    def launchWindow(self):
        i=0
        while(i<1):
            print(pyautogui.position())
            time.sleep(1)
            i+=1

        m_w = tk.Tk()
        frm = ttk.Frame(m_w, padding=10)

        frm.grid()
        tk.Button(frm, text="Add area", command=self.addAreaWindows).grid(column=0, row=0)
        b1=tk.Button(frm, text="quit", command=m_w.destroy)
        b1.grid(column=1,row=0)

        tk.Button(frm, text="Adding commands", command=self.clickingWindows).grid(column=2, row=0)
        tk.Button(frm, text="Load CS", command= lambda : self.selectFile(True)).grid(column=0, row=1)
        tk.Button(frm, text="Clear File", command=self.clearFile).grid(column=1, row=1)
        tk.Button(frm, text="Let's Go", command=lambda : backEnd.clickProcess(self.mainFile,self.Parameters)).grid(column=2, row=1)

        #msgGUI.trace('w',my_r)
        tk.mainloop()
    """
    Remove soon
    """
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
    """
    Clear the content of the file
    Opens a file explorer and the selected file will be erased
    """
    def clearFile(self):
        filename = fd.askopenfilename(initialdir=os.getcwd())
        f = open(filename, "w")  # Create a blank file
        f.truncate()  # Clear previous content
        f.close()  # Close file
        print("suppressed successfully")


    """
    Disable the possibility to enter and clear the content writen
    """
    def disableEntry(self, entry):
        entry.delete(0, 'end')
        entry.config(state="disabled")
    """
    Window containing a lots of items for the script parametrizing
    3 modes ares possibles choosen with radio buttons
    Multiple clicks wich leads to another choice between 
    a number of clicks or a duration of clicks
    Single clicks will proceed to only one click
    Keyboard touch let user enter keyboard commands,
    For keyboard input:    
        the ";" character cut two sequences
        the "+" character ask to press simultaneously the keyboard keys
    For every possibilities it is possible to add a delay after click or a keyboard pressed
    The button Choose file allows to choose a file where the script will be written
    The button Submit let the user submit each action
    The button Done closes the window
    """
    def clickingWindows(self):
        params = self.Parameters()
        def updateAreaInfo(*args):
            print("called method" + self.msgArea)
            selectedArea.set(self.msgArea)
            print(selectedArea.get())
        def my_r(*args): #args avoid error of passing arguments
            msgGUI.set("Submited " + str(self.Parameters.timeBetweenClick.get()) + " " + str(self.Parameters.entryNB.get())
                       + " " + str(self.Parameters.entryDelay.get()) + " " + str(self.Parameters.timePressed.get()))
            print(msgGUI.get())  # Print when variable changes.
        """
        This method manages the element of the window.
        It update the state of the elements, which guides the user 
        how to fill the parameters
        """
        def selection(*args):
            print("You selected the option " + str(self.Parameters.clickMode.get()))
            if(str(self.Parameters.clickMode.get())=="Multiple"):
                self.disableEntry(self.Parameters.timePressed)
                self.disableEntry(self.Parameters.keyboardEntry)
                self.Parameters.timeBetweenClick.config(state="enabled")
                self.Parameters.entryNB.config(state="enabled")
                radioClick.config(state="enabled")
                radioClick2.config(state="enabled")
            if (str(self.Parameters.clickMode.get()) == "Single"):
                self.disableEntry(self.Parameters.timeBetweenClick)
                self.disableEntry(self.Parameters.entryNB)
                self.disableEntry(self.Parameters.keyboardEntry)
                self.Parameters.timePressed.config(state="enabled")
                radioClick.config(state="disabled")
                radioClick2.config(state="disabled")
            if(str(self.Parameters.clickMode.get()) == "Keyboard"):
                self.disableEntry(self.Parameters.timeBetweenClick)
                self.disableEntry(self.Parameters.entryNB)
                self.disableEntry(self.Parameters.timePressed)
                self.Parameters.keyboardEntry.config(state="enabled")
                radioClick.config(state="disabled")
                radioClick2.config(state="disabled")

        def fakeCallback(*args):
            print("callback called")
            print("duration mode " + str(self.Parameters.durationMode.get()))
        clickingWindow= Tk()
        msgGUI = tk.StringVar(clickingWindow)
        msgGUI.set("")
        self.Parameters.clickMode = tk.StringVar(clickingWindow)
        selectedArea = tk.StringVar(clickingWindow)
        self.Parameters.durationMode = tk.StringVar(clickingWindow)

        selectedArea.set(self.msgArea)
        self.Parameters.clickMode.set("Multiple Clicks")
        #durationMode.set("Clicks")
        #adding trace to bind stringvar to actions trigger by GUI
        self.Parameters.clickMode.trace('w', selection)
        self.Parameters.durationMode.trace('w', fakeCallback)
        msgGUI.trace('w', my_r)
        selectedArea.trace('w', updateAreaInfo)
        frm2 = ttk.Frame(clickingWindow, padding=10)
        frm2.grid()

        ttk.Button(frm2, text="select area", command=lambda:[backEnd.retrievingMouseCoord(4), selectedArea.set(self.msgArea)]).grid(column=1, row=1)
        ttk.Label(frm2, textvariable=selectedArea).grid(row=1, column=2)

        r1 = ttk.Radiobutton(frm2, text='Multiple Clicks', variable=self.Parameters.clickMode, value='Multiple', command=lambda: self.Parameters.clickMode.set("Multiple Clicks"))
        r1.grid(row=2,column=1)
        r1['command'] = partial(selection)
        r2 = ttk.Radiobutton(frm2, text='Single Click' , variable=self.Parameters.clickMode, value='Single', command=lambda: self.Parameters.clickMode.set("Single Click"))
        r2.grid(row=2, column=2)
        r2['command'] = partial(selection)

        r3 = ttk.Radiobutton(frm2, text='Keyboard Touch', variable=self.Parameters.clickMode, value='Keyboard',
                             command=lambda: self.Parameters.clickMode.set("Keyboard Touch"))
        r3.grid(row=2, column=3)
        r3['command'] = partial(selection)

        ttk.Label(frm2, text="Time between click (s)").grid(row=3, column=0)
        self.Parameters.timeBetweenClick = ttk.Entry(frm2)
        self.Parameters.timeBetweenClick.grid(row=3, column=1)
        self.Parameters.timeBetweenClick.config(state="disabled")

        ttk.Label(frm2, text="Delay after click(s)").grid(row=3, column=2)
        self.Parameters.entryDelay = ttk.Entry(frm2)
        self.Parameters.entryDelay.grid(row=3, column=3)
        ttk.Label(frm2, text="Number of ").grid(row=4, column=0)

        radioClick = ttk.Radiobutton(frm2, text='click (s)', variable=self.Parameters.durationMode, value='Clicks',
                             command=lambda: self.Parameters.durationMode.set("Clicks"))
        radioClick.grid(row=4, column=1)
        radioClick['command'] = partial(fakeCallback)

        radioClick2 = ttk.Radiobutton(frm2, text='second(s) clicking', variable=self.Parameters.durationMode, value="Seconds",
                             command=lambda: self.Parameters.durationMode.set("Seconds"))
        radioClick2.grid(row=4, column=2)
        radioClick2['command'] = partial(fakeCallback)

        self.Parameters.entryNB = ttk.Entry(frm2)
        self.Parameters.entryNB.grid(row=4, column=3)
        self.Parameters.entryNB.config(state="disabled")

        ttk.Label(frm2, text="Time maintaining click").grid(row=5, column=0)
        self.Parameters.timePressed = ttk.Entry(frm2)
        self.Parameters.timePressed.grid(row=5, column=1)
        self.Parameters.timePressed.config(state="disabled")

        ttk.Label(frm2, text="Keyboard Input").grid(row=5, column=2)
        self.Parameters.keyboardEntry = ttk.Entry(frm2)
        self.Parameters.keyboardEntry.grid(row=5, column=3)
        self.Parameters.keyboardEntry.config(state="disabled")

        newFileB= ttk.Button(frm2, text="Choose File",command =lambda : self.selectFile(False))
        newFileB.grid(row=6,column=0)
        b1=ttk.Button(frm2, text="Submit", command=lambda
        :[backEnd.submitClickingScript(self.Parameters), msgGUI.set("Submited ")])
        b1.grid(row=6,column=1)
        ttk.Button(frm2, text="Done", command=clickingWindow.destroy).grid(row=6,column=2)

        l1=tk.Label(clickingWindow, textvariable=msgGUI)
        l1.grid(row=7, column=0)

        tk.mainloop()
    """
    Open an explorer window to select a file
    If bool is true a text editor is opened
    
    @bool boolean for opening the text editor
    """
    def selectFile(self, bool):
        #dirname = ttk.askdirectory()
        self.mainFile = fd.askopenfilename(initialdir = os.getcwd())
        if bool:
            if os.name == "nt":
                EDITOR = os.environ.get('EDITOR', 'notepad')
            else:
                EDITOR = os.environ.get('EDITOR', 'nano')
            call([EDITOR, self.mainFile])