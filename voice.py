

# # prompt user for instructions
# print "What would you like me to say?"
# # create a variable to store input to string
# speech = raw_input()
# # 
# print speech

import pyttsx
engine = pyttsx.init()
print "What would you like me to say?"

engine.say(raw_input())
engine.runAndWait()