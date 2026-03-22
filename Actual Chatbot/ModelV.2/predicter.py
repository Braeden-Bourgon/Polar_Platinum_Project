from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer

texts = []
labels = [] # 0: positive, 1: negative

#Opens data file
with open("data.txt", 'r', encoding='utf-8') as f:
    lines = f.read().split('\n')
#Splits lines of txt file into input and target data
for line in lines:
    text, label = line.split('$$$')
    texts.append(text.lower())
    labels.append(label)

# Creates the vectors and trains it
vectorizer = CountVectorizer()
txt = vectorizer.fit_transform(texts)
nb = MultinomialNB()
nb.fit(txt, labels)

#Predicts whether user's input is for or against plea bargains
def interpret(userInput):
    new_text = [userInput]
    userinput = vectorizer.transform(new_text)
    probabilities = nb.predict_proba(userinput)
    #If statement where if class 0 (poistive) is greater than class 1 (negative) the statement is positive
    pbias = False if probabilities[0][0] < probabilities[0][1] else True
    result = [pbias, userInput]
    print(result)
    return result

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
            stop = True
        trainInput = vectorizer.transform(new_text)
        probabilities = nb.predict_proba(trainInput)
        print(probabilities)  #[P, N]
        print("Negative" if probabilities[0][0] < probabilities[0][1] else "Positive" )
    return 
Train()