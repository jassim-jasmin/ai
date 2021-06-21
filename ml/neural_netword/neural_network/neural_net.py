import numpy as np


class NN:
    @staticmethod
    def _sigmoid(x):
        return 1/(1 + np.exp(-x))

    @staticmethod
    def layer_1(input_vector, weights, bias):
        return np.dot(input_vector, weights) + bias

    @classmethod
    def layer_2(cls, layer_1):
        return cls._sigmoid(layer_1)

    @classmethod
    def predict(cls, input_vector, weights, bias):
        layer_1 = cls.layer_1(input_vector, weights, bias)
        layer_2 = cls.layer_2(layer_1)

        return layer_2

    @staticmethod
    def _d_mse(prediction, target):
        return 2 * (prediction - target)

    @classmethod
    def _sigmoid_deriv(cls, x):
        return cls._sigmoid(x) * (1 - cls._sigmoid(x))

    @classmethod
    def _compute_gradients(cls, input_vector, target, weights, bias):
        layer_1 = np.dot(input_vector, weights) + bias
        layer_2 = cls._sigmoid(layer_1)
        prediction = layer_2

        derror_dprediction = 2 * (prediction - target)
        dprediction_dlayer1 = cls._sigmoid_deriv(layer_1)
        dlayer1_dbias = 1
        dlayer1_dweights = (0 * weights) + (1 * input_vector)

        derror_dbias = (
                derror_dprediction * dprediction_dlayer1 * dlayer1_dbias
        )
        derror_dweights = (
                derror_dprediction * dprediction_dlayer1 * dlayer1_dweights
        )

        return derror_dbias, derror_dweights, weights, bias

    @staticmethod
    def _mse(prediction, target):
        return (prediction - target) ** 2

    @classmethod
    def learn(cls, input_vector, weights, bias, target):
        prediction = cls.predict(input_vector, weights, bias)
        mse = cls._mse(prediction, target)

        if round(mse) != 0:
            d_prediction_d_layer_1 = cls._sigmoid_deriv(cls.layer_1(input_vector, weights, bias))
            d_error = cls._d_mse(prediction, target)
            d_layer_1_bias = 1
            weights -= d_error


input_vector_1 = np.array([1.66, 1.56])
weights_1 = np.array([1.45, -0.66])
bias = np.array([0.0])

def sigmoid(x):
    return 1/(1 + np.exp(-x))


def make_prediction(input_vector, weights, bias):
    layer_1 = np.dot(input_vector, weights) + bias
    layer_2 = sigmoid(layer_1)

    return layer_2


def predict(input_vector, weights_1, bias, target):
    prediction = make_prediction(input_vector, weights_1, bias)
    mse = (prediction - target) ** 2

    print(f"Prediction: {prediction}, mse: {mse}, target: {target}")

    return prediction, mse


target_1 = 1
prediction, mse = predict(input_vector_1, weights_1, bias, target_1)
n_prediction = NN.predict(input_vector_1, weights_1, bias)
print(f"n prediction: {n_prediction}")

input_vector_2 = np.array([2, 1.5])
target_2 = 0

prediction, mse = predict(input_vector_2, weights_1, bias, target_2)

derivative = 2 * (prediction - target_2)

print(f"derivative: {derivative}")
weights_1 -= derivative

prediction, mse = predict(input_vector_2, weights_1, bias, target_2)

prediction, mse = predict(input_vector_1, weights_1, bias, target_1)

derivative = 2 * (prediction - target_1)

print(f"derivative: {derivative}")
weights_1 -= derivative

prediction, mse = predict(input_vector_1, weights_1, bias, target_1)


def _compute_gradients(self, input_vector, target):
    layer_1 = np.dot(input_vector, self.weights) + self.bias
    layer_2 = self._sigmoid(layer_1)
    prediction = layer_2

    derror_dprediction = 2 * (prediction - target)
    dprediction_dlayer1 = self._sigmoid_deriv(layer_1)
    dlayer1_dbias = 1
    dlayer1_dweights = (0 * self.weights) + (1 * input_vector)

    derror_dbias = (
            derror_dprediction * dprediction_dlayer1 * dlayer1_dbias
    )
    derror_dweights = (
            derror_dprediction * dprediction_dlayer1 * dlayer1_dweights
    )

    return derror_dbias, derror_dweights
