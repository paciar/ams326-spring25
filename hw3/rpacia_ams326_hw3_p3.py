# AMS326 - Numerical Analysis, Spring 2025
# Professor Yuefan Deng
# Homework 3, Problem 3.3
# Ralf Pacia

import numpy as np
import matplotlib.pyplot as plt

def f(x, y):
    w = 44
    v0 = 88
    k = w / v0
    return y/x - k * np.sqrt(1 + (y/x)**2)

# Using Forward Euler method to solve ODE
def euler(x0, y0, h, f):
    # Store initial (x0, y0) in coordinate list
    x_vals = np.array([])
    y_vals = np.array([])
    x_vals = np.append(x_vals, x0)
    y_vals = np.append(y_vals, y0)
    x = x0
    y = y0
    # Move from (100, 0), the starting point, to (0, 0), the airport
    while x >= 0:
        xn = x
        yn = y
        x += h
        # y_(n+1) = y_n + h * f(xn, yn)
        y += h * f(xn, yn)
        x_vals = np.append(x_vals, x)
        y_vals = np.append(y_vals, y)
    return x_vals, y_vals

def main():
    x0 = 100
    y0 = 0
    # Since we are starting at (100, 0), we want to move towards (0, 0)
    h = -0.0005
    x_vals, y_vals = euler(x0, y0, h, f)
    plt.plot(x_vals, y_vals, label='Trajectory of plane')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Trajectory of plane - Forward Euler')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
