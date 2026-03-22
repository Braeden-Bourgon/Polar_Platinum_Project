#seqtoseq
#https://www.codecademy.com/paths/build-chatbots-with-python/tracks/deep-learning-and-generative-chatbots/modules/deep-learning-for-nlp/lessons/generating-text-with-deep-learning/exercises/preprocessing-for-seq-2-seq

import keras
import re
import numpy as np
# Importing our translations
data_path = "span-eng.txt"
# Defining lines as a list of each line
with open(data_path, 'r', encoding='utf-8') as f:
  lines = f.read().split('\n')
  print("test:", lines)

# Building empty lists to hold sentences
input_docs = []
target_docs = []
# Building empty vocabulary sets
input_tokens = set()
target_tokens = set()

for line in lines:
  # Input and target sentences are separated by tabs
  input_doc, target_doc = line.split('\t')
  # Appending each input sentence to input_docs
  input_docs.append(input_doc)
  # Splitting words from punctuation
  target_doc = " ".join(re.findall(r"[\w']+|[^\s\w]", target_doc))
  # Redefine target_doc below 
  # and append it to target_docs:
  target_doc = "<START> " + target_doc + " <END>"
  target_docs.append(target_doc)
  
  # Now we split up each sentence into words
  # and add each unique word to our vocabulary set
  for token in re.findall(r"[\w']+|[^\s\w]", input_doc):
    print(token)
    # Add your code here:
    if token not in input_tokens:
      input_tokens.add(token)
  for token in target_doc.split():
    print(token)
    # And here:
    if token not in target_tokens:
      target_tokens.add(token)

input_tokens = sorted(list(input_tokens))
target_tokens = sorted(list(target_tokens))

# Create num_encoder_tokens and num_decoder_tokens:
num_encoder_tokens = len(input_tokens)
num_decoder_tokens = len(target_tokens)
try:
  max_encoder_seq_length = max([len(re.findall(r"[\w']+|[^\s\w]", input_doc)) for input_doc in input_docs])
  max_decoder_seq_length = max([len(re.findall(r"[\w']+|[^\s\w]", target_doc)) for target_doc in target_docs])
except ValueError:
  pass


print('Number of samples:', len(input_docs))
print('Number of unique input tokens:', num_encoder_tokens)
print('Number of unique output tokens:', num_decoder_tokens)
print('Max sequence length for inputs:', max_encoder_seq_length)
print('Max sequence length for outputs:', max_decoder_seq_length)

input_features_dict = dict(
    [(token, i) for i, token in enumerate(input_tokens)])
# Build out target_features_dict:
target_features_dict = dict(
  [(token, i) for i, token in enumerate(target_tokens)])

# Reverse-lookup token index to decode sequences back to
# something readable.
reverse_input_features_dict = dict(
    (i, token) for token, i in input_features_dict.items())
# Build out reverse_target_features_dict:
reverse_target_features_dict = dict(
  (i, token) for token, i in target_features_dict.items())

encoder_input_data = np.zeros(
    (len(input_docs), max_encoder_seq_length, num_encoder_tokens),
    dtype='float32')
print("\nHere's the first item in the encoder input matrix:\n", encoder_input_data[0], "\n\nThe number of columns should match the number of unique input tokens and the number of rows should match the maximum sequence length for input sentences.")

# Build out the decoder_input_data matrix:
decoder_input_data= np.zeros(
  (len(input_docs), max_decoder_seq_length,
  num_decoder_tokens), 
  dtype='float32'
)
# Build out the decoder_target_data matrix:
decoder_target_data= np.zeros(
  (len(target_docs), max_decoder_seq_length,
  num_decoder_tokens), 
  dtype='float32'
)

for line, (input_doc, target_doc) in enumerate(zip(input_docs, target_docs)):
  
  for timestep, token in enumerate(re.findall(r"[\w']+|[^\s\w]", input_doc)):
    print("Encoder input timestep & token:", timestep, token)
    print(input_features_dict[token])
    # Assign 1. for the current line, timestep, & word
    # in encoder_input_data:
    encoder_input_data[line, timestep, input_features_dict[token]] = 1.
    

  for timestep, token in enumerate(target_doc.split()):
    # decoder_target_data is ahead of decoder_input_data by one timestep
    print("Decoder input timestep & token:", timestep, token)
    # Assign 1. for the current line, timestep, & word
    # in decoder_input_data:
    decoder_input_data[line, timestep, target_features_dict[token]] = 1.
    
    if timestep > 0:
      # decoder_target_data is ahead by 1 timestep
      # and doesn't include the start token.
      print("Decoder target timestep:", timestep)
      # Assign 1. for the current line, timestep, & word
      # in decoder_target_data:
      decoder_target_data[line, timestep -1, target_features_dict[token]] = 1.
print("Dicts: ", target_features_dict, reverse_target_features_dict, reverse_input_features_dict, input_features_dict)