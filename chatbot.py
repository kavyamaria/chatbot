#https://x.ai/how-to-teach-a-machine-to-understand-us/
#https://x.ai/a-peek-at-x-ais-data-science-architecture/
import re
#from textblob import TextBlob
import random
import sys

#later on, use encapsulation (define functions in another file, this file only has main script)

#regular expression for at and number, or days of the week, or months, or days of the month

yearRe = '(\d\d\d\d)'
monthRe = '(January|February|March|April|May|June|July|August|September|October|November|December)'
timeRe = '(\d\d?)'
dayRe = '(Monday|Tuesday|Wednesday|Thursday|Friday|Saturday)'
dateRe = '(\d\d?)'
timeRegex = '(' + dayRe + '\s*' + monthRe + '\s*' + dateRe + '\s*at\s*' + timeRe + ')'
yearExp = re.compile(yearRe,  re.I)
monthExp = re.compile(monthRe, re.I)
timeExp = re.compile(timeRe, re.I)
dayExp = re.compile(dayRe, re.I)
dateExp = re.compile(dateRe, re.I)
fullTimeExp = re.compile(timeRegex, re.I)

def dateParse(dateString): #given a date string, returns a date object
    month = re.search(monthExp, dateString)
    time = re.search(timeExp, dateString)
    
    return Date(time, dayOfTheWeek, month, dayNumber, year)

    #if you don't have all the stuff, ask for it again
    #if you don't have all the stuff, such as date number, calculate it?
    #wow look the datetime module has lots of date objects already

def findTime(userInput): #returns a date struct, given an input string
    match = re.search(timeExp, userInput)
    if (match == None):
        return None
    d = dateParse(match)
    return d

#locations- textblob find noun
def findLocation(userInput): #returns string
    #a;lkshfaospigh

def parseInput(userInput, time):
    location = findLocation(userInput)
    #write method to find name later
    return Event("", time, location) 
    #returns an event

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
def hello(): #returns void
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

def displayRequest(line):
    #check if the user asked to display events
    return (line.upper().find("DISPLAY") != -1)

def cancelRequest(line):
    #check if user asked to cancel a request
    return (line.upper().find("CANCEL") != -1)

def cancelEvent(line):
    #iterate through event list
    eventName = raw_input("What is the name of the event you want to remove?")
    for i in range(len(eventList)):
        if (eventList[i].name == eventName):
            eventList.remove(eventList[i]) #is this good syntax??
            return
    #if event is found, remove it
    #if event isn't found, tough luck 

#bye -> leave the while loop
def bye():
    print 'kthxbai'

#SCRIPT: (shivesther)

#say hi
hello()

exit = false
#while (flag)
while (!exit):

#read user input
    line = raw_input()
#if user asks to display events, print the list of events
    if (displayRequest(line)):
        displayEvents()
#else if user asks to cancel events, remove it from the list
    elif (cancelRequest(line)):
        cancelEvent(line)
#else if user mentions an event:
    elif((time = findTime(line)) != None):
    #canned response
        answer = raw_input(response())
        event = parseInput(line, time)
        if (answer.upper() == 'YES'):
            while (!event.checkEvent): #maybe put this in the checkEvent function?
                if self.name == "":
                    self.name = raw_input('What is the event name?')
                elif self.date == None: #this is not possible
                    self.date = findTime(raw_input('When is this event happening?'))
                elif self.location == "":
                    self.location = findLocation(raw_input('Where is it happening?'))                #ask for the missing part
        else:
            print 'ok...'

#else if user says bye, change the flag
    elif (byeRequest(line)):
        exit = false

#else if user says something irrelevent, bot asks "do you have any plans? ;)"
    else
        print "Do you have any plans? ;)"

#end while

bye()
