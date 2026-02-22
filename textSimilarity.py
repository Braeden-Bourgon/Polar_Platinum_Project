import nltk


from nltk.metrics import edit_distance

def print_levenshtein(string1, string2):
    print("The Levenshtein distance from '{0}' to '{1}' is {2}!".format(string1, string2, edit_distance(string1, string2)))