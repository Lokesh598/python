
"""This module demonstrates simple mathematical operations on a list of numbers."""

no_list = [1, 2, 6, 4, 5, 3]

def math(no_list : list) : 
    if len(no_list) == 0:
        return 0
    mean = sum(no_list) / len(no_list)

    max_val = max(no_list)

    min_val = min(no_list)

    sorted_list = sorted(no_list)

    print("Mean:", mean)
    print("Max:", max_val)
    print("Min:", min_val)
    print("Sorted List:", sorted_list)
math(no_list)


#  more professional way

from typing import List, Dict

def compute_statistics(numbers: List[float]) -> Dict[str, float]:
    """Compute mean, max, min, and sorted list of numbers."""
    if not numbers:
        raise ValueError("The list of numbers is empty.")

    mean = sum(numbers) / len(numbers)
    max_val = max(numbers)
    min_val = min(numbers)
    sorted_list = sorted(numbers)

    return {
        "mean": mean,
        "max": max_val,
        "min": min_val,
        "sorted_list": sorted_list
    }

data = [1, 2, 6, 4, 5, 3]
stats = compute_statistics(data)

print(stats)