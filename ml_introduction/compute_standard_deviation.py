import numpy as np
from typing import Dict, Any


def compute_standard_deviation(numbers: np.ndarray) -> Dict[str, float]:
    """Compute mean, standard deviation using NumPy."""
    if numbers.size == 0:
        raise ValueError("The array is empty.")

    mean = numbers.mean()
    standard_deviation = numbers.std()

    return {
        "mean": mean,
        "standard_deviation": standard_deviation
    }


def transform_and_filter (numbers:np.ndarray) -> np.ndarray:
    """Filter numbers greater than 3 after multiplying by 2."""
    new_numbers = np.multiply(numbers, 2)
    
    filtered_numbers = new_numbers[new_numbers > 3]
    return filtered_numbers


data = [1, 2, 6, 4, 5, 3]

numbers = np.array(data) # numpy array from list

stats = compute_standard_deviation(numbers)
filtered = transform_and_filter(numbers)
print("Statistics: ", stats)
print("Filtered: ",filtered)