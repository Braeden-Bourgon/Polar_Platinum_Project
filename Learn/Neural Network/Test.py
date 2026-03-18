input_vector = [1.72, 1.23]
weights_1 = [1.26, 0]
weights_2 = [2.17, 0.32]

first_indexs_mult = input_vector[0] * weights_1[0]
second_indexs_mult = input_vector[1] * weights_1[1]
dot_product_1 = first_indexs_mult + second_indexs_mult

print(f"The dot product is: {dot_product_1}")

import numpy as np
dot_product_1 = np.dot(input_vector, weights_1)
print(f"The real dot product is: {dot_product_1}")

dot_product_2= np.dot(input_vector, weights_2)
print(f"The second dot product is: {dot_product_2}")


#Wrapping vectors in NumPy arrays
input_vector = np.array([1.66, 1.56])
weights_1 = np.array([1.45, -0.66])
bias = np.array([0.0])

def sigmoid(x):
    return 1 / (1 + np.exp(-x))
def make_prediction(input_vector, weights, bias):
    layer_1 = np.dot(input_vector, weights) + bias
    layer_2 = sigmoid(layer_1)
    return layer_2

prediction = make_prediction(input_vector, weights_1, bias)
print(f"The prediction result is: {prediction}")

input_vector = np.array([2, 1.5])
prediction = make_prediction(input_vector, weights_1, bias)
print(f"The prediction result is: {prediction}")

#Compute Error
target = 0 
mse = np.square(prediction - target)
print(f"Prediction: {prediction}; Error: {mse}")

derivative = 2 * (prediction - target)
print(f"The derivative is {derivative}")

#Updating Weights
weights_1 = weights_1 - derivative 
prediction = make_prediction(input_vector, weights_1, bias)
error = (prediction - target) ** 2
print(f"Prediction: {prediction}; Error: {error}")


#Chain Rule
'''derror_dweights = (
    derror_dprediction * dprediction_dlayer1 * dlayer1_dweights
)'''
def sigmoid_deriv(x):
    return sigmoid(x) * (1-sigmoid(x))

derror_dprediction = 2 * (prediction - target)
layer_1 = np.dot(input_vector, weights_1) + bias
dprediction_dlayer1 = sigmoid_deriv(layer_1)
dlayer1_dbias = 1
dlayer1_weights = (1 * weights_1[1]) * (1 * weights_1[0])

derror_dbias = (
    derror_dprediction * dprediction_dlayer1 * dlayer1_dbias
)
print(f"Error Bias{derror_dbias}")
derror_dweights = (
    derror_dprediction * dprediction_dlayer1 * dlayer1_weights
)
print(f"Error Weights{derror_dweights}")

import NeuralNetworkClass
learning_rate = 0.1

neural_network = NeuralNetworkClass.NeuralNetwork(learning_rate)

print(f"Input Vector should be {neural_network.predict(input_vector)}\nAt {neural_network.bias} bias, \n{neural_network.weights} weight, \nAnd {neural_network.learning_rate} learning rate")