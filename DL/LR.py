import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import mean_squared_error

df = pd.read_csv("HousingData.csv")
df.head()

df.fillna(df.mean(), inplace=True)

x = df.drop('MEDV', axis=1)
y = df['MEDV']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

scaler = StandardScaler()

x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)
model = MLPRegressor (hidden_layer_sizes=(64,32), activation='relu', max_iter=500, random_state=42)
model.fit(x_train, y_train)
MLPRegressor (hidden_layer_sizes=(64,32), activation='relu', max_iter=500, random_state=42)

predictions = model.predict(x_test)

print("Predicted Price:", predictions[0])
print("Actual Price:", y_test.iloc[0])

MSE = mean_squared_error(y_test, predictions)
print("Mean Squared Error:", MSE)