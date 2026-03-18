#Creating a Binary language model
import numpy as np

#sample dataset: a small text corpus
corpus = """Artificial intelligence is the new electricity
Machine learning is the future of AI. 
AI is transforming industries and shaping the future."""

#Tokenize corpus into words
words = corpus.lower().split()

#Create a Vocab list
vocab = list(set(words))
vocab_size = len(vocab)

print(f"Vocabulary: {vocab}")
print(f"Vocabulary Size: {vocab_size}")

word_to_idx = {word: idx for idx, word in enumerate(vocab)}
idx_to_word = {idx: word for word, idx in word_to_idx.items()}

#Convert the words in the corups to indices
corpus_indices = [word_to_idx[word] for word in words]

# Initialize bigram counts matrix
bigram_counts = np.zeros((vocab_size, vocab_size))

# Count occurerences of each bigram in the corpus
for i in range(len(corpus_indices) - 1):
    current_word = corpus_indices[i]
    next_word = corpus_indices[i + 1]
    bigram_counts[current_word, next_word] += 1

#Apply Laplace smoothing by adding 1 to all bigram counts =/ inflating prob, but also ensuring there is no 0 probabilities
bigram_counts += 0.01

#Normalize the counts to get probabilities
bigram_probabilities = bigram_counts / bigram_counts.sum(axis=1, keepdims=True)

print("Bigram probabilities matrix: ", bigram_probabilities)

#Compares all probabilities and selects word based off of that
def predict_next_word(current_word, bigram_probabilities):
    word_idx = word_to_idx[current_word]
    next_word_probs = bigram_probabilities[word_idx]
    next_word_idx = np.random.choice(range(vocab_size), p=next_word_probs)
    return idx_to_word[next_word_idx]

#Testing model with a word
current_word = "ai"
next_word = predict_next_word(current_word, bigram_probabilities)
print(f"Given '{current_word}', the model predicts '{next_word}'.")

#Generating a sentence
def generate_sentence(start_word, bigram_probabilities, length=5):
    sentence = [start_word]
    current_word = start_word
    
    for _ in range(length):
        next_word = predict_next_word(current_word, bigram_probabilities)
        sentence.append(next_word)
        current_word = next_word

    return ' '.join(sentence)

#Generate a sentence starting with "artificial"
generated_sentence = generate_sentence("artificial", bigram_probabilities, length = 10)
print(f"Generated sentence: {generated_sentence.capitalize()}")


