import numpy as np
"""
x = [1,1,1]
biases = [2,3,4]
weights = [10,100,1000]

a = np.dot(biases,weights)

print(a)

"""

biases = np.array([2, 3, 4])
weights = np.array([10, 100, 1000])

# Compute the dot product
a = biases*weights

print(a)