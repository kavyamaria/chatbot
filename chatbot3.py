from functions3 import *
#from speech import *
import re
#from textblob import TextBlob
#from textblob.taggers import NLTKTagger
#nltk_tagger = NLTKTagger()
import random
import sys

#say hi
name = hello()
firstIteration = True
prompted = 0
exit = False

while (not exit):

   # print("f")
#read user input and change to uppercase
    if ((not firstIteration) and prompted == 0):
        speak("\nI'm dumb Kevin. Let me try to help you more,"+name+".")
    firstIteration = False

    prompted = 0
    line = listen().upper()
    print(line)
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
            #print("djjf g f")
            print("Tell me about them")
            speak("Tell me about them")
            prompted = 1
    elif (line.find("NO") != -1):
            print("Life's not about staying indoors,"+name+ "! Go make some plans!\n\nWell do you need anything?")
            speak("Life's not about staying indoors,"+name+ "! Go make some plans!\n\nWell do you need anything?")
            prompted = 1

#else if user mentions an event:
    #elif(time != None):
    elif (validInput == True):
    #canned response
         #print("shrek")
       # answer = listen(response())
        #print(response())
        r = response()
        print(r)
        speak(r)
        answer = listen()
        if (answer.upper() == 'YES'):
            event = parseInput(line, time)
            #event = Event(None, Date(None, None, None, None, None), None)
            event.date = Date(None, None, None, None, None)
            event.date.time = searchForTime(line)
            event.name = getEventName(event, line)
            while (event.checkEvent() == False): #maybe put this block in the checkEvent function?
                if event.name == "" or event.name == None:
                    speak("What is the event name")
                    print("What is the event name")
                    event.name = listen();
                if event.location == "" or event.location == None:
                    print("Where is it happening?\n")
                    speak("Where is it happening?\n")
                    event.location = listen()
                #ask for the missing part
            event.date = fillDate(event.date, line)
        else:
            print("ok...")
            speak('ok...')

#else if user says bye, change the flag
    elif (byeRequest(line)):
        exit = True

#else if user says something irrelevant, bot asks whether you have plans
    else:
        print("Do you have any plans,"+name+"? ;)")
        speak("Do you have any plans,"+name+"? ;)")
        prompted = 1



#end while

bye()

#end while
