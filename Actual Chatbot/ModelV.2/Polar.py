import re
from predicter import interpret
from generator import generate
def Initialize():
    restart = Polar(False, False)
    while(restart[0] == True):
        Polar(True, restart[1])

def Polar(restart, again):
    response = ""
    #Code gets user response and seperates it into phrases
    while restart == False or again == True:
        user_response = input("What do you think about plea bargaining?\n")
        user_phrases = re.split(r'[!?.;:]+', user_response)
        #Code analyzes what user is saying
        for user_phrase in user_phrases:
            norp = interpret(user_phrase)
            #Code sends the bias and phrase to the generator
            response = generate(norp)
        print(response)
        #Code checks if user wants to try again
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
        return restart, 
    else:
        user_response = input("Sorry, but that last response did not mention plea bargaining. \nMake sure you include words like plea, or bargain in your response. \nWhat do you think about plea bargaining?\n")
   

Initialize()