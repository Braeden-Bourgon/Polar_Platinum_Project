from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
import numpy as np
texts = []
labels = [] # 0: positive, 1: negative
inputs = []
biases = []
targets=[]
#Opens data file
with open("data.txt", 'r', encoding='utf-8') as f:
    lines = f.read().split('\n')
#Splits lines of txt file into input and target data
for line in lines:
    text, label = line.split('$$$')
    texts.append(text.lower())
    labels.append(label)

#Opens target file
with open("targetText.txt", 'r', encoding='utf-8') as f:
    lines = f.read().split('\n')
#Splits lines of txt file into input and target data
for line in lines:
    input, bias, target = line.split('$$$')
    inputs.append(input)
    bias= "Negative" if bias == 0 else "Positive"
    biases.append(bias)
    targets.append(target)


# Creates the vectors and trains it
vectorizer = TfidfVectorizer()
txt = vectorizer.fit_transform(texts)
nb = MultinomialNB()
nb.fit(txt, labels)

gnb = MultinomialNB()
gnb.fit(txt, targets)
#Predicts whether user's input is for or against plea bargains
def interpret(userInput):
    new_text = [userInput]
    userinput = vectorizer.transform(new_text)
    probabilities = nb.predict_proba(userinput)
    #If statement where if class 0 (positive) is greater than class 1 (negative) the statement is positive
    pbias = 1 if probabilities[0][0] < probabilities[0][1] else 0
    result = (userInput, pbias)
    return result

def generate(userInput):
    new_text = [userInput]
    userinput = vectorizer.transform(new_text)
    probabilities = gnb.predict_proba(userinput)
    responsecode = int(np.argmax(probabilities))
    return responsecode
#Function used to create more sentences
def Train():
    stop = False
    userInputs = []
    while stop ==False:
        userInput = input("Test\n")
        userInputs.append(userInput)
        new_text = [userInput.lower()]
        if userInput == "q":
            for userinput in userInputs:
                if userinput != "q": 
                    with open("data.txt", "a") as f:
                        f.write("\n"+ userinput +"$$$")
                    with open("targetText.txt", "a") as f:
                        f.write("\n"+ userinput +"$$$")
            stop = True
        trainInput = vectorizer.transform(new_text)
        probabilities = nb.predict_proba(trainInput)
        print(probabilities)  #[P, N]
        print("Negative" if probabilities[0][0] < probabilities[0][1] else "Positive" )
    return 
# Train()
generate("I hate pleas")