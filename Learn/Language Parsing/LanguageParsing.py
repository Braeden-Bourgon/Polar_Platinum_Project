#Part of Speech Tagging
from textPreprocessing import process_text, Othertext
import nltk 
from nltk import pos_tag, RegexpParser, Tree
cleanedTxt = pos_tag(process_text(Othertext))
#print(cleanedTxt)
chunked = []
#Chunking 
chunk_grammar = r"""
    NP: {<DT>?<JJ>*<NN>+}
    AN: {<JJ><NN>}
"""
# create RegexpParser object here
chp = RegexpParser(chunk_grammar)
# for s in cleanedTxt:
#     testy = chunked.append(chunk_parser.parse(s))
# chunk the pos-tagged sentence at index 282 in pos_tagged_oz here
test = chp.parse(cleanedTxt)
print("Test:", test)
Tree.fromstring(str(test)).pretty_print()