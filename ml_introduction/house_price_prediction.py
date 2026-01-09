import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error


"""Task 6. House Price Prediction using Linear Regression."""



x = np.array([[1000, 2],
  [1500, 3],
  [2000, 4],
  [2500, 4],
  [3000, 5]])

y = np.array([50, 75, 100, 130, 160])


# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)


model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred) # Mean Squared Error (Evaluation Metric or evaluate)
print("Predicted House Prices:", y_pred)
print("Mean Squared Error:", mse)
print("Model Coefficients:", model.coef_)
print("Model Intercept:", model.intercept_)
# The output will show the predicted house prices for the test set,
# the mean squared error of the predictions, and the coefficients of the linear regression model.