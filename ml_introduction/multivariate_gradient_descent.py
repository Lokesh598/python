import numpy as np


"""Task 5. Implementation of Gradient Descent for Multivariate Linear Regression."""

def mutltivariate_gradient_descent(x : np.ndarray, y : np.ndarray, w : np.ndarray, learning_rate : float, iterations : int) -> tuple[np.ndarray, float]:
    for _ in range(iterations):
        predict = x @ w
        error = predict - y
        # final_loss = np.mean((predict - y)**2)
        gradient = (2/len(y)) * (x.T@error)
        w = w - learning_rate * gradient

    return w, np.mean(error**2)



x = np.array([
  [1, 1],
  [2, 2],
  [3, 3],
  [4, 4]
])

y = np.array([2, 4, 6, 8])

final_weight, error = mutltivariate_gradient_descent(x, y, w = np.array([0, 0]), learning_rate=0.01, iterations=1000)


print("Optimized Weights (w):", final_weight) # should be close to [1,1]
print("Final Loss:", error) # close to 0 indicates good fit