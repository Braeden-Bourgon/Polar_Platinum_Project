import re
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.corpus import wordnet
from collections import Counter

stop_words = stopwords.words('english')

def get_part_of_speech(word):
    probable_part_of_speech = wordnet.synsets(word)
    pos_counts = Counter()
    pos_counts["n"] = len( [item for item in probable_part_of_speech if item.pos() == "n"])
    pos_counts["v"] = len( [item for item in probable_part_of_speech if item.pos() == "v"])
    pos_counts["a"] = len( [item for item in probable_part_of_speech if item.pos() == "a"])
    pos_counts["r"] = len( [item for item in probable_part_of_speech if item.pos() == "r"])

    most_likely_part_of_speech = pos_counts.most_common(1)[0][0]
    return most_likely_part_of_speech

def stem(text):
   
    cleaned = re.sub('\W', ' ', text)
    tokenized = word_tokenize(cleaned)

    stemmer = PorterStemmer()
    stemmed = [stemmer.stem(token) for token in tokenized]

    lemmatized = [WordNetLemmatizer().lemmatize(token, get_part_of_speech(token)) for token in tokenized]

    print("Stemmed:", stemmed)
    print("Lemmatized:", lemmatized)
    return

def process(text):
   words = re.sub(r'\s+', ' ', text).lower()
   tokens = word_tokenize(words)
   lemmatized_words = [WordNetLemmatizer().lemmatize(token, get_part_of_speech(token)) for token in tokens]
#    print("Words: ", lemmatized_words)
   return lemmatized_words

