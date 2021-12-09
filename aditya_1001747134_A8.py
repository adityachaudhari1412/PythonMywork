import numpy as mp
import sympy
import scipy.linalg as linalg

# a)  3x3 and 3x1 matrix given 
M = mp.array([
    [-7, 0, -3],
    [7, -1, 0],
    [5, -1, 0] ])
M_sp = sympy.Matrix(M) # Converting the numpy array to the sympy.Matrix class and performing rref
M_rref = M_sp.rref()
M_rref = mp.array(M_rref[0].tolist()) # Converting M_rref to numpy
print('a) Reduced row echelon form for M =\n', M_rref)

# b) column space of M
M_col = M_sp.columnspace(M)
print('b) M =\n', M_col)

# c) Solve Ax=b
b = mp.array([
    [-10],
    [5],
    [3] ])
eq = linalg.solve(M, b)
print('c) solved matrix vector\n', eq)
print('A@eq =\n', A@eq)

# d) null space of M
nullM = linalg.null_space(M)
print('d) Nul M\n', nullM)