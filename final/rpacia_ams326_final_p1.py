# AMS326 - Numerical Analysis, Spring 2025
# Professor Yuefan Deng
# Final Exam, Problem F.1
# Ralf Pacia

import numpy as np

# Given root and sample size
given = 4.028423
n = 10**6

'''
Implementation 1: uniform distribution

Arguments
    - ax: lower x bound
    - bx: upper x bound
    - ay: lower y bound
    - by: upper y bound
    - n: number of samples
    - f: function to integrate

For this problem, we are integrating e**(x**6 - y**4), over x = [-1, 1] and y = [-1, 1]

Our samples are uniformly distributed.
'''
def monte_carlo_uniform(ax, bx, ay, by, n, f):
    # Generate n random x and y values uniformly
    x = np.random.uniform(ax, bx, n)
    y = np.random.uniform(ay, by, n)
    # Evaluate the function at all (x, y) pairs
    f_vals = f(x, y)
    # Average of function values
    avg = np.mean(f_vals)
    # Multiply by the area of the rectangle
    area = (bx - ax) * (by - ay)
    return avg * area

def u(x, y):
    return np.exp(x**6 - y**4)

uniform = monte_carlo_uniform(-1, 1, -1, 1, n, u)
print(f"Implementation # 1: \t\t N = {n} \t\t My Integral = {uniform} \t\t My error = {abs(uniform - given):.6f}")


'''
Implementation 2: samples drawn randomly with density proportional to the gradient magnitude of u(x,y)

Step 1: The gradient magnitude is first calculated.
Step 2: The normalizer is computed by generating n random points in the [-1,1]x[-1,1] domain, applying the gradient magnitude function to the random points, then multiplying the mean of the grad_mag(x,y) points by the area of the sampling domain. The estimated max value is computed by returning the max of the grad_mag(x,y) points.
Step 3: We generate n accepted points, where the criteria of accepting is by generating a random (x,y) point in the given range, applying grad_mag(x,y), then generating a random value between 0 and the estimated max. If the random value is less than the calculated grad_mag(x,y) value, then we accept the randomly generated (x,y) point. Essentially, we are accepting the sample point in proportion to the gradient magnitude.
Step 4: Over each accepted point (x,y), we calculate "weights" using the normalizer F, u(x,y), and grad_mag(x, y). The mean of these weights is then returned as the estimated integral.
'''

# Gradient magnitude of u(x,y)
def grad_mag(x, y):
    u = np.exp(x**6 - y**4)
    return u * np.sqrt(36 * x**10 + 16 * y**6)

# Compute PDF normalizer and estimated max value
def compute_normalizer_and_M(n):
    x = np.random.uniform(-1, 1, n)
    y = np.random.uniform(-1, 1, n)
    vals = grad_mag(x, y)
    area = 4  # area of [-1,1] x [-1,1]
    return area * np.mean(vals), np.max(vals)

# Sample accepted points
def sample_gradient_importance(n, M, F):
    # Generate n accepted sample points
    accepted = []
    while len(accepted) < n:
        x = np.random.uniform(-1, 1)
        y = np.random.uniform(-1, 1)
        gx = grad_mag(x, y)             # Compute gradient magnitude of generated point
        r = np.random.uniform(0, M)     # Generate sample between 0 and the estimated max
        # Accept if the randomly generated point is less than the gradient magnitude
        if r < gx:
            accepted.append((x, y))
    return np.array(accepted)

# Monte Carlo estimate of integral using accepted points
def monte_carlo_density(n):
    F, M = compute_normalizer_and_M(n)
    samples = sample_gradient_importance(n, M, F)
    x, y = samples[:,0], samples[:,1]
    weights = F * u(x, y) / grad_mag(x, y)
    return np.mean(weights)

density = monte_carlo_density(n)
print(f"Implementation # 2: \t\t N = {n} \t\t My Integral = {density} \t\t My error = {abs(density - given):.6f}")