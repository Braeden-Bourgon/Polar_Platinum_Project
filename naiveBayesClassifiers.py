#from data import training_counts
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

counter = CountVectorizer
opinion = input("What do you think about _")
review_counts = counter.transform([opinion])

classifier = MultinomialNB()
training_labels = [0] * 1000 + [1] * 1000

classifier.fit(training_counts training_labels)