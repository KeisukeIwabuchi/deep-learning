import numpy as np

A = np.array([1, 2, 3, 4])

# print(A)
# print(np.ndim(A))
# print(A.shape)
# print(A.shape[0])


B = np.array([[1, 2], [3, 4], [5, 6]])

# print(B)
# print(np.ndim(B))
# print(B.shape)


# 行列の積
A = np.array([[1, 2], [3, 4]])
print(A.shape)

B = np.array([[5, 6], [7, 8]])
print(B.shape)

print(np.dot(A, B))