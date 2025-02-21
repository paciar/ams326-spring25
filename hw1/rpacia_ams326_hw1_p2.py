# AMS326 - Numerical Analysis, Spring 2025
# Professor Yuefan Deng
# Homework 1, Problem 1.2
# Ralf Pacia

import sys

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
    # Iterate over all points and accumulate the product of all (x - xi) / (xk - xi), where k is the order of the Lagrange polynomial and i is the iteration index.
    # Skip over iterations (i.e. do not accumulate the term) if i = k.
    for i in range(len(points['x'])):
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
    else:
        print("Usage: py rpacia_ams326_hw1_p2.py polynomial|quadratic")
        exit(1)

    exit(0)

if __name__ == '__main__':
    main()