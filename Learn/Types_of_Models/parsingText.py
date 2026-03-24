import spacy 
from nltk import Tree
from textPreprocessing import text 

dependancy_parser = spacy.load('en_core_web_sm')

parsed_text = dependancy_parser(text)

my_sentence = "This is absolutely amazing!"
my_parsed_sentece = dependancy_parser(my_sentence)

def to_nltk_tree(node):
    if node.n_lefts + node.n_rights > 0:
        parsed_child_nodes = [to_nltk_tree(child) for child in node.children]
        return Tree(node.orth_, parsed_child_nodes)
    else: 
        return node.orth_
    
for sent in parsed_text.sents:
    to_nltk_tree(sent.root).pretty_print()

for sent in my_parsed_sentece.sents:
    to_nltk_tree(sent.root).pretty_print()