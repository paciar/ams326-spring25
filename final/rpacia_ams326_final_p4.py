# AMS326 - Numerical Analysis, Spring 2025
# Professor Yuefan Deng
# Final Exam, Problem F.4
# Ralf Pacia

import numpy as np
import matplotlib.pyplot as plt

# Euler's method for second order ODE
def euler_second_order(f, x0, y0, yp0, h, x_end):
    n_steps = int((x_end - x0) / h) + 1
    x = np.linspace(x0, x_end, n_steps)
    y = np.zeros(n_steps)
    yp = np.zeros(n_steps)

    y[0] = y0
    yp[0] = yp0

    for i in range(1, n_steps):
        y[i] = y[i-1] + h * yp[i-1]
        yp[i] = yp[i-1] + h * f(x[i-1], y[i-1])

    return x, y

# The differential equation y'' = -xy
def ode_func(x, y):
    return -x*y

# Shooting Method

def shoot(h, x0, x_end, ode_func):
    # IVP 1: y(0) = 1, y'(0) = 0
    x1, y1 = euler_second_order(ode_func, x0, y0=1, yp0=0, h=h, x_end=x_end)

    # IVP 2: y(0) = 1, y'(0) = 1
    x2, y2 = euler_second_order(ode_func, x0, y0=1, yp0=1, h=h, x_end=x_end)

    # Calculate shoot value
    y_b = 2         # We know y(b) = y_b --> y(2) = 2
    y1_b = y1[-1]   # Calculate y(2) from first IVP
    y2_b = y2[-1]   # Calculate y(2) from second IVP
    s = (y_b - y1_b) / (y2_b - y1_b)

    # Final solution
    y_final = y1 + s * (y2 - y1)

    print(f"x \t\t y(x)")
    for x, y in zip(x1, y_final):
        print(f"{x:.2f} \t\t {y:.3f}")

    # Plotting the results
    plt.figure(figsize=(8, 5))
    plt.plot(x1, y1, label="IVP 1: y'(0)=0", linestyle='--')
    plt.plot(x2, y2, label="IVP 2: y'(0)=1", linestyle='--')
    plt.plot(x1, y_final, label=f"Interpolated: s ≈ {s:.4f}", linewidth=2)
    plt.title("Linear Shooting Method for y'' = -xy, y(0)=1, y(2)=2")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

    return x1, y_final

# Step size and range
h = 0.01    # Given in problem
x0 = 0
x_end = 2   # For this question, we know y(0) = 1 and y(2) = 2

shoot(h, x0, x_end, ode_func)