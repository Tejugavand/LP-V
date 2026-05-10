import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, classification_report

df = pd.read_csv("IMDB Dataset.csv")
df.head()

df.shape

x = df['review']
y = df['sentiment']

vectorizer = TfidfVectorizer(max_features=5000)
x = vectorizer.fit_transform(x)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

model = MLPClassifier (hidden_layer_sizes=(128,64), activation='relu', max_iter=100, random_state=42)

model.fit(x_train, y_train)

MLPClassifier(hidden_layer_sizes=(128, 64), activation='relu', max_iter=100, random_state=42)

predictions = model.predict(x_test)

print("Predicted:", predictions[:10])
print("Actual:", y_test.values[:10])

accuracy = accuracy_score(y_test, predictions)

print("Accuracy", accuracy)
print("Classification Report:")
print(classification_report(y_test, predictions))