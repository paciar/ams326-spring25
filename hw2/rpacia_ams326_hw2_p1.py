# AMS326 - Numerical Analysis, Spring 2025
# Professor Yuefan Deng
# Homework 2, Problem 2.1
# Ralf Pacia

import numpy as np
import sys

"""
Method 1 - Rectangle Method

Arguments:
    theta_min:      lower integration bound
    theta_max:      upper integration bound
    n:              number of subintervals
    r:              polar function to be integrated

Returns:
    The area bounded by the function r(theta) over the interval [theta_min, theta_max] using the rectangle method and n subintervals.
    For the purposes of the given question, this uses the polar form of an equation, r(theta).

Acknowledgements:
    I used ChatGPT-4o to partially generate this program and consult it for further polishing.
"""
def rectangle(theta_min, theta_max, n, r):
    # print("Inside rectangle method...")
    # Calculate step size (delta theta) by dividing total interval over number of subintervals.
    delta_theta = (theta_max - theta_min) / n
    # Accumulate all r(theta_i*)^2 values in area.
    area = 0
    for i in range(n):
        # Midpoint of interval i can be calculated using theta_min + delta_theta * (interval index + 0.5)
        theta_mid = theta_min + (delta_theta * (i + 0.5))
        r_mid = r(theta_mid)
        area += r_mid**2
    # Multiply accumulated values by 1/2 * delta theta, as shown in my report.
    area *= 0.5 * delta_theta
    # Area = 1/2 * \int_{theta_min}^{theta_max} r^2 d\theta
    return area

"""
Method 2 - Trapezoid Method

Arguments:
    theta_min:      lower integration bound
    theta_max:      upper integration bound
    n:              number of subintervals
    r:              polar function to be integrated

Returns:
    The area bounded by the function r(theta) over the interval [theta_min, theta_max] using the trapezoid method and n subintervals.
    For the purposes of the given question, this uses the polar form of an equation, r(theta).

Acknowledgements:
    I used ChatGPT-4o to partially generate this program and consult it for further polishing.
"""
def trapezoid(theta_min, theta_max, n, r):
    # print("Inside trapezoid method...")
    # Calculate step size (delta theta) by dividing total interval over number of subintervals.
    delta_theta = (theta_max - theta_min) / n
    # Accumulate all r(theta_i)^2 values in area.
    area = 0
    # In trapezoid method, the first and last terms are only multiplied by 1.
    area += r(theta_min)**2 + r(theta_max)**2
    # Now, we sum the "middle terms" from i = 1 to i = n-1, which are each multiplied by 2.
    for i in range(1, n):
        theta_i = theta_min + i*delta_theta
        area += 2 * (r(theta_i)**2)
    # Area = 1/2 * \int_{theta_min}^{theta_max} r^2 d\theta
    area *= 0.5 * 0.5 * delta_theta
    return area

# Kidney Equation (polar form)
# FIXED after HW2 grades released.
def kidney(theta):
    res = (np.cos(theta))**3 + (np.sin(theta))**3
    # Before returning r(theta), make sure it is non-negative.
    if (res > 0):
        return res
    else:
        return 0

# Disc Equation (polar form, and translated to origin)
# FIXED after HW2 grades released.
def disc(theta):
    res = np.sqrt(0.125)
    # Before returning r(theta), make sure it is non-negative.
    if (res > 0):
        return res
    else:
        return 0

def main():
    # Areas have to be correct within 4 significant digits.
    tolerance = 0.5 * 10**(-4)
    if (len(sys.argv) != 2):
       print("Usage: py rpacia_ams326_hw2_p1.py rectangle|trapezoid")
       exit(1)
    elif (sys.argv[1] == "rectangle"):
        # Method 1 - Write a program to use the rectangle method to compute the area of the remaining kidney (4 significant digits).
        print("Rectangle method requested.")
        # Calulate the remaining area in a loop, to approximate 4 significant digits. I'll be using an initial number of 10 subintervals.
        n = 10
        kidney_area = rectangle(0, 2*np.pi, n, kidney)
        disc_area = rectangle(0, 2*np.pi, n, disc)
        prev_area = kidney_area - disc_area
        while True:
            n *= 2
            kidney_area = rectangle(0, 2*np.pi, n, kidney)
            disc_area = rectangle(0, 2*np.pi, n, disc)
            current_area = kidney_area - disc_area
            # Check if the difference between the previous iteration and the current iteration is within tolerance.
            if (abs(current_area - prev_area) < tolerance):
                print("Within tolerance!")
                break
            else:
                # If not within tolerance, repeat again with double the number of subintervals.
                print("Not within tolerance! Looping...")
                prev_area = current_area
        print(f"Kidney area: {kidney_area}")
        print(f"Disc area: {disc_area}")
        print(f"Area of remaining kidney using rectangle method: {kidney_area - disc_area}")
        print(f"Number of subintervals: {n}")
    elif (sys.argv[1] == "trapezoid"):
        # Method 2 - Write a program to use the trapezoid method to compute the area of the remaining kidney (4 significant digits).
        print("Trapezoid method requested.")
        # Calulate the remaining area in a loop, to approximate 4 significant digits. I'll be using an initial number of 10 subintervals.
        n = 10
        kidney_area = trapezoid(0, 2*np.pi, n, kidney)
        disc_area = trapezoid(0, 2*np.pi, n, disc)
        prev_area = kidney_area - disc_area
        while True:
            n *= 2
            kidney_area = trapezoid(0, 2*np.pi, n, kidney)
            disc_area = trapezoid(0, 2*np.pi, n, disc)
            current_area = kidney_area - disc_area
            # Check if the difference between the previous iteration and the current iteration is within tolerance.
            if (abs(current_area - prev_area) < tolerance):
                print("Within tolerance!")
                break
            else:
                # If not within tolerance, repeat again with double the number of subintervals.
                print("Not within tolerance! Looping...")
                prev_area = current_area
        print(f"Kidney area: {kidney_area}")
        print(f"Disc area: {disc_area}")
        print(f"Area of remaining kidney using trapezoid method: {kidney_area - disc_area}")
        print(f"Number of subintervals: {n}")
    else:
        print("Usage: py rpacia_ams326_hw2_p1.py rectangle|trapezoid")
        exit(1)
    
    exit(0)

if __name__ == "__main__":
    main()