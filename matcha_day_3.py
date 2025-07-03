import numpy as np
"""
S
Block 1: Array Creation, Indexing & Arithmetic
Focus: Creating arrays, indexing, slicing, vectorized ops

 1  Create a 1D array of integers 5 to 15
 2  Create a 2D array with shape (4, 5) using arange
 3  Extract row 2, column 3
 4  Replace all even numbers with -1 using slicing
 5  Add 5 to all values in a 2D array
 6  Multiply one array by another element-wise
 7  Square each element using vectorized ops
 8  Reshape a 1D array into 3x4
 9  Reverse a 1D array
 10  Get sum, mean, min, max of a random array
"""
arr1 = np.arange(5,16)

arr2 = np.arange(20).reshape(4,5)

element3 = arr2[2,3]

arr2[arr2 % 2 == 0] = -1

arr5 = np.arange(2,10).reshape(2,4)
arr5 += 5

arr6_1 = np.array([2,34,5])
arr6_2 = np.array([5,6,0])
arr6_multiply = arr6_1 * arr6_2

arr7 = np.arange(4,10).reshape(2,3)
arr7 = arr7 ** 2
#arr7 = np.square(arr7)

arr8 = np.arange(12).reshape(3,4)

arr9 = np.arange(4,10)
reversed_arr9 = arr9[::-1]

arr10 = np.arange(12).reshape(3,4)
arr10_min = np.min(arr10)
arr10_max = np.max(arr10)
arr10_sum = np.sum(arr10)
arr10_sum = np.mean(arr10)



