from tkinter import *
#from datetime import datetime
#import sys
#from urllib import Request, urlopen, URLError
import urllib.request
import json
import requests

import time
#def displayTime():
#     # while True:
#     #    now = datetime.now()
#     #    currentHour= now.hour
#     #    currentMinute = now.minute
#     #    if (currentHour > 12):
#     #        time = (strftime("%H:%M", "PM"), end="", flush = True)
#     #    else:
#     #        time = (strftime("%H:%M", "AM"), end="", flush = True)
#     #    return time


def getWeather():
	

	rawResultIP = requests.get(url='http://freegeoip.net/json')
	resultIP = rawResultIP.json()

	latitude = str(resultIP['latitude'])
	longitude  = str(resultIP['longitude']) 

	
	rawResult = requests.get(url='https://api.darksky.net/forecast/aa28a61d1702958fed967991486ee6b7/'+ latitude + ',' + longitude)
	result = rawResult.json()

	currentTemp = str(result['currently']['temperature']) + '\u00b0F'
	currentSummary = result['currently']['summary']
	dailySummary = result['daily']['summary']

	icon = result['currently']['icon']

	#print('long: ' + longitude + ' and lat: ' + latitude)
	#print(currentTemp)

	return (currentTemp,currentSummary,dailySummary,icon)

	
#getWeather()

def main():
	root = Tk() #This is a blank screen
	root.configure(background ='black')
	root.attributes('-fullscreen',True)

	clock = Label(root, font=('Pacifico', 72), background='black', fg = "white")
	#clock.grid(rowspan = 1,columnspan = 1, padx=(100,10), pady =(100,10))
	#clock.grid()
	clock.place(x= 100, y=100, anchor=NW)

	def tick():
		time1 = ''
		# get the current local time from the PC
		nowHour = int(time.strftime('%H'))
		nowMin = time.strftime('%M')

		if(nowHour>12):
			time2 = str(nowHour - 12) + ":" + nowMin + "PM"
		else:
			time2 = str(nowHour) + ":" + nowMin + "AM"
		# if time string has changed, update it

		if (time2 != time1):
			time1 = time2
			clock.config(text=time2)
		# calls itself every 200 milliseconds
		# to update the time display as needed
		# could use >200 ms, but display gets jerky
		clock.after(200, tick)

	tick()


	tempSum = getWeather()
	currentTemp = tempSum[0]
	currentSummary = tempSum[1]
	dailySummary = tempSum[2]
	icon = tempSum[3]

	tempLabel = Label(root, text = currentTemp, font=('Pacifico', 72), background='black', fg = "white")
	tempLabel.place(relx=1.0, x= -100, y=100, anchor=NE)

	currentSummaryLabel = Label(root, text = currentSummary, font=('Pacifico', 60), background='black', fg = "white")
	currentSummaryLabel.place(relx=1.0, x= -100, y=180, anchor=NE)

	dailySummaryLabel = Label(root, text = dailySummary, font=('Pacifico', 15), background='black', fg = "white")
	dailySummaryLabel.place(relx=1.0, x= -100, y=260, anchor=NE)


	#Default is clear-day
	iconFilePath = ''#

	if (icon == 'rain'): #
		iconFilePath = ''
	elif (icon == 'snow' or icon == 'sleet'): #
		iconFilePath = ''
	elif (icon == 'wind'): #
		iconFilePath = ''
	elif (icon == 'fog' or icon == 'cloudy' or icon == 'partly-cloudy-night'): #
		iconFilePath = ''
	elif (icon == 'partly-cloudy-day'):#
		iconFilePath = ''
	elif (icon == 'clear-night'): #
		iconFilePath = ''


	# insert pic
	iconImage = PhotoImage(file = iconFilePath)

	iconPic = Label(root, image = iconImage)
	iconPic.place(relx=1.0, x= -25go0, y=100, anchor=NE)

	root.mainloop()
main()


#canvas = Canvas(root, width=100, height=100)
#canvas.pack()

#blackLine= canvas.create_line(0, 0, 200, 50) #line(startx, starty, endx, endy)
#redLine= canvas.create_line(0, 0, 200, 50, fill="red")
#greenBox = canvas.create_rectangle(25,25,130, 60, fill="green")
#canvas.delete(redLine)

	#class gridpattern:
	#    def __init__(self, master):
	#        frame = Frame(master)
	#        frame.pack()

	#        self.printButton = Button(frame, text="Print Message", command=self.printMessage)
	#        self.printButton.pack(side = LEFT)

	#        self.quitButton= Button(frame, text="Quit", command=frame.quit)
	#        self.quitButton.pack(side = LEFT)

	#    def printMessage(self):
	#        print("Wow, This actually worked")

	# b = gridpattern(root) #creating an instance of the class

	#button_1 = Button(root, text="Print my name", command = printName)
	#button_1.bind("<Button-1>")
	#button_1.pack()

	#label_1 = Label(root, text = "Name")
	#label_2 = Label(root, text = "Password")
	#entry_1= Entry(root)
	#entry_2= Entry(root)


	#label_1.grid(row = 0, sticky = E)
	#label_2.grid(row = 1, sticky = E)
	#entry_1.grid(row = 0, column = 1)
	#entry_2.grid(row = 1, column = 1)

	#c = Checkbutton(root, text="Keep my signed in")
	#c.grid(columnspan=2)

#one = Label(root, text = "One", bg ="red", fg="white")
#one.pack()
#two = Label(root, text = "Two", bg ="green", fg="black")
#two.pack(fill=X)
#three = Label(root, text = "Three", bg ="blue", fg="white")
#three.pack(side = LEFT, fill=Y)



#topFrame = Frame(root)
#topFrame.pack()


#bottomFrame = Frame(root)
#bottomFrame.pack(side = BOTTOM)

#button1 = Button(topFrame, text = "Button 1", fg="red")
#button2 = Button(topFrame, text = "Button 2", fg="blue")
#button3 = Button(topFrame, text = "Button 3", fg="green")
#button4 = Button(bottomFrame, text = "Button 4", fg="orange")

#button1.pack(side = LEFT)
#button2.pack(side = LEFT)
#button3.pack(side = left)
#button4.pack(side = BOTTOM)