import nltk, re
from nltk.tokenize import word_tokenize
from nltk.util import ngrams
from collections import Counter
from textPreprocessing import Othertext

cleaned = re.sub('\W+', ' ', Othertext).lower()
tokenized = word_tokenize(cleaned)

text_bigrams = ngrams(tokenized, 2)
text_bigrams_frequency = Counter(text_bigrams)

text_trigrams = ngrams(tokenized, 3)
text_trigrams_frequency = Counter(text_trigrams)

text_ngrams = ngrams(tokenized, 7)
text_ngrams_frequency = Counter(text_ngrams)

print("Bigrams:", text_bigrams_frequency.most_common(10))
print("Trigrams:", text_trigrams_frequency.most_common(10))
print("N-Grams:", text_ngrams_frequency.most_common(10))