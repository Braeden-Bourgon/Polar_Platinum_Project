import numpy as np
import textData 
from textData import oplea, pplea, pvictim, ovictim, pjustice, ojustice, pdiscrim, odiscrim, peffecient, oeffecient 
import preProcessing
from interpreter import interpret, matched_words

generatorDictionary = {('plea', 0): pplea, ('plea', 1): oplea, ('bargain', 0): pplea, ('bargain', 1): oplea}
def Polar(restart, again): #(user_response, restart)
    response =""
    #Code gets user response and parses it
    if restart == False or again == True:
        user_response= input("What do you think about plea bargaining?\n")
    else:
        user_response= input("Sorry, but that last response did not mention plea bargaining. \nMake sure you include words like plea, or bargain in your response. \nWhat do you think about plea bargaining?\n")
    user_words = preProcessing.process(user_response)
    #Code analyzes what user is saying
    phrases = interpret(user_words)
    # print(any(phrase[0] != ('plea' or 'bargain') for phrase in phrases))
    #Code uses a response for user's phrases / perspective
    if all(phrase[0] == 'plea' or phrase[0] == 'bargain' for phrase in phrases):  
        if all(phrase[1] == -1 for phrase in phrases):
            response = textData.oplea
        elif all(phrase[1] == 0 for phrase in phrases):
            response = textData.pplea
        else:
            response="This is a mixed opinion! Great job on being moderate, but try to take a stance.\n" \
            "Maybe take one of your points and type it for next time to see an opposing side to it."
    elif any(phrase[0] != 'plea' or phrase[0] != 'bargain' for phrase in phrases):
        for phrase in phrases:
            print(generatorDictionary.get(phrase), "Not Found")
    else:
        return True, False
    print(response)
    again = input("Would you like to try again? Type y for yes or n for no.\n").lower()
    if("y" == again or "yes" == again):
        print("Awesome! Let us do it again.")
        restart = True
        again = True
    elif("n" == again or "no" ==  again):
        print("Alright! I hope you were able to learn more about the other side. Until next time!")
        restart = False
        again = False
    else:
        print("Can you try that again?")
    return restart, again


def Initialize():
    restart = Polar(False, False)
    while(restart[0] == True):
        Polar(True, restart[1])
        
print("Hey, I am Polar. I will give you a brief summary and resources that oppose your inputted viewpoint. Try it out!\n (Only works with plea bargaining rn)")
Initialize()