# AMS326 - Numerical Analysis, Spring 2025
# Professor Yuefan Deng
# Exam 2, Problem 2.1
# Ralf Pacia

import numpy as np
import scipy as sp

def rectangle(a, b, n, f):
    # Calculate step size (delta x) by dividing total interval over number of subintervals.
    dx = (b-a) / n
    # Accumulate all f(x_i) values in area.
    area = 0
    for i in range(n):
        # Midpoint of interval i can be calculated using a + dx * (interval index + 0.5)
        x_mid = a + (dx * (i + 0.5))
        f_mid = f(x_mid)
        area += f_mid
    # Multiply accumulated values by dx, as shown in my report.
    area *= dx
    return area

def simpson_one_third(a, b, n, f):
    # Step size
    h = (b - a) / n

    # Initialize result
    # f(a) is the first variable
    # f(b) is the last variable
    integral = f(a) + f(b)

    # Iterate from 1 to n-1 (middle elements)
    for i in range(1, n):
        # Calculate x-value from step size and interval index
        x = a + i * h
        # If index is even, we multiply by 2
        if i % 2 == 0:
            integral += 2 * f(x)
        # If index is odd, we multiply by 4
        else:
            integral += 4 * f(x)

    # Final total is multiplied by 1/3 * step size
    integral *= h / 3
    return integral

def simpson_three_eighth(a, b, n, f):
    # Step size
    h = (b - a) / n

    # Initialize result
    # f(a) is the first variable
    # f(b) is the last variable
    integral = f(a) + f(b)

    # Iterate from 1 to n-1 (middle elements)
    for i in range(1, n):
        x = a + i * h
        # If index is divisible by 3, multiply by 2
        if i % 3 == 0:
            integral += 2 * f(x)
        # Otherwise, multiply by 3
        else:
            integral += 3 * f(x)

    # Final total is multiplied by 3/8 * step size
    integral *= (3 * h) / 8
    return integral

def monte_carlo(a, b, n, f):
    # Generate points using uniform distribution
    x_pts = np.random.uniform(a, b, n)
    # Perform function on each point
    f_vals = f(x_pts)
    # Find mean of f(x_n) points (this divides the sum by n)
    avg = np.mean(f_vals)
    # Mutliply mean by (b-a)
    integral = avg * (b - a)
    return integral

def gauss_quad(a, b, n, f):
    # Get xi and ci values
    x, c = np.polynomial.legendre.leggauss(n)
    integral = 0
    # Sum ci * f(xi)
    for xi, ci in zip(x, c):
        integral += ci * f(xi)
    return integral

def f(x):
    return np.e**(x**5)

def main():
    known = 2.0949681713212

    # Midpoint
    rect = rectangle(-1, 1, 100, f)
    print(f"Midpoint method with n=100 subintervals: {rect}")
    print(f"Midpoint error (known - rect) is: {known - rect}\n")

    # Simpson 1/3
    simp_one_third = simpson_one_third(-1, 1, 101, f)
    print(f"Simpson 1/3 method with n=101 subintervals: {simp_one_third}")
    print(f"Simpson 1/3 error (known - simp_one_third) is: {known - simp_one_third}\n")

    # Simpson 3/8
    simp_three_eighth = simpson_three_eighth(-1, 1, 101, f)
    print(f"Simpson 3/8 method with n=101 subintervals: {simp_three_eighth}")
    print(f"Simpson 3/8 error (known - simp_three_eighth) is: {known - simp_three_eighth}\n")

    # Gaussian Quadrature
    gq = gauss_quad(-1, 1, 5, f)
    print(f"Gaussian quadrature method with n=5 points: {gq}")
    print(f"Gaussian quadrature error (known - gq) is: {known - gq}\n")

    # Monte Carlo
    mc = monte_carlo(-1, 1, 1000, f)
    print(f"Monte Carlo method with n=1000 points: {mc}")
    print(f"Monte Carlo error (known - mc) is: {known - mc}\n")

    exit(0)

if __name__ == "__main__":
    main()
