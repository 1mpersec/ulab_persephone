#File: even_sum.py
import numpy as np

def even_sum(numbers):
    """
    Return the sum of all even numbers in array
    """
    sum= np.sum(num for num in numbers if num % 2 == 0)
    return sum

