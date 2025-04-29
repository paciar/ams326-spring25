# AMS326 - Numerical Analysis, Spring 2025
# Professor Yuefan Deng
# Exam 3, Problem 3.2
# Ralf Pacia

import numpy as np
from shapely.geometry import Polygon, LineString, Point

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

# Generate a LineString object for a needle of length l centered at (x,y) with rotation angle alpha.
# Computed with the help of ChatGPT.
def generate_needle(x, y, alpha, l):
    dx = (l / 2) * np.cos(alpha)
    dy = (l / 2) * np.sin(alpha)
    # Endpoints of the needle
    p1 = (x-dx, y-dy)
    p2 = (x+dx, y+dy)
    return LineString([p1, p2])

# Given needle states and needle length, calculate how many times 2 or more intersections occur between the needle and the rose
def num_crossings(needle_states, l, rose):
    intersections = 0
    for state in needle_states:
        # Generate needle
        needle = generate_needle(state[0], state[1], state[2], l)
        # Calculate intersection with rose
        inter = needle.intersection(rose)
        # If there are at least 2 intersections, increment counter by 1
        if (not inter.is_empty and not isinstance(inter, Point)):
            intersections += 1
        # Otherwise, do not increment
    return intersections

def main():
    lengths = [0.1, 0.2, 0.25, 0.33, 0.5, 1]
    # Idea: keep a state (x,y,alpha) for each needle
    # Randomly generate (x,y) points in the range x = [-1, 1] and y = [-1, 1] to serve as the center of the needle
    # A random angle alpha = [0, 360] will also be generated to serve as the rotation of the needle

    # Use 1_000_000 needle tosses, as defined in class
    num_tosses = 1_000_000

    # Generate needle states
    # For sake of time, I will use the same needle states (x,y,alpha) for all lengths
    y_min, y_max = -1, 1
    x_min, x_max = -1, 1
    alpha_min, alpha_max = 0, 360
    needle_states = np.random.uniform(low=[x_min, y_min, alpha_min], high=[x_max, y_max, alpha_max], size=(num_tosses, 3))

    # Generate rose curve
    rose = rose_curve()

    # Number of crossings for each needle length
    crossings = [0,0,0,0,0,0]
    probabilities = [0,0,0,0,0,0]
    for i in range(len(crossings)):
        crossings[i] = num_crossings(needle_states, lengths[i], rose)
        # Probability is calculated by number of crossings / total tosses
        probabilities[i] = crossings[i] / num_tosses
    
    for i in range(len(probabilities)):
        print(f"Length: {lengths[i]} \t\t Probability of Crossing: {probabilities[i]}")

if __name__ == "__main__":
    main()