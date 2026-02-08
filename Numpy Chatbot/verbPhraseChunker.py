#Chunking Verb Phrases
from nltk import RegexpParser, word_tokenize, pos_tag
import nltk 
nltk.download('punkt_tab')
#from pos_tagged_oz import pos_tagged_oz
from chunkCounter import chunk_counter
from searchingFinding import importanttext

words = word_tokenize(importanttext)
tagged = pos_tag(words)
chunk_grammar = "VP: {<VB.*><DT>?<JJ>*<NN><RB.?>?}"

chunk_parser = RegexpParser(chunk_grammar)

vp_chunked_oz = list()

for pos_tagged_sentence in tagged:

    vp_chunked_oz.append((chunk_parser.parse(tagged)))

most_common_vp_chunks = chunk_counter(vp_chunked_oz, "VP")
print("Most common VP chunks", most_common_vp_chunks)