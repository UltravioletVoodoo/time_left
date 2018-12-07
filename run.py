from datetime import datetime
from LeavingTime import LeavingTime
import time
import os
import sys
import tkinter


def start():
	if(checkArguments()):
		leavingTime = getLeavingTime()
		
		while(stillWorkTime(leavingTime)):
			os.system("cls")
			printTimeLeft(leavingTime)
			time.sleep(1)
		
		leaveWorkReminder()
	
	
def stillWorkTime(leavingTime):
	now = datetime.now()
	if(now < now.replace(hour = leavingTime.hour, minute = leavingTime.minute, second = leavingTime.second)):
		return True
	else:
		return False
	
	
def printTimeLeft(leavingTime):
	now = datetime.now()
	print("Work Ends in:	(" + str(leavingTime.getPercentComplete(now)) + "%)\n" + str(leavingTime.getHoursLeft(now)) + " Hours\n" + str(leavingTime.getMinutesLeft(now)) + " Minutes\n" + str(leavingTime.getSecondsLeft(now)) + " Seconds")
	
	
def getLeavingTime():
	if(len(sys.argv) == 3):
		return LeavingTime(int(sys.argv[1]), int(sys.argv[2]))

	if(len(sys.argv) == 2):
		return LeavingTime(int(sys.argv[1]))

	return LeavingTime()
	
	
def checkArguments():
	if(len(sys.argv) > 3):
		print("Too many arguments")
		return False
	
	for argument in sys.argv[1:]:
		if (not representsInteger(argument)):
			print("Bad arguments. Arguments must be integers")
			return False
			
	return True
	
	
def representsInteger(value):
	try:
		int(value)
		return True
	except ValueError:
		return False

		
def leaveWorkReminder():
	os.system("cls")
	print("Work is over. Generating popup reminder")
	root = tkinter.Tk()
	box = tkinter.Text(root, background="#d10a0a", font = ("Impact", 72))
	for x in range(1, 100):
		box.insert(tkinter.END, "    Work is done!    GO HOME!")
		if (x % 4 == 0):
			box.insert(tkinter.END, "\n")
	box.pack()
	root.mainloop()
		
		
start()

