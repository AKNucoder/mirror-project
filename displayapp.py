from tkinter import *
import forecastio
import time
import requests
import json

import PIL.Image
import PIL.ImageTk

def weather():

    api_key="cf29d83127cfdf7b9baadf86cc013b60" #dark Skies API key call

    send_url = 'http://freegeoip.net/json' #used to obtain latitude and longitude through ip
    r = requests.get(send_url)
    j = json.loads(r.text)
    latitude = j['latitude']
    longitude = j['longitude']

    forecast=forecastio.load_forecast(api_key, latitude, longitude)

    current_Weather = forecast.currently()
    daily_Summary = forecast.daily()

    summary2 = daily_Summary.summary

    summary1 = current_Weather.summary
    icon = current_Weather.icon
    temperature = str(current_Weather.temperature) + '\u00b0F'

    return (temperature, summary1, summary2, icon)


def main():
    root = Tk() #This is a blank screen
    root.configure(background ='black')



    clock = Label(root, font=('Pacifico', 72), background='black', fg = "white")
    clock.place(x = 100 , y = 100, anchor= NW)

    TempSum = weather()
    temp = TempSum[0]
    summary=TempSum[1]
    summary2=TempSum[2]
    icon = TempSum[3]

    current_temperature = Label(root, text = temp, font=('Pacifico', 72), background='black', fg = "white")
    current_temperature.place(relx = 1.0, x = -100 , y = 100, anchor= NE)

    current_summary = Label(root, text = summary, font=('Pacifico', 60), background='black', fg = "white")
    current_summary.place(relx = 1.0, x = -100 , y = 180, anchor= NE)

    current_summary = Label(root, text = summary2, font=('Pacifico', 15), background='black', fg = "white")
    current_summary.place(relx = 1.0, x = -100 , y = 260, anchor= NE)

    #default = clear day
    iconFilepath = 'photos/clear.png'

    if(icon == 'rain'):
        iconFilepath = 'photos/rain.png'

    elif(icon == 'snow' or icon == 'sleet'):
        iconFilepath = 'photos/snow.png'

    elif(icon == "wind"):
        iconFilepath = 'photos/wind.png'

    elif(icon == "fog" or icon == "cloudy" or icon == "partly-cloudy-night"):
        iconFilepath = 'photos/cloudy.png'

    elif(icon == "partly-cloudy-day"):
        iconFilepath = 'photos/partly-cloudy-day.png'

    elif(icon == "clear night"):
        iconFilepath = 'photos/clearnight.png'


#insert picture

    im = PIL.Image.open(iconFilepath)
    photo = PIL.ImageTk.PhotoImage(im)

    iconPic = Label(root, image = photo)
    iconPic.image = photo
    iconPic.place(relx = 1.0, x = -250 , y = 125, anchor= NE)



    #iconPic = Label(root, text = summary2, font=('Pacifico', 15), background='black', fg = "white")
    #iconPic.place(relx = 1.0, x = -100 , y = 260, anchor= NE)



    def tick():
        time1 = ''
        # get the current local time from the PC
        nowHour = int(time.strftime('%H'))
        nowMin = time.strftime('%M')


        if(nowHour>12):
            time2 = str(nowHour-12) + ":" + nowMin + "PM"
        else:
            if(nowHour == 0):
                nowHour = 12
                time2 = str(nowHour) + ":" + nowMin + "AM"
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


    root.mainloop()
main()


#canvas = Canvas(root, width=100, height=100)
#canvas.pack()

#blackLine= canvas.create_line(0, 0, 200, 50) #line(startx, starty, endx, endy)
#redLine= canvas.create_line(0, 0, 200, 50, fill="red")
#greenBox = canvas.create_rectangle(25,25,130, 60, fill="green")
#canvas.delete(redLine)

    #class gridpattern:
    #    def __init__(self, master):
    #        frame = Frame(master)
    #        frame.pack()

    #        self.printButton = Button(frame, text="Print Message", command=self.printMessage)
    #        self.printButton.pack(side = LEFT)

    #        self.quitButton= Button(frame, text="Quit", command=frame.quit)
    #        self.quitButton.pack(side = LEFT)

    #    def printMessage(self):
    #        print("Wow, This actually worked")

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
