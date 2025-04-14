# AMS326 - Numerical Analysis, Spring 2025
# Professor Yuefan Deng
# Homework 3, Problem 3.2
# Ralf Pacia

"""
Cookie-Cutter Problem
- Idea is to use Metropolis Method for optimization
- We want to use a relatively large number of samples, so I will be using 1_000_000
- We randomly initialize a state (x,y,alpha) for the rectangular cutter -- (x,y) is the center and alpha is the angle of rotation
- Based on the heatmap, we know the cutter should be placed near the center, so (x,y) ~U(-0.1, 0.1)
- We want to vary the angle (in degrees) as well, so alpha ~U(0, 180)
- We can also put an extra check in place to make sure (x,y) stays within the bounds of [-1, 1] and alpha stays within [0, 180]
- We want to perturb all 3 dimensions during each iteration using ~U(-0.1, 0.1)
- If the perturbed state results in a better-cut area, we accept it -- otherwise, we reject it
- The method stops once the number of samples has been reached
"""

# Required external libraries: numpy, matplotlib, shapely
import numpy as np
import matplotlib.pyplot as plot
from shapely.geometry import Polygon, box
from shapely.affinity import rotate, translate
# Since the program can take a while, we can also track execution time just to let the user know how long it took.
import time

# Rose curve: r = sin(2 * theta)
# We can generate points along the curve and wrap it in Shapely's Polygon class.
def rose_curve():
    # Generate theta values between [0, 2*pi]
    theta = np.linspace(0, 2 * np.pi, 10000)
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

def main():
    # I used the Shapely library to perform the rotations/translations for the cookie cutter and to calculate overlapping area.
    exit(0)

if __name__ == "__main__":
    main()
