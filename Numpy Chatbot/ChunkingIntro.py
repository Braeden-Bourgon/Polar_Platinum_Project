from nltk import RegexpParser, Tree

pos_tagged_sentence = [('where', 'WRB'), ('is', 'VBZ'), ('the', 'DT'), ('emerald', 'JJ'), ('city', 'NN'), ('?', '.')]
chunk_grammar = "AN: {<JJ><NN>}"
chunk_parser = RegexpParser(chunk_grammar)
chunked = chunk_parser.parse(pos_tagged_sentence)
print(chunked)

Tree.fromstring(str(chunked)).pretty_print()