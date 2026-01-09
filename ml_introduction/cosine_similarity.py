
import numpy as np


def cosine_similarity(v1: np.ndarray, v2: np.ndarray) -> float:    
    """Compute the cosine similarity between two vectors."""
    if v1.shape != v2.shape:
        raise ValueError("Vectors must be of the same length.")

    dot_product = np.dot(v1, v2)
    magnitude_v1 = np.linalg.norm(v1)
    magnitude_v2 = np.linalg.norm(v2)

    if magnitude_v1 == 0 or magnitude_v2 == 0:
        raise ValueError("One or both vectors have zero magnitude.")

    return dot_product / (magnitude_v1 * magnitude_v2)


data_set1 = [1, 2, 3]
data_set2 = [4, 5, 6]

v1 = np.array(data_set1)
v2 = np.array(data_set2)


similarity = cosine_similarity(v1, v2)

print("Cosine Similarity:", similarity)

