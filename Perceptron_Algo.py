import numpy as np

class Perceptron:
    def __init__(self, num_features, learning_rate=0.01, num_epochs=100):
        self.num_features = num_features
        self.learning_rate = learning_rate
        self.num_epochs = num_epochs
        self.weights = np.zeros(num_features + 1)  # +1 for the bias term

    def predict(self, features):
        activation = np.dot(features, self.weights[1:]) + self.weights[0]
        return 1 if activation >= 0 else 0

    def train(self, features, labels):
        for _ in range(self.num_epochs):
            for x, y in zip(features, labels):
                prediction = self.predict(x)
                self.weights[1:] += self.learning_rate * (y - prediction) * x
                self.weights[0] += self.learning_rate * (y - prediction)

    def evaluate(self, features, labels):
        correct = 0
        for x, y in zip(features, labels):
            prediction = self.predict(x)
            if prediction == y:
                correct += 1
        accuracy = correct / len(labels)
        return accuracy

# Example usage:
# Assuming you have a dataset with multiple input features (X) and corresponding labels (y)
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])  # Example dataset with 2 input features
y = np.array([0, 0, 0, 1])

perceptron = Perceptron(num_features=2)  # Specify the number of input features
perceptron.train(X, y)

test_features = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
predictions = [perceptron.predict(x) for x in test_features]
print(predictions)  # Prints the predicted labels for the test features


"""
Output -

[0, 0, 0, 1]

"""