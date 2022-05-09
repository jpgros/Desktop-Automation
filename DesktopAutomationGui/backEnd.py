import time
import random
import Gui
from pynput import mouse
from pynput.mouse import Button, Controller, Listener
class backEnd:
	coords=[]

inst = backEnd()
mouse = Controller()
def repeatclick(i):
	for x in range(i):
		time.sleep(0.3)
		print("Current position: " + 			str(mouse.position))
		mouse.move((random.random()-0.5)*25, (random.random()-0.5)*25)
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

def submitClickingScript(e):
	f = open("clickingScript.txt", "a")
	f.write(e.get())
	f.write("\n")
	f.write(str(inst.coords[0]) +";"+ str(inst.coords[1])+ "\n")
	f.write(str(inst.coords[2]) +";"+ str(inst.coords[3])+ "\n")
	f.close()

print ("Current positions: " + str(mouse.position))
#mouse.position = (404, 879)#absolute

