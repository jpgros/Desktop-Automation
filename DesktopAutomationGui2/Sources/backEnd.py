import inspect
import time
import random

import pyautogui

import Sources.Gui as Gui
import os
#import main
from tkinter import filedialog as fd
from pynput import mouse
from pynput.mouse import Button, Listener
from pynput.mouse import Controller as mouseController
from pynput.keyboard import Controller as keyboardController

class backEnd:
	coords=[]

instBackEnd = backEnd()
mouseC = mouseController()
keyboardC = keyboardController()
strFile= "" #"C:/Users/jgr22027/OneDrive - OPEN/Documents/ScriptFiles/"

"""
Method to manage keyboard actions depending on macros
Existing macros 
";" for sequence of actions
"+" for a simultaneous key press
"§cmd§" for running a special command
For example §ctrl§ will press ctrl key
"""
def keyboardActions(keyboard):
	actions = keyboard.split(";")
	for elt in actions:
		print("try to write "+ str(elt))
		keysPressed = elt.split("+")
		for key in keysPressed:
			for char in key:
				print("try to type " + str(char))
				keyboardC.press(char)
				keyboardC.release(char)
"""
Returns int average between two parameters
@a any type accepted but need to be a number for cast to float 
@b any type accepted but need to be a number for cast to float
"""
def moy(a ,b):
	return int((float(a) + float(b))/2.0)

"""
Method to manage mouse actions depending on parameters
@line1 line containing first couple of coords
@line2 line containing second couple of coords
@timePressed containing time between click and release mouse bouton
@entryDelay containing the delay after the click
"""
def mouseActions(line1, line2, timePressed, entryDelay):
	coords1 = line1.split(";")
	coords2 = line2.split(";")

	print("clicking on " + str(moy(coords1[0],coords2[0])) + " " + str(moy(coords1[1],coords2[1])))
	mouseC.position =moy(coords1[0],coords2[0]), moy(coords1[1],coords2[1])
	mouseC.press(Button.left)
	time.sleep(timePressed)
	mouseC.release(Button.left)
	time.sleep(float(entryDelay))
	print("Current position: " + str(mouseC.position))

"""
Method retrieving the information for the script in the file
and calling the corresponding methods
@file input file containing the informations
"""
def clickProcess(file):
	#print(inspect.currentframe())
	try:
		f = open(file) #open(strFile+"clickingScript.txt","r")
		print("given file "+ file)
	except (FileNotFoundError) as e:
		file = fd.askopenfilename(initialdir=os.getcwd())
		f=open(file)
		print(f)
	while True:
		print("while loop")
		try:
			timeBetweenClick = float(f.readline())
			entryNB= int(f.readline())
			timePressed= float(f.readline())
			keyboard=f.readline()
			entryDelay= float(f.readline())
			coords1= f.readline()
			coords2= f.readline()
		except (AttributeError, ValueError) as e:
			print("catched err reading script files values" + str(e))
			break
			#if(line.__contains__(';')) : break
		try:
			if entryNB==-1 and timeBetweenClick==-1 and timePressed==-1: # clickmode = keyboard
				print("keyboard")
				keyboardActions(keyboard)

			elif entryNB!=-1 or timeBetweenClick!=-1 or timePressed!=-1: #clickmode = single or multiple
				print("mouse")
				mouseActions(coords1, coords2,timePressed,entryDelay)
			else:
				print("ERROR : clickMode in function " + inspect.currentframe() + " not taken into account")

		except (AttributeError, ValueError) as e:
			print("catched err using keyboard/mouse script actions" + str(e))
			break

def printSelectedCoord():
	for x in instBackEnd.coords:
		print(" coord loop "+ str(x))

"""
Retrieve an area with 2 clicks
The listener is called twice
"""
def retrievingMouseCoord(nb):
	# Collect events until released
	with Listener(
			on_click=on_click) as listener:
		listener.join()

	with Listener(
			on_click=on_click) as listener:
		listener.join()
"""
Bridge between gui interface and backend
Retrieve click and add it to the list
"""
def on_click(x, y, pressed):
	if pressed:
		print("coords clicked "  + str(x) + " " + str(y))
		for i in instBackEnd.coords:
			print (str(i) + " ")
		instBackEnd.coords.append(x)
		instBackEnd.coords.append(y)
		print('{0} at {1}'.format(
			'Pressed' if pressed else 'Released',
			(x, y)))
		print("len" + str(len(instBackEnd.coords)))
		if len(instBackEnd.coords)>=2:
			# Stop listener
			Gui.msgArea= "Selected (" + str(instBackEnd.coords.__getitem__(len(instBackEnd.coords) - 4)) + "," + str(instBackEnd.coords.__getitem__(len(instBackEnd.coords) - 3))
			Gui.msgArea = Gui.msgArea + ") (" + str(instBackEnd.coords.__getitem__(len(instBackEnd.coords) - 2)) + "," + str(instBackEnd.coords.__getitem__(len(instBackEnd.coords) - 1)) + ")"
			print("strarea should be " + Gui.msgArea)
			return False

# def verifPos(x,y):
# 	if(x > 500 or x <300):
# 		x= (random.random()*200)+300
# 	if(y > 800 or y <300):
# 		y= (random.random()*500)+300
# 	mouse.position= (x,y)

# def setCoords():
# 	f = open(strFile+"areas.txt", "a")
# 	f.write("wrting")
# 	f.write(str(instBackEnd.coords[0]) +";"+ str(instBackEnd.coords[1])+ "\n")
# 	instBackEnd.coords.clear()
# 	f.close()
def retrieveClickingScript():
	f = open(strFile+"clickingScript.txt", "a")

"""
Submit an action by writing it on a file
IF all parameters are well defined all the parameters are writen in the script file
"""
def submitClickingScript(parameters):
	f = open(strFile+"clickingScript.txt", "a")
	res=""
	res = parameters.timeBetweenClick.get() if parameters.timeBetweenClick.get() !=None and parameters.clickMode.get()=="Multiple" else "-1"
	f.write(res+"\n")
	if parameters.entryNB.get() != None and parameters.clickMode.get()=="Multiple":
		if parameters.durationMode.get()=="Clicks":
			res = "C:" + parameters.entryNB.get()
		elif parameters.durationMode.get()=="Seconds":
			res = "S:" + parameters.entryNB.get()
		else:
			print("Duration mode " + str(parameters.durationMode.get()) + "not taken into account")
			print("Please be sure you selected either a duration or a click number if you chose multiple clicks")
	else:
		res= "-1"
	f.write(res+"\n")
	res = parameters.timePressed.get() if parameters.timePressed.get() != None and parameters.clickMode.get()=="Single" else "-1"
	f.write(res + "\n")
	res = parameters.keyboardEntry.get() if parameters.clickMode.get() == "Keyboard" else ""
	f.write(res + "\n")
	res = parameters.entryDelay.get() if parameters.entryDelay.get() != None else "0"
	f.write(res + "\n")

	f.write(str(instBackEnd.coords[0]) +";"+ str(instBackEnd.coords[1])+ "\n")
	f.write(str(instBackEnd.coords[2]) +";"+ str(instBackEnd.coords[3])+ "\n")
	instBackEnd.coords.clear()
	f.close()
	Gui.infoMsg= "Writen done"

#mouse.position = (404, 879)#absolute

