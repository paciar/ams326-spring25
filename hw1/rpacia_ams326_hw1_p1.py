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

"""
fun_prime(x) = (-3 * e^(-x^3) * x^2) - 4*(x^3) - cos(x)
fun(x) differentiated with respect to x

FLOP counting:
    As previously shown, e^(-x^3) will count as +9 FLOPS
    x^2: +1 FLOP
    4*(x^3): +3 FLOPS
    cos(x): +1 FLOP
    Multiplication/subtraction between "separate" terms: +4 FLOPS
    TOTAL: 18 FLOPS
"""
def fun_prime(x):
    return ((-3) * (np.exp(-(x**3))) * (x**2)) - (4*(x**3)) - np.cos(x)

"""
Method 2 - Newton's Method

Arguments:
    x0:         initial starting point
    f:          function
    f_flops:    function FLOPS (approximation)
    f_p:        derivative of f with respect to x
    f_p_flops:  derivative function FLOPS (approximation)
    tol:        tolerance level
    root:       known root

Returns:
    A tuple in the form of (calculated root, num of iterations, num of FLOPS).
"""
def newton(x0, f, f_flops, f_p, f_p_flops, tol, root):
    newton_iterations = 0
    newton_flops = 0
    # Initialize x_i to x_0.
    xi = x0
    while (True):
        # If the calculated root is within tolerance of the known root, break.
        if (abs(xi - root) < tol):
            # If this case is reached, +1 FLOP for calculating |c - root|.
            newton_flops += 1
            return xi, newton_iterations, newton_flops
        # Otherwise, calculate x_(i+1) and use it as x_i for the next iteration.
        else:
            # If this case is reached, +1 FLOP for calculating |c - root|.
            # +2 FLOPS for the subtraction and division.
            # +(f_flops) FLOPS for the call to f(xi) and +(f_p_flops) FLOPS for the call to f_p(xi).
            # Total: +(3 + f_flops + f_p_flops)
            newton_flops += (3 + f_flops + f_p_flops)
            xi_1 = xi - (f(xi) / f_p(xi))
            xi = xi_1
        newton_iterations += 1


def main():
    # Tolerance level, known root, and FLOPS of fun(x)
    tolerance = 0.5 * 10**(-4)
    r = 0.641583
    fun_flops = 14
    fun_p_flops = 18

    if (len(sys.argv) != 2):
       print("Usage: py rpacia_ams326_hw1_p1.py bisect|newton|secant|monte_carlo")
       exit(1)
    elif (sys.argv[1] == "bisect"):
       # Method 1: Use the bisection method with a given internal a_0 = −1 and b_0 = 1.
       bisect_root, bisect_iterations, bisect_flops = bisect(-1, 1, fun, fun_flops, tolerance, r)
       print(f"Bisection method: {bisect_root}")
       print(f"Bisection method number of iterations: {bisect_iterations}")
       print(f"Bisection method number of floating point operations (approximate): {bisect_flops}")
    elif (sys.argv[1] == "newton"):
       # Method 2: Use Newton’s method with the given initial root x_0 = 0.
       newton_root, newton_iterations, newton_flops = newton(0, fun, fun_flops, fun_prime, fun_p_flops, tolerance, r)
       print(f"Newton's method: {newton_root}")
       print(f"Newton's method number of iterations: {newton_iterations}")
       print(f"Newton's method number of floating point operations (approximate): {newton_flops}")
    else:
        print("Usage: py rpacia_ams326_hw1_p1.py bisect|newton|secant|monte_carlo")
        exit(1)

    exit(0)

if __name__ == '__main__':
    main()