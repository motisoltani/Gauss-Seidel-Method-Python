'''
Systems of Linear Algebraic Equations
Gauss–Seidel Method
language: Python

Motahare Soltani
soltani.wse@gmail.com

'''

import numpy as np
from scipy.linalg import solve

def gauss(A, b, x, n):
    L = np.tril(A)
    U = A - L
    for i in range(n):
        x = np.dot(np.linalg.inv(L), b - np.dot(U, x))
    return x

A = np.array([[4.0, -2.0, 1.0], [1.0, -3.0, 2.0], [-1.0, 2.0, 6.0]])
b = [1.0, 2.0, 3.0]
x = [1, 1, 1]
n = 20

print (gauss(A, b, x, n))
print( solve(A, b))