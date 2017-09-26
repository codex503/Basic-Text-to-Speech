

# import cross-platform module
import pyttsx

# set initialization to variable
engine = pyttsx.init()

# prompt for user input
print "What would you like me to say?"


engine.say(raw_input())
engine.runAndWait()
