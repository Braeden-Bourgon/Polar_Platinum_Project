import re
from nltk import word_tokenize, ngrams
from collections import Counter
matched_words = {"plea", 'bargain'}
matches = []
newData = []
length = range(1, 8)
def interpret(userwords): 
    for userword in userwords: 
        for matchedword in matched_words: 
            if userword == matchedword:
                match = userword
                matches.append(match)
            continue
        continue
    user_phrase = phrases(matches, userwords)
    return user_phrase

def phrases(matches, words):
    phrases = []
    for match in matches: 
        phrase = (match)
        for time in length: 
           if((words[words.index(match) + time]) != ("." or "!" or"?")):
               phrase += " " +(words[words.index(match) +time])
           else: 
               break 
        print(phrases)
        phrases.append(phrase)
    return phrases

# def addData(phrases):
#     for phrase in phrases:
#       newData.append(phrase)
#       with open(')
#I think pleas are very terrible. Bargaining is a very bad practice and should not be considered in the United States.