# AMS326 - Numerical Analysis, Spring 2025
# Professor Yuefan Deng
# Exam 1, Problem 1.1
# Ralf Pacia

import numpy as np

# NOTE: The code I have provided for poly were adapted from my HW1 submission.

"""
Least Squares Fit

Arguments:
    matrix_A:   matrix A in Ax = b
    matrix_b:   matrix b in Ax = b
    x:          interpolating the data at point x=t

Returns:
    The interpolated data at point t using a quadratic fit.
"""
def poly(matrix_A, matrix_b, x):
    matrix_c = np.zeros((4,1))
    # We want to solve A^T * A * c = A^T * b for c, which numpy conveniently has methods for.
    matrix_AT = np.matrix.transpose(matrix_A)
    matrix_ATA = np.matmul(matrix_AT, matrix_A)
    matrix_ATb = np.matmul(matrix_AT, matrix_b)
    matrix_c = np.linalg.solve(matrix_ATA, matrix_ATb)
    # We now have solved for c_1, c_2, and c_3.
    print(f"P_3(t) = {matrix_c[0][0]} + {matrix_c[1][0]}t + {matrix_c[2][0]}t^2\n")
    qx = matrix_c[0][0] + (matrix_c[1][0] * x) + (matrix_c[2][0] * (x**2)) + (matrix_c[3][0] * (x**3))
    return qx

def main():
    # Given data points. The x-coordinates were generated with a temporary for-loop I made.
    points = {
        "x": [16, 47, 78, 109, 140, 171, 202, 233, 264, 295, 326, 357],
        "y": [33, 34, 40, 51, 60, 69, 75, 74, 67, 56, 47, 38]
    }
    # We will need a 12x4 matrix since we have 12 x-values and 3 constants to solve for.
    matrix_A = np.zeros((12,4))
    # We will need a 12x1 matrix for the 12 y-values.
    matrix_b = np.zeros((12,1))
    # Populate A and b matrices.
    for i in range(len(points['x'])):
        matrix_A[i] = [points['x'][i]**0, points['x'][i]**1, points['x'][i]**2, points['x'][i]**3]
        matrix_b[i] = points['y'][i]
    print("Polynomial fit:\n")
    # June 4 = 4 + 31*5
    print(f"P_3(t=159) = {poly(matrix_A, matrix_b, 159)}")
    # Dec 25 = 25 + 31*11 = 366
    print(f"P_3(t=366) = {poly(matrix_A, matrix_b, 366)}")
    exit(0)

if __name__ == "__main__":
    main()