import numpy as np
import textData
import preProcessing
import interpreter
#Code tells user what they are
print("Hey, I am polar. I will give you a brief summary and resources that oppose your inputted viewpoint. Try it out!\n (Only works with plea bargaining rn)")
#Code gets user response and parses it
user_response= input("What do you think about plea bargaining?\n")
user_words = preProcessing.process(user_response)
#Code analyzes what user is saying
phrases = interpreter.interpret(user_words)
print("Phrases: ", phrases)
#Code uses a response for user's phrases / perspective 


# Response adds sources onto it
