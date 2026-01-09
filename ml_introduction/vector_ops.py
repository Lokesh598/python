import numpy as np



def dot_product_of_vectors(v1: np.ndarray, v2: np.ndarray) -> float:
    """Compute the dot product of two vectors."""
    if v1.shape != v2.shape:
        raise ValueError("Vectors must be of the same length.")

    return np.dot(v1, v2)
    
def magnitude_of_vector(v: np.ndarray) -> float:
    """Compute the magnitude of a vector. (magnitude is the length of the vector)"""
    return np.linalg.norm(v)


data_set1 = [1, 2, 3]
data_set2 = [4, 5, 6]

v1 = np.array(data_set1)
v2 = np.array(data_set2)

dot_product = dot_product_of_vectors(v1, v2)
magnitude = magnitude_of_vector(v1)

print("Dot Product:", dot_product)
print("Magnitude of v1:", magnitude)
