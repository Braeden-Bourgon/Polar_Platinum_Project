#Part-Of-Speech Tagging
import nltk
from  nltk import pos_tag
'''
NN = Noun
    NNS = Plural
    NNP = Proper 
        NNPS = Proper plural
PRP = Pronoun
    PRP$ = Possesive
        WP$ = Possesive Wh
    WP = Wh-prounoun
DT = Determiner (article)
    PDT = Predeterminer
    WDT = Wh-determiner
VB = Verb
    VBD = base form
    VBG = present participle
    VBN = past participle
    VBP = non-3rd person singular present
    VBZ = 3rd person singular present
JJ = Adjective
    JJR = Comparative
    JJS = Superlative
RB = Adverb
    RBR = Comparative
    RBS = Superlative
    WRD = Wh-Adverb
IN = Preposition
CC = Conjunction
UH = Interjection
'''

word_sentence = ['Wow', 'do','you','suppose', 'oz', 'quickly', 'could', 'give', 'me', 'a', 'very', 'big', 'and', 'healthy', 'heart', 'on', 'Wednesday' '?']
part_of_speech_tagged_sentence = pos_tag(word_sentence)
print(part_of_speech_tagged_sentence)