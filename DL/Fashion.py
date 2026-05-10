import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import matplotlib.pyplot as plt
import numpy as np

(X_train, y_train), (X_test, y_test) = 
keras.datasets.fashion_mnist.load_data()

print('Training data shape:', X_train.shape)
print('Test data shape:', X_test.shape)

X_train = X_train / 255.0
X_test = X_test / 255.0

X_train = X_train.reshape(-1,28,28,1)
X_test = X_test.reshape(-1,28,28,1)

model = keras.Sequential([
    layers.Conv2D(32,(3,3),activation='relu',input_shape=(28,28,1)),
    layers.MaxPooling2D((2,2)),
    layers.Conv2D(64,(3,3),activation='relu'),
    layers.MaxPooling2D((2,2)),
    layers.Flatten(),
    layers.Dense(128,activation='relu'),
    layers.Dense(10,activation='softmax')
])

model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

history = model.fit(
    X_train, y_train,
    epochs=5,
    validation_data=(X_test,y_test)
)

test_loss, test_acc = model.evaluate(X_test,y_test)
print('Test Accuracy:', test_acc)

predictions = model.predict(X_test)

print('Predicted class:', np.argmax(prediction[0]))
print('Actual class:', y_test[0])