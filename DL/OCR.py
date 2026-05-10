import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, classification_report

df = pd.read_csv("letter-recognition.csv")
df.head()

df.shape

y = df.iloc[:,0]
x = df.iloc[:,1:]

X = x.apply(pd.to_numeric)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
scaler = StandardScaler()

x_train_scaled = scaler.fit_transform(x_train)
x_test_scaled = scaler.transform(x_test)
model = MLPClassifier(hidden_layer_sizes=(128, 64), activation='relu', solver='adam', max_iter=300, random_state=42)
model.fit(x_train, y_train)

MLPClassifier(hidden_layer_sizes=(128, 64), activation='relu', solver='adam', max_iter=300, random_state=42)

predictions = model.predict(x_test)

print("Predicted:", predictions[:10])
print("Actual:", y_test.values[:10])

accuracy = accuracy_score(y_test, predictions)

print("Accuracy:", accuracy)
print("Classification Report:\n")
print(classification_report(y_test, predictions))