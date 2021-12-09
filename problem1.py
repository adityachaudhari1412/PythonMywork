#Aditya Chaudhari
import numpy as np

# part a)
def cos_sim(u, v):
    return np.dot(u, v) / (np.linalg.norm(u) * np.linalg.norm(v))

# part b)
u = np.array([3, -1, 4])
v = np.array([-2, 3, 1])
print(cos_sim(u, v))

u = np.array([5, 6, -5])
v = np.array([6, 2, -5])
print(cos_sim(u, v))

u = np.array([-3, 1, 7])
v = np.array([7, -4, 7])
print(cos_sim(u, v))


