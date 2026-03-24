#training Generator
from keras.layers import Input, LSTM, Dense
from keras.models import Model
def getModel(num_input_tokens, num_target_tokens, train_input_data, target_input_data, target_target_data): 
    input_inputs = Input(shape=(None, num_input_tokens))
    encoder_lstm = LSTM(256, return_state=True)

    # Retrieve the outputs and states:
    train_outputs, state_hidden, state_cell = encoder_lstm(input_inputs)

    # Put the states together in a list:
    encoder_states = [state_hidden, state_cell]
    print(encoder_states)

    # The decoder input and LSTM layers:
    decoder_inputs = Input(shape=(None, num_target_tokens))
    decoder_lstm = LSTM(256, return_sequences=True, return_state=True)

    # Retrieve the LSTM outputs and states:
    (decoder_outputs, decoder_state_hidden, decoder_state_cell) = decoder_lstm(decoder_inputs, initial_state = encoder_states)

    # Build a final Dense layer:
    decoder_dense = Dense(num_target_tokens, activation='softmax')

    # Filter outputs through the Dense layer:
    decoder_outputs = decoder_dense(decoder_outputs)
    print(decoder_outputs)
    return [decoder_lstm, decoder_inputs, decoder_dense]


def Train(polar_output_model): 
    from generator import num_input_tokens, num_target_tokens, train_input_data, target_input_data, target_target_data
    input_inputs = Input(shape=(None, num_input_tokens))
    encoder_lstm = LSTM(256, return_state=True)

    # Retrieve the outputs and states:
    train_outputs, state_hidden, state_cell = encoder_lstm(input_inputs)

    # Put the states together in a list:
    encoder_states = [state_hidden, state_cell]
    print(encoder_states)

    # The decoder input and LSTM layers:
    decoder_inputs = Input(shape=(None, num_target_tokens))
    decoder_lstm = LSTM(256, return_sequences=True, return_state=True)

    # Retrieve the LSTM outputs and states:
    (decoder_outputs, decoder_state_hidden, decoder_state_cell) = decoder_lstm(decoder_inputs, initial_state = encoder_states)

    # Build a final Dense layer:
    decoder_dense = Dense(num_target_tokens, activation='softmax')

    # Filter outputs through the Dense layer:
    decoder_outputs = decoder_dense(decoder_outputs)
    print(decoder_outputs)
    # Compile the model:
    # Building the training model:
    polar_output_model = Model([input_inputs, decoder_inputs], decoder_outputs)

    print("Model summary:\n")
    polar_output_model.summary()
    print("\n\n")

    polar_output_model.compile(optimizer='adam', 
                loss='categorical_crossentropy',
                metrics=['accuracy'])


    # Choose the batch size
    # and number of epochs:
    batch_size = 1
    epochs = 500

    print("Training the model:\n")
    # Train the model:
    polar_output_model.fit([train_input_data, target_input_data], 
            target_target_data,
            batch_size= batch_size,
            epochs=epochs,
            validation_split=0.2)

    polar_output_model.save('training_model.keras')