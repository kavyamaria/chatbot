import re
from textblob import TextBlob
from textblob.taggers import NLTKTagger
nltk_tagger = NLTKTagger()
import random
import sys

class Date:

    def __init__(self, time, dayOfTheWeek, month, dayNumber, year):
        self.time = time #string
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
    for line in matches:
        maxword = ''
        for x in line: 
            if (len(x) > len(maxword)):
                maxword = x
        return maxword

def dateParse(dateString): #given a date string, returns a date object
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
    #if you don't have all the stuff, such as date number, calculate it

def findTime(userInput): #returns a date struct, given an input string
    match = re.findall(fullTimeExp, userInput)
    match = maxLengthWord(match)
    if (match == None):
        return None
    d = dateParse(match)
    return d

#locations- textblob find noun
def findLocation(userInput): #returns string
    blob = TextBlob(userInput)
    for tags in blob.pos_tags:
        if tags[1]==u'NN':
            return tags[0]
   return None

def parseInput(userInput, time):
    location = findLocation(userInput)
    #write method to find name later
    return Event("", time, location)
    #returns an event

eventList = []
#function to display events, if user says "display events" or "show events"
def displayEvents(): 
    for i in range(0, len(eventList)):
        e = eventList[i]
        t = "{}, {} {}, {} at {}".format(e.date.dayOfTheWeek,
            e.date.month, e.date.dayNumber, e.date.year, e.date.time)
        s = "Event: {}\nDate: {}\nLocation: {}".format(e.name, t, e.location)
        print(s)
    return ""

def hello():
    print "Hi, my name is Kevin. What can I help you with?"

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

def response(): #returns void
    one = random.randint(0, 3)
    two = random.randint(0, 2)
    s = "{} {}\n".format(cannedResponses[one], cannedResponses2[two])
    return s

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
            eventList.remove(eventList[i]) 
            return
    #if event is found, remove it
    #if event isn't found, tough luck

def bye():
    print 'Thanks for sharing your plans with ya boi Kevin!'

def byeRequest(line):
    return (line.upper().find("BYE") != -1)

#say hi
hello()
firstIteration = True
prompted = 0
exit = False

while (not exit):

#read user input
    if ((not firstIteration) and prompted == 0):
        print("I'm dumb Kevin. Let me try to help you more.")
    firstIteration = False

    prompted = 0
    line = raw_input()
    time = findTime(line)

#if user asks to display events, print the list of events
    if (displayRequest(line)):
        displayEvents()

#else if user asks to cancel events, remove it from the list
    elif (cancelRequest(line)):
        cancelEvent(line)

#if the user is answering whether they have plans
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
                    event.location = raw_input('Where is it happening?\n')
                #ask for the missing part
        else:
            print 'ok...'

#else if user says bye, change the flag
    elif (byeRequest(line)):
        exit = True

#else if user says something irrelevant, bot asks whether you have plans
    else:
        print "Do you have any plans? ;)"
       prompted = 1


#end while

bye()
