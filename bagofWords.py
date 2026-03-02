import re, nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from collections import Counter 
from textPreprocessing import get_part_of_speech, text

cleaned = re.sub('\W+', ' ', text).lower()
tokenized = word_tokenize(cleaned)
print("Token", tokenized)

stop_words = stopwords.words('english')
filtered = [word for word in tokenized if word not in stop_words]

normalized = [WordNetLemmatizer().lemmatize(token, get_part_of_speech(token)) for token in filtered]
anormalized = [WordNetLemmatizer().lemmatize(token, get_part_of_speech(token)) for token in tokenized]

bag_of_words = Counter(normalized)
abag_of_words = Counter(anormalized)
print("NOT STOP WORDS:", bag_of_words)
print("ALL WORDS:", abag_of_words)