#Aditya Chaudhari
import numpy as np
import matplotlib.pyplot as plt

def plot_L1_vs_L2():
    x = np.linspace(-3, 3, 100)
    l1 = abs(x)
    l2 = x**2
    fig, ax = plt.subplots()
    ax.plot(x, l1)
    ax.plot(x, l2)
    ax.axhline(y=0, color='k')
    ax.axvline(x=0, color='k')
    plt.show()

# a
plot_L1_vs_L2()

# b
def compute_L1_and_L2(u, v):
    x = u - v
    return sum(abs(x)), sum(x**2)

u = np.random.rand(4)
v = np.random.rand(4)
l1, l2 = compute_L1_and_L2(u, v)

print(f'u = {u}')
print(f'v = {v}')
print(f'L1(u, v) = {l1}')
print(f'L2(u, v) = {l2}')
