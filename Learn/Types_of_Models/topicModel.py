import nltk, re
from textPreprocessing import Othertext, get_part_of_speech, newText, preprocess_text
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.decomposition import LatentDirichletAllocation

corpus = [Othertext, newText]
preprocessed_corpus = [preprocess_text(document) for document in corpus]

stop_list = ["the", "that", "this", "cheng", "panigrahi", "et", "al"]

def filter_out_stop_words(corpus):
    no_stops_corpus = []
    for document in corpus:
        no_stops_document = " ".join([word for word in document.split(" ") if word not in stop_list]) 
        no_stops_corpus.append(no_stops_document)
    return no_stops_corpus
filtered_for_stops = filter_out_stop_words(preprocessed_corpus)

#Bag of Words
bag_of_words_creator = CountVectorizer()
bag_of_words = bag_of_words_creator.fit_transform(filtered_for_stops)

#tf-idf 
tfidf_creator = TfidfVectorizer(min_df = 0.2)
tfidf = tfidf_creator.fit_transform(preprocessed_corpus)

#tf-idf LDA model
lda_tfidf_creator = LatentDirichletAllocation(learning_method ="online", n_components=10)
lda_tfidf = lda_tfidf_creator.fit_transform(tfidf)
print(corpus)
print('~~~~ Topics found by bag of words LDA ~~~~')
for topic_id, topic in enumerate(lda_tfidf_creator.components_):
    message = "Topic #{}: ".format(topic_id + 1)
    message += " ".join([tfidf_creator.get_feature_names_out()[i] for i in topic.argsort()[:-5:-1]])
    print(message)

print('\n\n~~~~ Topics found by tf-idf LDA ~~~~')
for topic_id, topic in enumerate(lda_tfidf_creator.components_):
    message = "Topic #{}: ".format(topic_id + 1)
    message += " ".join([tfidf_creator.get_feature_names_out()[i] for i in topic.argsort()[:-5:-1]])
    print(message)