import re
#from textblob import TextBlob
import random

#later on, use encapsulation (define functions in another file, this file only has main script)

#regular expression for at and number, or days of the week, or months, or days of the month
findTime(userInput) #returns a date struct
#esther

#locations- textblob find noun
findLocation(userInput) #returns string
#esther

eventList = []
#keep track of list of event objects- struct
    #within this object we have date objects
#ria and kavya
#class Eventz:
#    name has a default value of "event"
#    Date
#    location
#    people? (later)

#class Date:
#   time
#   day of week
#   month
#   day number
#   year
class Date:

    def __init__(self, time, dayOfTheWeek, month, dayNumber, year):
        self.time = time #string object
        self.dayOfTheWeek = dayOfTheWeek
        self.month = month
        self.dayNumber = dayNumber
        self.year = year

class Event:

    def __init__(self, name, date, location):
        self.name = name
        self.date = date
        self.location = location

    #kria
    #function to read input, say which parts of the event object still needs to be filled
    def checkEvent(self):
        if self.name == "":
            return False
        if self.date == None:
            return False
        if self.location == "":
            return False
        eventList.append(self)
        return True

#function to display events, if user says "display events" or "show events"
def displayEvents(): #prints all the events, returns void
    #kria
    for i in range(0, len(eventList)):
        e = eventList[i]
        t = "{}, {} {}, {} at {}".format(e.date.dayOfTheWeek,
            e.date.month, e.date.dayNumber, e.date.year, e.date.time)
        s = "Event: {}\nDate: {}\nLocation: {}".format(e.name, t, e.location)
        print(s)

#on startup say hi i'm ur bish kevin
hello() #returns void
#shivali

cannedResponses = ["It's a date!", "Sounds like a plan!", "Okay!", "Litty."]
cannedResponses2 = ["Should I make an event for that?", "Would you like me to add that to the calendar?",
    "Would you like me to create an event for that?"]
#chatbot response- choose a response from a set of responses
#eg "do you want me to set up an event at chipotle at 2?"
def response(): #returns void
    #kria
    one = random.randint(0, 3)
    two = random.randint(0, 2)
    s = "{} {}".format(cannedResponses[one], cannedResponses2[two])
    print(s)

# stuff to test kria functions
#d = Date("11:00", "Monday", "April", 25, 2017)
#e = Event("Party!", d, "Joe's")
#e.checkEvent()
#d2 = Date("5:00pm", "Sunday", "July", 31, 2017)
#e2 = Event("Pray", d2, "Presby")
#e2.checkEvent()
#d3 = Date("5:00pm", "Sunday", "July", 31, 2017)
#e3 = Event("", d3, "Presby")
#e3.checkEvent()
#displayEvents()
#response()
#response()
#response()

#bye -> leave the while loop

#SCRIPT: (shivesther)

#say hi

#while (flag)

#read user input

#if user asks to display events, print the list of events

#else if user asks to cancel events, remove it from the list

#else if user mentions an event:
    #canned response
    #if event object isnt filled, ask for the missing part
    #create event object and add it to the list

#else if user says something irrelevent, bot asks "do you have any plans? ;)"

#else if user says bye, change the flag

#end while
