#https://www.codecademy.com/paths/build-chatbots-with-python/tracks/deep-learning-and-generative-chatbots/modules/deep-learning-for-nlp/lessons/generating-text-with-deep-learning/exercises/encoder-training-setup
from seqtoseq import num_encoder_tokens, num_decoder_tokens, decoder_target_data, encoder_input_data, decoder_input_data, decoder_target_data
from keras.layers import Input, LSTM, Dense
from keras.models import Model

# Create the input layer:
encoder_inputs = Input(shape=(None, num_encoder_tokens))

# Create the LSTM layer:
encoder_lstm = LSTM(256, return_state=True)

# Retrieve the outputs and states:
encoder_outputs, state_hidden, state_cell = encoder_lstm(encoder_inputs)

# Put the states together in a list:
encoder_states = [state_hidden, state_cell]
print(encoder_states)

# The decoder input and LSTM layers:
decoder_inputs = Input(shape=(None, num_decoder_tokens))
decoder_lstm = LSTM(256, return_sequences=True, return_state=True)

# Retrieve the LSTM outputs and states:
(decoder_outputs, decoder_state_hidden, decoder_state_cell) = decoder_lstm(decoder_inputs, initial_state = encoder_states)

# Build a final Dense layer:
decoder_dense = Dense(num_decoder_tokens, activation='softmax')

# Filter outputs through the Dense layer:
decoder_outputs = decoder_dense(decoder_outputs)
print(decoder_outputs)

# Building the training model:
training_model = Model([encoder_inputs, decoder_inputs], decoder_outputs)

print("Model summary:\n")
training_model.summary()
print("\n\n")

# Compile the model:
training_model.compile(optimizer='rmsprop', 
              loss='categorical_crossentropy',
              metrics=['accuracy'])


# Choose the batch size
# and number of epochs:
batch_size = 11
epochs = 500

print("Training the model:\n")
# Train the model:
training_model.fit([encoder_input_data, decoder_input_data], 
          decoder_target_data,
          batch_size= batch_size,
          epochs=epochs,
          validation_split=0.2)

training_model.save('training_model.keras')