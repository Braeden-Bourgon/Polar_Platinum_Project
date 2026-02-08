from nltk import RegexpParser 
#from pos_tagged_oz import pos_tagged_oz
from chunkCounter import chunk_counter

chunk_grammar = "NP: {<DT>?<JJ>*<NN>}"
chunk_parser = RegexpParser(chunk_grammar)
np_chunked_oz = list()