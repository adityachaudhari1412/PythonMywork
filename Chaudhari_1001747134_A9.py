import numpy as np
import scipy.linalg as linalg

#  B and C matrix
x1 = np.array([[-3],[6],[2]])
x2 = np.array([[1],[8],[-4]])
x3 = np.array([[5],[5],[-2]])

y1 = np.array([[1],[-8],[-8]])
y2 = np.array([[1],[5],[8]])
y3 = np.array([[-7],[1],[-1]])

x = np.hstack((b1,b2,b3))
y = np.hstack((c1,c2,c3))

x_inverse = linalg.inv(b)
y_inverse = linalg.inv(c)

print("\n")
# basis change from B to C
print(y_inverse.dot(x))
print("\n")

# change of basis from C to B
print(x_inverse.dot(y))