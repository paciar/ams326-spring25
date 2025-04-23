# AMS326 - Numerical Analysis, Spring 2025
# Professor Yuefan Deng
# Homework 3, Problem 3.2
# Ralf Pacia

"""
Cookie-Cutter Problem
- Idea is to use Metropolis Method for optimization
- We want to use a relatively large number of samples, so I will be using 250_000
- We randomly initialize a state (x,y,alpha) for the rectangular cutter -- (x,y) is the center and alpha is the angle of rotation
- Based on the heatmap, we know the cutter should be placed near the center, so (x,y) ~U(-0.1, 0.1)
- We want to vary the angle (in degrees) as well, so alpha ~U(0, 180)
- We can also put an extra check in place to make sure (x,y) stays within the bounds of [-0.1, 0.1]
- We want to perturb the x and y dimensions during each iteration using ~U(-0.1, 0.1) and perturb alpha using ~U(-3, 3) since the range for angles is much larger
- If the perturbed state results in a (x,y) that goes outside the bounds of [-0.1, 0.1], we reject it so the cutter does not deviate from the center
- If the perturbed state results in a better-cut area, we accept it -- otherwise, we reject it
- The method stops once the number of samples has been reached
"""

# Required external libraries: numpy, matplotlib, shapely
import numpy as np
import matplotlib.pyplot as plt
from shapely.geometry import Polygon, box
from shapely.affinity import rotate, translate
# Since the program can take a while, we can also track execution time just to let the user know how long it took.
import time
import sys

# Rose curve: r = sin(2 * theta)
# We can generate points along the curve and wrap it in Shapely's Polygon class.
def rose_curve():
    # Generate theta values between [0, 2*pi]
    theta = np.linspace(0, 2 * np.pi, 1000)
    # Calculate r = sin(2 * theta) for all generated theta values
    r = np.abs(np.sin(2 * theta))
    # Convert each (r, theta) to (x,y) coordinates
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    # Wrap all points into a polygon
    rose_polygon = Polygon(np.column_stack((x, y)))
    return rose_polygon

# Rectangle cutter: 1 by 1/sqrt(2), centered at (x,y), and rotated by alpha degrees
def rectangle_cutter(x, y, alpha):
    width = 1
    height = 1 / np.sqrt(2)
    # Create box polygon for the rectangle cutter
    rect_polygon = box(-width/2, -height/2, width/2, height/2)
    # Rotate by alpha degrees
    rect_polygon = rotate(rect_polygon, alpha)
    # Translate to (x,y)
    rect_polygon = translate(rect_polygon, x, y)
    return rect_polygon

# Metropolis method
def metropolis(rose, iterations):
    # Generate random initial state
    init_x = np.random.uniform(-0.1, 0.1)
    init_y = np.random.uniform(-0.1, 0.1)
    init_alpha = np.random.uniform(0, 180)
    # Initial state
    current_state = np.array([init_x, init_y, init_alpha])
    print(f"Number of iterations: {iterations}")
    print(f"Initial state: (x = {current_state[0]:.4f}, y = {current_state[1]:.4f}, alpha = {current_state[2]:.4f})")
    # Calculate initial area of intersection between rose curve and rectangular cutter
    current_area = rose.intersection(rectangle_cutter(*current_state)).area

    # Metropolis method loop
    for _ in range(iterations):
        # Calculate new state
        dx = np.random.uniform(-0.1, 0.1)
        dy = np.random.uniform(-0.1, 0.1)
        da = np.random.uniform(-3, 3)
        perturb_state = np.array([dx, dy, da])
        new_state = current_state + perturb_state

        # Reject state if (x,y) falls outside of [-0.1, 0.1]
        if (new_state[0] < -0.1 or new_state[0] > 0.1):
            continue
        if (new_state[1] < -0.1 or new_state[1] > 0.1):
            continue

        # Calculate new area of intersection between rose curve and rectangular cutter using the new state
        new_area = rose.intersection(rectangle_cutter(*new_state)).area

        # If perturbed state is better, accept it
        if (new_area > current_area):
            current_state = new_state
            current_area = new_area

    # After iterations have completed, return the state and area
    return current_state, current_area

def main():
    # I used the Shapely library to perform the rotations/translations for the cookie cutter and to calculate overlapping area.
    
    iterations = 250_000
    # Allow user to specify iterations
    if (len(sys.argv) == 2):
        try:
            iterations = int(sys.argv[1])
        except Exception as e:
            print("Usage: rpacia_ams326_hw3_p2.py [iterations]")
            print(e)
            exit(1)

    rose = rose_curve()
    start = time.perf_counter()
    best_state, best_area = metropolis(rose, iterations)
    end = time.perf_counter()
    print(f"Optimized state (x,y,alpha): (x = {best_state[0]:.4f}, y = {best_state[1]:.4f}, alpha = {best_state[2]:.4f})")
    print(f"Optimized cut area: {best_area:.4f}")
    print(f"Total execution time: {(end - start):.4f} seconds")

    # Plot the optimized rectangular cutter and rose curve (ChatGPT helped me with this)
    best_rect = rectangle_cutter(*best_state)
    x_rect, y_rect = best_rect.exterior.xy
    x_rose, y_rose = rose.exterior.xy

    plt.figure(figsize=(5,5))
    plt.grid(True)
    plt.plot(x_rose, y_rose, color="red", label="Rose Curve")
    plt.plot(x_rect, y_rect, color="black", label="Rectangular Cutter")
    plt.title("Optimized Rectangular Cutter Placement")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()
