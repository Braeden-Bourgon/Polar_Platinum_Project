import numpy as np
import textData

#Code tells user what they are
print("Hey, I am polar. I will give you a brief summary and resources that oppose your inputted viewpoint. Try it out!/n (Only works with plea bargaining rn)")
#Code analyzes what user is saying

#Code generates response for user
data = textData.data
words = data.lower().split()

vocab = list(set(words))
vocab_size = len(vocab)

word_to_idx = {word: idx for idx, word in enumerate(vocab)}
idx_to_word = {idx: word for word, idx in word_to_idx.items()}
#Send vocab to indexs
data_indexs = [word_to_idx[word] for word in words]

bigram_counts = np.zeros((vocab_size, vocab_size))

for i in range(len(data_indexs) - 1):
    current_word = data_indexs[i]
    next_word = data_indexs[i + 1]
    bigram_counts[current_word, next_word] += 1


def predict_next_word(current_word, bigram_probabilities):
    word_idx = word_to_idx[current_word]
    next_word_probs = bigram_probabilities[word_idx]
    next_word_idx = np.random.choice(range(vocab_size), p=next_word_probs)
    return idx_to_word[next_word_idx]


def generate_sentence(start_word, bigram_probabilities, length=5):
    sentence = [start_word]
    current_word = start_word
    
    for _ in range(length):
        next_word = predict_next_word(current_word, bigram_probabilities)
        sentence.append(next_word)
        current_word = next_word

    return ' '.join(sentence).capitalize()

bigram_counts += 0.01
bigram_probabilities = bigram_counts / bigram_counts.sum(axis=1, keepdims=True)

#Code is checked by a bot and continues if passes

#Code adds sources for user