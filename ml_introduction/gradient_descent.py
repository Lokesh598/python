import numpy as np

""""Task 4. Simple implementation of Gradient Descent for Linear Regression."""


def gradient_descent(x : np.ndarray, y : np.ndarray, w : float, learning_rate : float, iterations : int) -> tuple[float, float]:
    for _ in range(iterations):
        predict = w * x    
        final_loss = np.mean((predict - y)**2)
        gradient = (2/len(x)) * np.sum(x * (w*x - y))
        w = w - learning_rate * gradient

    return w, final_loss


data_set1 = [1, 2, 3, 4]
data_set2 = [2, 4, 6, 8]

x = np.array(data_set1) # vector 1
y = np.array(data_set2) # vector 2


w, final_loss = gradient_descent(x, y, w = 0, learning_rate=0.01, iterations=1000)

print("Optimized Weight (w):", w) # should be close to 2
print("Final Loss:", final_loss) # close to 0 indicates good fit






