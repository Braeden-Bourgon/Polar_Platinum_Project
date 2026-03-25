import re
from predicter import interpret, generate
from generator import generator
    

def Polar(restart, again):
    response = ""
    #Code gets user response and seperates it into phrases
    while again == True or restart == False:
        user_response = input("What do you think about plea bargaining?\n")
        user_phrases = re.split(r'[!?.;:]+', user_response)
        #Code analyzes what user is saying
        for user_phrase in user_phrases:
            norp = interpret(user_phrase)
            generatecode = generate(user_phrase)
            #Code sends the bias and phrase to the generator
            response = generator(generatecode)
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
        return restart, again
    else:
        user_response = input("Sorry, but that last response did not mention plea bargaining. \nMake sure you include words like plea, or bargain in your response. \nWhat do you think about plea bargaining?\n")
   
def Initialize():
    restart = Polar(False, False)
    while(restart[0] == True):
        Polar(True, restart[1])

print("Hey, I am Polar. I will give you a brief summary and resources that oppose your inputted viewpoint. Try it out!\n (Only works with plea bargaining rn)")

Initialize()