import yfinance as yf
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import numpy as np

# Download historical stock data (e.g., Apple)
ticker = 'AAPL'
data = yf.download(ticker, start='2020-01-01', end='2023-01-01')

# Use 'Close' price as target and create features
data['Prediction'] = data['Close'].shift(-1)  # Next day's closing price

# Drop last row with NaN target
data = data[:-1]

X = np.array(data[['Open', 'High', 'Low', 'Close', 'Volume']])
y = np.array(data['Prediction'])

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict and evaluate
predictions = model.predict(X_test)
mse = mean_squared_error(y_test, predictions)

print(f"Mean Squared Error: {mse}")

# Example prediction for the last available data day
print(f"Predicted next close price: {predictions[-1]}")
