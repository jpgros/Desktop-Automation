import time
import random
import Gui
#import main
from pynput import mouse
from pynput.mouse import Button, Controller, Listener
class backEnd:
	coords=[]

inst = backEnd()
mouse = Controller()
def clickProcess(file):
	f = open("C:/Users/jgr22027/PycharmProjects/DesktopAutomationGui/clickingScript.txt","r")
	print("C:/Users/jgr22027/PycharmProjects/DesktopAutomationGui/clickingScript.txt","r")
	for x in range(3):
		timeBetweenClick = int(f.readline())
		entryNB= int(f.readline())
		timePressed= int(f.readline())
		entryDelay= int(f.readline())
		line= f.readline()
		line= f.readline()
		#if(line.__contains__(';')) : break
		coords = line.split(";")
		print(coords[0] + " " + coords[1])
		mouse.move( int(coords[0]), int(coords[1]))
		mouse.press(Button.left)
		time.sleep(timePressed)
		mouse.release(Button.left)
		time.sleep(int(entryDelay))
		print("Current position: " + str(mouse.position))


def printSelectedCoord():
	for x in inst.coords:
		print(" coord loop "+ str(x))

def retrievingMouseCoord(nb):

	def on_click(x, y, button, pressed):
		if pressed:
			inst.coords.append(x)
			inst.coords.append(y)
			print('{0} at {1}'.format(
				'Pressed' if pressed else 'Released',
				(x, y)))
			print("len" + str(len(inst.coords)))
			if len(inst.coords)>=nb:
				# Stop listener
				print(" try ")
				Gui.msgArea="Selected (" + str(inst.coords.__getitem__(len(inst.coords)-4)) + "," + str(inst.coords.__getitem__(len(inst.coords)-3))
				Gui.msgArea = Gui.msgArea + ") (" + str(inst.coords.__getitem__(len(inst.coords)-2)) + "," + str(inst.coords.__getitem__(len(inst.coords)-1)) +")"
				print("strarea should be " + Gui.msgArea)
				return False

	# Collect events until released
	with Listener(
			on_click=on_click) as listener:
		listener.join()

def verifPos(x,y):
	if(x > 500 or x <300):
		x= (random.random()*200)+300
	if(y > 800 or y <300):
		y= (random.random()*500)+300
	mouse.position= (x,y)
def setCoords():
	f = open("areas.txt", "a")
	f.write("wrting")
	f.write(str(inst.coords[0]) +";"+ str(inst.coords[1])+ "\n")
	inst.coords.clear()
	f.close()
def retrieveClickingScript():
	f = open("clickingScript.txt", "a")

def submitClickingScript(timeBetweenClick, entryNB,entryDelay,timePressed, clickMode):
	f = open("clickingScript.txt", "a")
	res=""
	res = timeBetweenClick.get() if timeBetweenClick.get() !=None and clickMode.get()=="1" else "-1"
	f.write(res+"\n")
	res = entryNB.get() if entryNB.get() != None and clickMode.get()=="1" else "-1"
	f.write(res+"\n")
	res = timePressed.get() if timePressed.get() != None and clickMode.get()=="2" else "-1"
	f.write(res + "\n")
	res = entryDelay.get() if entryDelay.get() != None else "0"
	f.write(res + "\n")

	f.write(str(inst.coords[0]) +";"+ str(inst.coords[1])+ "\n")
	f.write(str(inst.coords[2]) +";"+ str(inst.coords[3])+ "\n")
	inst.coords.clear()
	f.close()
	Gui.infoMsg="Writen done"

print ("Current positions: " + str(mouse.position))
#mouse.position = (404, 879)#absolute

