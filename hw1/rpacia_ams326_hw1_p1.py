# AMS326 - Numerical Analysis, Spring 2025
# Professor Yuefan Deng
# Homework 1, Problem 1.1
# Ralf Pacia

import numpy as np
import sys

"""
Method 1 - Bisection Method

Arguments:
    a0:         initial left bound
    b0:         initial right bound
    f:          function
    f_flops:    function FLOPS (approximation)
    tol:        tolerance level
    root:       known root

Returns:
    A tuple in the form of (calculated root, num of iterations, num of FLOPS).
"""
def bisect(a0, b0, f, f_flops, tol, root):
    bisect_iterations = 0
    bisect_flops = 0
    # Initialize search area to initial left/right bounds, [a0, b0].
    a = a0
    b = b0
    while ((b-a)/2 > tol):
        c = (a+b)/2
        # Every loop, +4 FLOPS for calculating (b-a)/2 and (a+b)/2.
        bisect_flops += 4
        # If the calculated root is within tolerance of the known root, break.
        if (abs(c - root) < tol):
            # If this case is reached, +1 FLOP for calculating |c - root|.
            bisect_flops += 1
            return c, bisect_iterations, bisect_flops
        # If f(a)*f(c) < 0, then the root must be in [a,c], so tighten right bound.
        elif (f(a)*f(c) < 0):
            # If this case is reached, +1 FLOP for calculating |c - root| and +(2*f_flops) FLOPS for calculating f(a) and f(c).
            bisect_flops += (1 + (2*f_flops))
            b = c
        # Otherwise, the root must be in [c,b]. so tighten left bound.
        else:
            # If this case is reached, similarly, +(1 + 2*f_flops) FLOPS for performing the calculations.
            bisect_flops += (1 + (2*f_flops))
            a = c
        # Every loop iteration, increment the iteration counter.
        bisect_iterations += 1

"""
fun(x) = e^(-x^3) - x^4 - sin(x)
For calculating FLOPS, I assume that Python uses exponentiation by squaring (optimized exponentiaion method).

FLOP counting:
    I approximated e^x to be +7 FLOPS, assuming we use Taylor series approximation of e^x with the first 4 terms.
    -x^3: +2 FLOPS
    x^4: +2 FLOPS
    sin(x): +1 FLOP
    Subtraction between all terms: +2 FLOPS
    TOTAL: 14 FLOPS

Arguments:
    x:  input x-variable

Returns:
    Result of f(x) using provided x-value.
"""
def fun(x):
    return np.exp(-(x**3)) - (x**4) - np.sin(x)

def main():
    # Tolerance level, known root, and FLOPS of fun(x)
    tolerance = 0.5 * 10**(-4)
    r = 0.641583
    fun_flops = 14

    if (len(sys.argv) != 2):
       print("Usage: py rpacia_ams326_hw1_p1.py bisect|newton|secant|monte_carlo")
       exit(1)
    elif (sys.argv[1] == "bisect"):
       # Method 1: Use the bisection method with a given internal a_0 = −1 and b_0 = 1.
       bisect_root, bisect_iterations, bisect_flops = bisect(-1, 1, fun, fun_flops, tolerance, r)
       print(f"Bisection method: {bisect_root}")
       print(f"Bisection method number of iterations: {bisect_iterations}")
       print(f"Bisection method number of floating point operations (approximate): {bisect_flops}")
    else:
        print("Usage: py rpacia_ams326_hw1_p1.py bisect|newton|secant|monte_carlo")
        exit(1)

    exit(0)

if __name__ == '__main__':
    main()