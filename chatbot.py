import re
from textblob import TextBlob

#later on, use encapsulation (define functions in another file, this file only has main script)

#regular expression for at and number, or days of the week, or months, or days of the month
findTime(userInput) #returns a date struct
#esther

#locations- textblob find noun
findLocation(userInput) #returns string
#esther

#function to display events, if user says "display events" or "show events"
displayEvents() #prints all the events, returns void
#kria

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

#on startup say hi i'm ur bish kevin
hello() #returns void
#shivali

#function to read input, say which parts of the event object still needs to be filled
checkEvent() #returns boolean
#kria

#chatbot response- choose a response from a set of responses
#eg "do you want me to set up an event at chipotle at 2?"
response(Event) #returns void
#kria

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
