from functions import *
import re
from textblob import TextBlob
from textblob.taggers import NLTKTagger
nltk_tagger = NLTKTagger()
import random
import sys

#say hi
name = hello()
firstIteration = True
prompted = 0
exit = False

while (not exit):

#read user input and change to uppercase
    if ((not firstIteration) and prompted == 0):
        print "I'm dumb Kevin. Let me try to help you more,", name,"."
    firstIteration = False

    prompted = 0
    line = raw_input().upper()
    time = findTime(line)
    validInput = findAnything(line) or time


#if user asks to display events, print the list of events
    if (displayRequest(line)):
        displayEvents()

#else if user asks to cancel events, remove it from the list
    elif (cancelRequest(line)):
        cancelEvent(line)

#else if user asks to update events, update an event's aspect
    elif (updateRequest(line)):
        updateEvent(line)

#if the user is answering whether they have plans
    elif (line.find("YES") != -1):
            print("Tell me about them.")
            prompted = 1
    elif (line.find("NO") != -1):
            print"Life's not about staying indoors,",name, "! Go make some plans!\n\nWell do you need anything?"
            prompted = 1

#else if user mentions an event:
    #elif(time != None):
    elif (validInput == True):
    #canned response
        answer = raw_input(response())
        if (answer.upper() == 'YES'):
            event = parseInput(line, time)
            #event = Event(None, Date(None, None, None, None, None), None)
            event.date = Date(None, None, None, None, None)
            if (time != None): event.date.time = time.time
            while (event.checkEvent() == False): #maybe put this block in the checkEvent function?
                if event.name == "" or event.name == None:
                    event.name = raw_input('What is the event name?\n')
                #elif event.date == None: #this is not possible
                    #event.date = findTime(raw_input('When is this event happening?\n'))
                if event.location == "" or event.location == None:
                    event.location = raw_input('Where is it happening?\n')
                #ask for the missing part
            event.date = fillDate(event.date, line)
        else:
            print 'ok...'

#else if user says bye, change the flag
    elif (byeRequest(line)):
        exit = True

#else if user says something irrelevant, bot asks whether you have plans
    else:
        print "Do you have any plans,",name, "? ;)"
        prompted = 1


#end while

bye()
