#Aditya Chaudhari
import numpy as np

u = np.array([5, 1, 4, -2])
v = np.array([0, 5, 4, 5])



def projection(u, v):
    return (np.dot(u, v) / np.dot(v, v)) * v

print(projection(u, v))
