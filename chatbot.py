#https://x.ai/how-to-teach-a-machine-to-understand-us/
#https://x.ai/a-peek-at-x-ais-data-science-architecture/
import re
from textblob import TextBlob
from textblob.taggers import NLTKTagger
nltk_tagger = NLTKTagger()
import random
import sys

#later on, use encapsulation (define functions in another file, this file only has main script)

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
        if (self.name == "") or (self.name == None):
            return False
        if self.date == None:
            return False
        if (self.location == "") or (self.location == None):
            return False
        eventList.append(self)
        print("Added!")   
        return True


#regular expression for at and number, or days of the week, or months, or days of the month

yearRe = '(\d\d\d\d)'
monthRe = '(January|February|March|April|May|June|July|August|September|October|November|December)'
timeRe = '(\d\d?)'
dayRe = '(Monday|Tuesday|Wednesday|Thursday|Friday|Saturday)'
dateRe = '(\d\d?)'
timeRegex = '(' + dayRe + '?\s*' + monthRe + '?\s*' + dateRe + '?\s*' + yearRe +  '?\s*at\s*' + timeRe + '?)'
yearExp = re.compile(yearRe,  re.I)
monthExp = re.compile(monthRe, re.I)
timeExp = re.compile(timeRe, re.I)
dayExp = re.compile(dayRe, re.I)
dateExp = re.compile(dateRe, re.I)
fullTimeExp = re.compile(timeRegex, re.I)

detectTimeRegex = '(([Oo]n.*)?at\s\d*)'
detectTimeExp = re.compile(detectTimeRegex, re.I)

def maxLengthWord(matches):
    for line in matches: #print out all found dates
        maxword = ''
        for x in line:  #since the regular expressions contain multiple groups, findall() returns multiple groups for each date. We print only the longest one.
            if (len(x) > len(maxword)):
                maxword = x
        return maxword

def dateParse(dateString): #given a date string, returns a date object
#    dateString = maxLengthWord(dateString)
#    print dateString

    time = re.search(timeExp, dateString)
    if time:
        time = time.group(0)
    dayOfTheWeek = re.search(dayExp, dateString)
    if dayOfTheWeek:
        dayOfTheWeek = dayOfTheWeek.group(0)
    month = re.search(monthExp, dateString)
    if month:
        month = month.group(0)
    dayNumber = re.search(dateExp, dateString)
    if dayNumber:
        dayNumber = dayNumber.group(0)
    year = re.search(yearExp, dateString)
    if year:
        year = year.group(0)

    return Date(time, dayOfTheWeek, month, dayNumber, year)

    #if you don't have all the stuff, ask for it again
    #if you don't have all the stuff, such as date number, calculate it?
    #wow look the datetime module has lots of date objects already

def findTime(userInput): #returns a date struct, given an input string
    match = re.findall(fullTimeExp, userInput)
    match = maxLengthWord(match)
    if (match == None):
        return None
    d = dateParse(match)
    return d

#locations- textblob find noun
def findLocation(userInput): #returns string
    #a;lkshfaospigh
#    return None
    blob = TextBlob(userInput)
    for tags in blob.pos_tags:
        if tags[1]==u'NN':
            return tags[0]
    #if len(nouns) > 0:
    #    return nouns[0]
    return None

def parseInput(userInput, time):
    location = findLocation(userInput)
    #write method to find name later
    return Event("", time, location)
    #returns an event

eventList = []
#function to display events, if user says "display events" or "show events"
def displayEvents(): #prints all the events, returns void
    #kria
    for i in range(0, len(eventList)):
        e = eventList[i]
        t = "{}, {} {}, {} at {}".format(e.date.dayOfTheWeek,
            e.date.month, e.date.dayNumber, e.date.year, e.date.time)
        s = "Event: {}\nDate: {}\nLocation: {}".format(e.name, t, e.location)
        print(s)
    return ""

#on startup say hi i'm ur bish kevin
def hello(): #returns void
    print "Hi, my name is Kevin. What can I help you with?"
#shivali

def ynResponse(line):
    s = ""
    if line.upper().find("YES") != -1 or line.upper().find("Y") != -1:
        s = "Tell me about them."
    elif line.upper().find("NO") != -1 or line.upper().find("N") != -1:
        s = "Life's not about staying indoors. Go make some plans!\n\nWell do you need anything?"
    else:
        s = "Um...K"
    return s

cannedResponses = ["It's a date!", "Sounds like a plan!", "Okay!", "Litty."]
cannedResponses2 = ["Should I make an event for that?", "Would you like me to add that to the calendar?",
    "Would you like me to create an event for that?"]
#chatbot response- choose a response from a set of responses
#eg "do you want me to set up an event at chipotle at 2?"
def response(): #returns void
    #kria
    one = random.randint(0, 3)
    two = random.randint(0, 2)
    s = "{} {}\n".format(cannedResponses[one], cannedResponses2[two])
    return s

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

def byeRequest(line):
    return (line.upper().find("BYE") != -1)

#SCRIPT: (shivesther)

#say hi
hello()
iterations = 0
prompted = 0
exit = False
#while (flag)
while (not exit):
#read user input
    if (iterations > 0 and prompted == 0):
        print("I'm dumb Kevin. Let me try to help you more.")

    prompted = 0
    line = raw_input()
    time = findTime(line)
#if user asks to display events, print the list of events
    if (displayRequest(line)):
        displayEvents()
#else if user asks to cancel events, remove it from the list
    elif (cancelRequest(line)):
        cancelEvent(line)
    elif (line.upper().find("YES") != -1):
            print("Tell me about them.")
            prompted = 1
    elif (line.upper().find("NO") != -1):
            print("Life's not about staying indoors. Go make some plans!\n\nWell do you need anything?")
            prompted = 1
    #else if user mentions an event:
    elif(time != None):
    #canned response
        answer = raw_input(response())
        if (answer.upper() == 'YES'):
            event = parseInput(line, time)
            while (event.checkEvent() == False): #maybe put this in the checkEvent function?
                if event.name == "" or event.name == None:
                    event.name = raw_input('What is the event name?\n')
                elif event.date == None: #this is not possible
                    event.date = findTime(raw_input('When is this event happening?\n'))
                elif event.location == "" or event.location == None:
                    event.location = raw_input('Where is it happening?\n')                #ask for the missing part
        else:
            print 'ok...'

#else if user says bye, change the flag
    elif (byeRequest(line)):
        exit = True

#else if user says something irrelevent, bot asks "do you have any plans? ;)"
    else:
        print "Do you have any plans? ;)"
        #ynResponse(line)

        #userResponse = raw_input("Do you have any plans ;)\n")
        #ynResponse(userResponse)
        prompted = 1

    iterations += 1
#end while

bye()
