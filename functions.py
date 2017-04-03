import re
import time
import calendar
from textblob import TextBlob
from textblob.taggers import NLTKTagger
nltk_tagger = NLTKTagger()
import random
import sys

class Date:

    def __init__(self, eventtime, dayOfTheWeek, month, dayNumber, year):
        self.time = eventtime #string
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
monthRe = '(JANUARY|FEBRUARY|MARCH|APRIL|MAY|JUNE|JULY|AUGUST|SEPTEMBER|OCTOBER|NOVEMBER|DECEMBER)'
timeRe = '(\d\d?)'
dayRe = '(MONDAY|TUESDAY|WEDNESDAY|THURSDAY|FRIDAY|SATURDAY)'
dateRe = '(\d\d?)'
timeRegex = '(' + dayRe + '?\s*' + monthRe + '?\s*' + dateRe + '?\s*' + yearRe +  '?\s*at\s*' + timeRe + '?)'
yearExp = re.compile(yearRe,  re.I)
monthExp = re.compile(monthRe, re.I)
timeExp = re.compile(timeRe, re.I)
dayExp = re.compile(dayRe, re.I)
dateExp = re.compile(dateRe, re.I)
fullTimeExp = re.compile(timeRegex, re.I)

detectTimeRegex = '((ON.*'+dayRe+')?AT\s\d*)'
detectTimeExp = re.compile(detectTimeRegex, re.I)

def maxLengthWord(matches):
    for line in matches:
        maxword = ''
        for x in line:
            if (len(x) > len(maxword)):
                maxword = x
        return maxword

def dateParse(dateString): #given a date string, returns a date object
    eventtime = re.search(timeExp, dateString)
    if eventtime:
        eventtime = eventtime.group(0)
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

    return Date(eventtime, dayOfTheWeek, month, dayNumber, year)
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
    index = userInput.find('TO')
    if (index != -1):
        blob = TextBlob(userInput[index:])
    else:
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

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
months = ['January','February','March', 'April', 'May', 'June', 'July', 'August','September', 'October','November','December']
def fillDate(date, line):
    text = ""
    # assuming user is smart enough not to say today & tomorrow in one line
    if (line.upper().find("TODAY") != -1 or line.upper().find("TONIGHT") != -1):
        text = "TODAY"
    if (line.upper().find("TOMORROW") != -1):
        text = "TOMORROW"
    if (date.time == "" or date.time == None):
        date.eventtime = raw_input("What time is the event?")
    month = 0
    if (text.upper() == 'TODAY' or text.upper() == 'TOMORROW'):
        localtime = time.localtime( time.time() )
        timez = localtime
        date.year = timez.tm_year
        month = timez.tm_mon
        date.month = months[timez.tm_mon - 1]
        date.dayNumber = timez.tm_mday
        if (text.upper() == 'TOMORROW'):
            # checks if today is the last day of the month
            if (date.dayNumber == calendar.monthrange(date.year, timez.tm_mon)[0]):
                date.dayNumber = 1
                # updates the month & year as necessary
                if (date.month == "December"):
                    date.month = 'January'
                    date.year = date.year + 1
                else:
                    date.month = months[timez.tm_mon]
            else:
                date.dayNumber = date.dayNumber + 1
    else:
        userinputdate = raw_input("What date is the event? (Enter in MM/DD/YYYY form)\n")
        mon, day, year = userinputdate.split("/")
        month = int(mon)
        date.month = months[month - 1]
        date.dayNumber = int(day)
        date.year = int(year)
    date.dayOfTheWeek = weekdays[calendar.weekday(date.year, month, date.dayNumber)]
    return date

eventList = []
userName = ""
#function to display events, if user says "display events" or "show events"
def displayEvents():
    for i in range(0, len(eventList)):
        e = eventList[i]
        t = "{}, {} {}, {} at {}".format(e.date.dayOfTheWeek,
            e.date.month, e.date.dayNumber, e.date.year, e.date.time)
        s = "Event: {}\nDate: {}\nLocation: {}".format(e.name, t, e.location)
        print(s)
    return ""

#startup function, greetings and getting name
def hello():
    name = raw_input("Hi, my name is Kevin. What's your name?\n")
    print "Hi,", name, "What can I help you with?"
    userName = name
    return name

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
    return (line.find("DISPLAY") != -1)

def cancelRequest(line):
    #check if user asked to cancel a request
    return (line.find("CANCEL") != -1)

def cancelEvent(line):
    #iterate through event list
    eventName = raw_input("What is the name of the event you want to remove?")
    for i in range(len(eventList)):
        if (eventList[i].name == eventName):
            eventList.remove(eventList[i])
            return
    #if event is found, remove it
    #if event isn't found, tough luck

def updateRequest(line):
#check if the user asked to update an event
    return (line.find("UPDATE") != -1)

def updateEvent(line):
    count = 0
    found = False
    #iterate through the event list
    eventName = raw_input("What is the name of the event you want to update?\n")
    for i in range(len(eventList)):
        if (eventList[i].name == eventName):
            found = True
            break
        count+=1
    if (found == False):
        print "I'm sorry bro; I couldn't find this event. Try again."
    update = raw_input("Which part of this event do you want to update? Name, Time, or Location?\n")
    if (update.upper() == "NAME"):
        eventList[count].name = raw_input("What is the new name?\n") 
    elif (update.upper() == "TIME"):
        userinputdate = raw_input("What is the new date is the event? (Enter in MM/DD/YYYY form)\n")
        mon, day, year = userinputdate.split("/")
        month = int(mon)
        eventList[count].date.month = months[month - 1]
        eventList[count].date.dayNumber = int(day)
        eventList[count].date.year = int(year)
        eventList[count].date.dayOfTheWeek = weekdays[calendar.weekday(date.year, month, date.dayNumber)]
    elif (update.upper() == "LOCATION"):
        eventList[count].location = raw_input("What is the new location?")
    else: print "I'm sorry bro; I don't understand. Try again."



def bye():
    print "Thanks for sharing your plans with ya boi Kevin! BYE,", userName, "!!!"

def byeRequest(line):
    return (line.find("BYE") != -1)
