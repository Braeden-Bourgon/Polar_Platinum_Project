import numpy as np
import re
from keras.models import Model, load_model
from keras.layers import Input
from trainingGenerator import getModel

matched_words = ['plea', 'bargain', 'innocent', 'prosecutor', 'system', 'defendant', 'justice', 'lawyer', 'judge']
trainInputData = []
trainTargetData = []
input_tokens = set()
target_tokens = set()
trainInputs = []
trainTargets = []

with open("targetText.txt", 'r', encoding='utf-8') as f:
    lines = f.read().split('\n')
    for line in lines:
        #For phrase generation
        trainInputPoint, trainingBias, targetPoint = line.split("$$$")
        trainInputData.append((trainInputPoint.lower(), trainingBias))
        trainTargetData.append(targetPoint.lower())
        #For word generation
        target_phrase = " ".join(re.findall(r"[\w']+|[^\s\w]", targetPoint))
        # target_phrase ="$$$" + target_phrase + "$$$"
        trainTargets.append(target_phrase)
        input_phrase = " ".join(re.findall(r"[\w']+|[^\s\w]", trainInputPoint))
        trainInputs.append(input_phrase)
        for token in re.findall(r"[\w']+|[^\s\w]", input_phrase): 
            if token not in input_tokens:
                input_tokens.add(token)
        for token in target_phrase.split():
            if token not in target_tokens:
                target_tokens.add(token)

input_tokens = sorted(list(input_tokens))
target_tokens = sorted(list(target_tokens))
num_input_tokens = len(input_tokens)
num_target_tokens = len(target_tokens)
try:
  max_input_seq_length = max([len(re.findall(r"[\w']+|[^\s\w]", input_doc)) for input_doc in trainInputs])
  max_target_seq_length = max([len(re.findall(r"[\w']+|[^\s\w]", target_doc)) for target_doc in trainTargets])
except ValueError:
  pass

input_features_dict = dict(
    [(token, i) for i, token in enumerate(input_tokens)])

target_features_dict = dict(
  [(token, i) for i, token in enumerate(target_tokens)])

reverse_input_features_dict = dict(
    (i, token) for token, i in input_features_dict.items())
# Build out reverse_target_features_dict:
reverse_target_features_dict = dict(
  (i, token) for token, i in target_features_dict.items())

train_input_data = np.zeros(
    (len(trainInputs), max_input_seq_length, num_input_tokens),
    dtype='float32')

target_input_data= np.zeros(
  (len(trainInputs), max_target_seq_length,
  num_target_tokens), 
  dtype='float32'
)
# Build out the decoder_target_data matrix:
target_target_data= np.zeros(
  (len(trainTargets), max_target_seq_length,
  num_target_tokens), 
  dtype='float32'
)

for line, (input_doc, target_doc) in enumerate(zip(trainInputs, trainTargets)):
  
    for timestep, token in enumerate(re.findall(r"[\w']+|[^\s\w]", input_doc)):
        train_input_data[line, timestep, input_features_dict[token]] = 1.
    

    for timestep, token in enumerate(target_doc.split()):
        target_input_data[line, timestep, target_features_dict[token]] = 1.
    
    if timestep > 0:
      target_target_data[line, timestep, target_features_dict[token]] = 1. 


def subject(user_phrase):
    #subject is the bias and phrase
    subject = [user_phrase[0],user_phrase[1]]
    for word in matched_words:
        if word in user_phrase: 
            subject.append(word)
    return subject

def generate(user_phrase):
    # subject = subject(user_phrase)
    # print(subject)
    response = ""
    training_model = load_model('training_model.keras')
    encoder_inputs = training_model.input[0]
    encoder_outputs, state_h_enc, state_c_enc = training_model.layers[2].output
    encoder_states = [state_h_enc, state_c_enc]

    decoder_lstm = getModel(num_input_tokens, num_target_tokens, train_input_data, target_input_data, target_target_data)[0]
    decoder_inputs = getModel(num_input_tokens, num_target_tokens, train_input_data, target_input_data, target_target_data)[1]
    decoder_dense = getModel(num_input_tokens, num_target_tokens, train_input_data, target_input_data, target_target_data)[2]
    # Building the encoder test model:
    encoder_model = Model(encoder_inputs, encoder_states)
    latent_dim = 256
    # Building the two decoder state input layers:
    decoder_state_input_hidden = Input(shape=(latent_dim,))

    decoder_state_input_cell = Input(shape=(latent_dim,))

    # Put the state input layers into a list:
    decoder_states_inputs = [decoder_state_input_hidden, decoder_state_input_cell]

    # Call the decoder LSTM:
    decoder_outputs, state_hidden, state_cell =decoder_lstm(decoder_inputs, initial_state=decoder_states_inputs)
    decoder_states = [state_hidden, state_cell]
    # Redefine the decoder outputs:
    decoder_outputs = decoder_dense(decoder_outputs)
    # Build the decoder test model:
    decoder_model= Model([decoder_inputs] + decoder_states_inputs, [decoder_outputs] + decoder_states)
    print(user_phrase)
    words = []
    words.append(user_phrase.split())
    for token in re.findall(r"[\w']+|[^\s\w]", input_phrase): 
        if token not in input_tokens:
            input_tokens.add(token)
    print(words)
    user_input_data = np.zeros((len(words), max_input_seq_length, num_input_tokens),
    dtype='float32')
    userInput = user_input_data
    response = decode_sequence(userInput, encoder_model, decoder_model)
    print(response)
    return response

def decode_sequence(test_input,encoder_model,decoder_model):
  # Encode the input as state vectors:
  encoder_states_value = encoder_model.predict(test_input)
  print(len(test_input))
  # Set decoder states equal to encoder final states
  decoder_states_value = encoder_states_value
  # Generate empty target sequence of length 1:
  target_seq = np.zeros((1, 1, num_target_tokens))
  
  # Populate the first token of target sequence with the start token:
  target_seq[0, 0, 0] = 1.
  
  decodedPhrase = ''
  stop_condition = False
  while not stop_condition:
    # Run the decoder model to get possible 
    # output tokens (with probabilities) & states
    output_tokens, new_decoder_hidden_state, new_decoder_cell_state = decoder_model.predict([target_seq] + decoder_states_value)

    # Choose token with highest probability
    sampled_token_index = np.argmax(output_tokens[0, -1, :])
    sampled_token = reverse_target_features_dict[sampled_token_index]
    decodedPhrase += " " + sampled_token
    # Exit condition: either hit max length
    # or find stop token.
    if (len(decodedPhrase) > 100):
      stop_condition = True

    # Update the target sequence (of length 1).
    target_seq = np.zeros((1, 1, num_target_tokens))
    target_seq[0, 0, sampled_token_index] = 1.

    # Update states
    decoder_states_value =[new_decoder_hidden_state, new_decoder_cell_state]
    print("Phrase:",decodedPhrase)
  return decodedPhrase
  
generate("I hate pleas more")