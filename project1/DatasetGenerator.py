#Juan Ramirez
#CS 2430
#Programming Project 1
"""
This file contains the dataset generator.
"""

import random

def make_array(size):
    numbers = []
    for i in range(size):
        numbers.append(random.randint(1, 100))
    return numbers

array4 = make_array(4)
array6 = make_array(6)
array8 = make_array(8)

print("Array of size 4:", array4)
print("Array of size 6:", array6)
print("Array of size 8:", array8)