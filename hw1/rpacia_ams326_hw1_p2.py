# AMS326 - Numerical Analysis, Spring 2025
# Professor Yuefan Deng
# Homework 1, Problem 1.2
# Ralf Pacia

import sys
import numpy as np

"""
L_k(x) -- calculates the Lagrange polynomial

Arguments:
    k:          calculating the k-th order Lagrange polynomial
    x:          calculating Lagrange polynomial at specific point x
    points:     set of given data points to be interpolated

Returns:
    Result of L_k(x) using provided k and x-values.
"""
def lagrange(k, x, points):
    # Accumulator variable set to 1, since we are accumulating terms through multiplication.
    lkx = 1
    # Keep track of how many valid terms have been printed, since asterisks are printed before the terms being accumulated.
    valid_terms = 0
    # Iterate over all points and accumulate the product of all (x - xi) / (xk - xi), where k is the order of the Lagrange polynomial, i is the iteration index, and n is the number of points.
    # Skip over iterations (i.e. do not accumulate the term) if i = k.
    n = len(points['x'])
    for i in range(n):
        if (i != k):
            # Print an asterisk before the accumulated term if it is not the first term. This ensures that asterisks are only printed between the terms being multiplied.
            if valid_terms > 0:
                print(" * ", end="")
            # Accumulating terms of the Lagrange polynomial.
            print(f"(t - {points['x'][i]})/({points['x'][k]} - {points['x'][i]})", end="")
            lkx *= (x - points['x'][i]) / (points['x'][k] - points['x'][i])
            # After a term has been accumulated, increment the number of valid terms.
            valid_terms += 1
    # After iterating over all points, the Lagrange polynomial has been calculated.
    return lkx

"""
Method 1 - Polynomial Interpolation (using Lagrange)

Arguments:
    n:          interpolating an n-th order polynomial
    x:          interpolating the data at point x=t
    points:     set of given data points to be interpolated

Returns:
    The interpolated data at point t using an n-th order polynomial.
"""
def poly(n, x, points):
    # Accumulator variable set to 0, since we are accumulating terms through summation.
    pnx = 0
    print(f"P_{n}(x) = ")
    # Iterate from 0 to n (the order of the polynomial being interpolated), inclusive.
    # Accumulate the sum of all y_i * L_i(x), where i is the order of the Lagrange polynomial to be calculated and x is the desired data point.
    for i in range(n+1):
        print(f"{points['y'][i]} * ", end="")
        pnx += points['y'][i] * lagrange(i, x, points)
        if (i != n):
            print(" + ")
    # After accumulating all terms, the data at point x has been computed using the interpolated polynomial of order n.
    print("\n")
    return pnx

"""
Method 2 - Quadratic Fit

Arguments:
    x:          interpolating the data at point x=t
    points:     set of given data points to be quadratically fitted

Returns:
    The interpolated data at point t using a quadratic fit.
"""
def quad(x, points):
    # We will need a 5x3 matrix since we have 5 x-values and 3 constants to solve for.
    matrix_A = np.zeros((5,3))
    matrix_c = np.zeros((3,1))
    # We will need a 5x1 matrix for the 5 y-values.
    matrix_b = np.zeros((5,1))
    # Populate A and b matrices.
    for i in range(len(points['x'])):
        matrix_A[i] = [points['x'][i]**0, points['x'][i]**1, points['x'][i]**2]
        matrix_b[i] = points['y'][i]
    # Now, we want to solve A^T * A * c = A^T * b for c
    matrix_c = np.linalg.solve(np.matmul(np.matrix.transpose(matrix_A), matrix_A), np.matmul(np.matrix.transpose(matrix_A), matrix_b))
    # We now have solved for c_1, c_2, and c_3.
    print(f"Q_2(t) = {matrix_c[0][0]} + {matrix_c[1][0]}t + {matrix_c[2][0]}t^2\n")
    return matrix_c[0][0] + (matrix_c[1][0] * x) + (matrix_c[2][0] * (x**2))
    

def main():
    # Given data points
    points = {
        'x': [1,2,3,4,5],
        'y': [412,407,397,398,417]
    }

    if (len(sys.argv) != 2):
        print("Usage: py rpacia_ams326_hw1_p2.py polynomial|quadratic")
        exit(1)
    elif(sys.argv[1] == "polynomial"):
        # (1) Interpolate the data in a polynomial P_4(t) and compute P_4(t=6) using your P_4(t)
        print("Polynomial interpolation:\n")
        print(f"P_4(t=6) = {poly(4,6,points)}")
    elif(sys.argv[1] == "quadratic"):
        # (1) Interpolate the data in a polynomial P_4(t) and compute P_4(t=6) using your P_4(t)
        print("Quadratic fit:\n")
        print(f"Q_2(t=6) = {quad(6,points)}")
    else:
        print("Usage: py rpacia_ams326_hw1_p2.py polynomial|quadratic")
        exit(1)

    exit(0)

if __name__ == '__main__':
    main()