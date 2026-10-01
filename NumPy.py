import numpy as np

# 1. Write a Python program using NumPy to create a one-dimensional array containing 10 integers and display the array, its size, data type, and number of dimensions.
arr1 = np.arange(10)
print(arr1)
print(arr1.size)
print(arr1.dtype)
print(arr1.ndim)

#2. Create two NumPy arrays of 5 integers each. Perform and display: Addition, Subtraction, Multiplication, Division, Modulus
a = np.array([10, 20, 30, 40, 50])
b = np.array([2, 4, 6, 8, 10])
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)

# 3. Create a NumPy array containing 10 numbers. Find and display the maximum, minimum, sum, and average of the elements.
arr3 = np.array([12, 45, 7, 89, 23, 56, 3, 67, 34, 90])
print(np.max(arr3))
print(np.min(arr3))
print(np.sum(arr3))
print(np.mean(arr3))

# 4. Create a NumPy array of integers from 1 to 20. Use Boolean indexing to separate and display the even and odd numbers.
arr4 = np.arange(1, 21)
evens = arr4[arr4 % 2 == 0]
odds = arr4[arr4 % 2 != 0]
print(evens)
print(odds)

# 5. Create a one-dimensional array containing numbers from 1 to 12. Reshape it into: 2 x 6 matrix, 3 x 4 matrix, 4 x 3 matrix
arr5 = np.arange(1, 13)
print(arr5.reshape(2, 6))
print(arr5.reshape(3, 4))
print(arr5.reshape(4, 3))

# 6. Create two 3 x 3 NumPy matrices and perform matrix addition.
m1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
m2 = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
print(m1 + m2)

# 7. Create two compatible matrices using NumPy and perform matrix multiplication using an appropriate NumPy function.
mat_a = np.array([[1, 2], [3, 4], [5, 6]])
mat_b = np.array([[7, 8, 9], [10, 11, 12]])
print(np.matmul(mat_a, mat_b))

# 8. Create a 3 x 4 matrix and display its transpose.
arr8 = np.arange(12).reshape(3, 4)
print(arr8.T)

# 9. Create a 4 x 4 NumPy array and write a program to: Display the first row, Display the last column, Display the diagonal elements, Display the elements from the second and third rows
arr9 = np.arange(16).reshape(4, 4)
print(arr9[0, :])
print(arr9[:, -1])
print(np.diagonal(arr9))
print(arr9[1:3, :])

# 10. Create a 4 x 4 matrix and calculate the sum of each row and each column separately.
arr10 = np.arange(16).reshape(4, 4)
print(np.sum(arr10, axis=1))
print(np.sum(arr10, axis=0))

# 11. Create a NumPy array containing numbers from 1 to 20. Using slicing, display: First 5 elements, Last 5 elements, Alternate elements, Elements in reverse order
arr11 = np.arange(1, 21)
print(arr11[:5])
print(arr11[-5:])
print(arr11[::2])
print(arr11[::-1])

# 12. Create an array of 10 integers. Replace all elements greater than 50 with 0 using NumPy Boolean indexing.
arr12 = np.array([15, 62, 45, 88, 30, 95, 50, 12, 73, 40])
arr12[arr12 > 50] = 0
print(arr12)

# 13. Create an unsorted NumPy array and display it in: Ascending order, Descending order
arr13 = np.array([42, 15, 8, 99, 23, 74])
print(np.sort(arr13))
print(np.sort(arr13)[::-1])

# 14. Create an array containing duplicate values. Find and display only the unique elements.
arr14 = np.array([1, 2, 2, 3, 4, 4, 4, 5, 1, 6])
print(np.unique(arr14))

# 15. Create two NumPy arrays and concatenate them horizontally and vertically.
arr15_a = np.array([[1, 2], [3, 4]])
arr15_b = np.array([[5, 6], [7, 8]])
print(np.hstack((arr15_a, arr15_b)))
print(np.vstack((arr15_a, arr15_b)))

# 16. Store marks of 10 students in a NumPy array. Calculate: Highest marks, Lowest marks, Average marks, Median, Standard deviation
marks = np.array([78, 85, 92, 64, 88, 73, 95, 81, 69, 90])
print(np.max(marks))
print(np.min(marks))
print(np.mean(marks))
print(np.median(marks))
print(np.std(marks))

# 17. Take marks of 20 students, calculate the class average and display the marks of students who scored above the average.
marks20 = np.array([55, 78, 82, 60, 91, 45, 88, 72, 67, 95, 81, 59, 74, 85, 90, 68, 77, 83, 62, 89])
avg = np.mean(marks20)
print(avg)
print(marks20[marks20 > avg])

# 18. Write a Python program using NumPy to create a 3D array of shape (2, 3, 4) containing numbers from 1 to 24. Display the array and its: Number of dimensions, Shape, Size
arr18 = np.arange(1, 25).reshape(2, 3, 4)
print(arr18)
print(arr18.ndim)
print(arr18.shape)
print(arr18.size)

# 19. Create a 3D array of shape (2, 3, 4) and write a program to access: First element, Last element, Element at index [0,1,2], Element at index [1,2,3]
arr19 = np.arange(24).reshape(2, 3, 4)
print(arr19[0, 0, 0])
print(arr19[-1, -1, -1])
print(arr19[0, 1, 2])
print(arr19[1, 2, 3])

# 20. Create a (2, 3, 4) array and calculate: Sum of all elements, Sum of each layer, Sum along rows, Sum along columns
arr20 = np.arange(24).reshape(2, 3, 4)
print(np.sum(arr20))
print(np.sum(arr20, axis=(1, 2)))
print(np.sum(arr20, axis=2))
print(np.sum(arr20, axis=1))

# 21. Create a 3D array of random integers between 1 and 100. Replace all values greater than 50 with 0
arr21 = np.random.randint(1, 101, size=(2, 3, 4))
arr21[arr21 > 50] = 0
print(arr21)

# 22. Generate a random 3D array of shape (3, 4, 5) and calculate its: mean, median, standard deviation, variance, minimum, and maximum.
arr22 = np.random.rand(3, 4, 5)
print(np.mean(arr22))
print(np.median(arr22))
print(np.std(arr22))
print(np.var(arr22))
print(np.min(arr22))
print(np.max(arr22))

# 23. Create a 3D NumPy array of shape (2, 3, 4) containing numbers from 1 to 24. Flatten the array into a one-dimensional array and display both the original and flattened arrays.
arr23 = np.arange(1, 25).reshape(2, 3, 4)
flat23 = arr23.flatten()
print(arr23)
print(flat23)

# 24. Create a 3D array containing integers from 1 to 27. Flatten the array and calculate: Sum, Average, Maximum, Minimum
arr24 = np.arange(1, 28).reshape(3, 3, 3)
flat24 = arr24.flatten()
print(np.sum(flat24))
print(np.mean(flat24))
print(np.max(flat24))
print(np.min(flat24))

# 25. Create a random 3D NumPy array of shape (3, 4, 5). Flatten it and display only the elements that are: Greater than 50, Even numbers, Less than the average value
arr25 = np.random.randint(1, 101, size=(3, 4, 5))
flat25 = arr25.flatten()
print(flat25[flat25 > 50])
print(flat25[flat25 % 2 == 0])
print(flat25[flat25 < np.mean(flat25)])