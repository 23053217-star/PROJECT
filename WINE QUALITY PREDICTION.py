from sklearn.ensemble import RandomForestClassifier
import numpy as np

# Example wine features (fixed values, replace with real data for better results)
# Features: fixed acidity, volatile acidity, citric acid, residual sugar, chlorides, etc.
X = np.array([
    [7.4, 0.70, 0.00, 1.9, 0.076, 11, 34, 0.9978, 3.51, 0.56, 9.4],
    [7.8, 0.88, 0.00, 2.6, 0.098, 25, 67, 0.9968, 3.20, 0.68, 9.8],
    [7.8, 0.76, 0.04, 2.3, 0.092, 15, 54, 0.9970, 3.26, 0.65, 9.8],
    [11.2, 0.28, 0.56, 1.9, 0.075, 17, 60, 0.9980, 3.16, 0.58, 9.8]
])

# Corresponding quality labels (1 to 10 scale)
y = np.array([5, 5, 4, 6])

# Train random forest model
model = RandomForestClassifier()
model.fit(X, y)

# Predict quality of a new wine sample
new_sample = np.array([[7.0, 0.6, 0.0, 2.0, 0.07, 20, 40, 0.9965, 3.3, 0.5, 10.0]])
predicted_quality = model.predict(new_sample)

print(f"Predicted wine quality: {predicted_quality[0]}")
