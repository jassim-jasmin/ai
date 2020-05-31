from tensorflow.keras.datasets import mnist
import numpy as np
import cv2

import matplotlib.pyplot as plt

import tensorflow as tf
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

image_index = 0 # You may select anything up to 60,000
print(y_train[image_index]) # The label is 8
plt.imshow(x_train[image_index], cmap='Greys')
cv2.imshow("result", x_train[image_index])
cv2.waitKey(0)