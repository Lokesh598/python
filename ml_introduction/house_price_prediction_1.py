
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Ridge
import numpy as np



"""Task 7. House Price Prediction using Ridge Regression with Pipeline."""


x = np.array([[1000, 2],
  [1500, 3],
  [2000, 4],
  [2500, 4],
  [3000, 5]])

y = np.array([50, 75, 100, 130, 160])


pipeline = Pipeline([ 
    ("scaler", StandardScaler()), # feature scaling = standardscaler
    ("model", Ridge(alpha=1.0)) # Ridge Regression model
])

pipeline.fit(x, y)

y_pred = pipeline.predict(x)

mse = np.mean((y - y_pred) ** 2)  # Mean Squared Error (Evaluation Metric or evaluate)
print("Predicted House Prices with Ridge Regression:", y_pred)
print("Mean Squared Error with Ridge Regression:", mse)
print("Model Coefficients with Ridge Regression:", pipeline.named_steps["model"].coef_)
print("Model Intercept with Ridge Regression:", pipeline.named_steps["model"].intercept_)
# The output will show the predicted house prices for the dataset,