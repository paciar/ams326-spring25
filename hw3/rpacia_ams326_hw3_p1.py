# AMS326 - Numerical Analysis, Spring 2025
# Professor Yuefan Deng
# Homework 3, Problem 3.1
# Ralf Pacia

"""
Buffon Disc Problem
- Generate points to serve as the center of each circle
- Number of lines crossed can be calculated by calculating how many integers fall between the range of [center_x - d/2, center_x + d/2]
- Lines will be placed at x = -2, -1, 0, 1, 2, etc. (integer x-values)
- Simulate for all diameters d and keep counters for how many lines were crossed (probably using a dict) -- note that if a line crosses 2 lines it also crosses 1 line (the probabilities are calculated for "at least" 1, 2, 3, 4... lines)
- Calculate probabilities using number of times n lines were crossed / total discs used for all n = 1, 2, 3, 4 lines
"""

import numpy as np
import math
import matplotlib.pyplot as plot
import matplotlib.patches as mpatches

def buffon_disc(d, n):
    # I'll use a 20 by 20 grid for point generation, but the "lines" can extend infinitely (i.e. discs generated on the border of the grid can still cross lines that are outside of the grid)
    # Generate n disc centers with diameter d
    y_min, y_max = -10, 10
    x_min, x_max = -10, 10
    disc_centers = np.random.uniform(low=[x_min, y_min], high=[x_max, y_max], size=(n, 2))
    r = d/2
    # For each point, check how many lines a disc centered at that point with diameter d it crosses
    # Maximum number of lines that can be crossed is 4 (maximum d value given in the problem is 3)
    crossings = [0, 0, 0, 0]
    for center in disc_centers:
        # ChatGPT helped me with finding a formula to calculate crossings (i.e. how many integers occur within the range [x-r, x+r])
        center_x = center[0]
        num_crossings = max(0, math.floor(center_x + r) - math.ceil(center_x - r) + 1)
        # We want to update the number of crossings "cumulatively" -- if a disc crossed 3 lines, it also crossed 2 lines and 1 line
        for i in range(num_crossings):
            crossings[i] += 1
    # Calculate probabilities
    probabilities = [0, 0, 0, 0]
    for i in range(len(crossings)):
        probabilities[i] = crossings[i] / n
    return crossings, probabilities

def main():
    n = 4_444_444
    diameters = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1.5, 2, 3]
    probs = {}
    for d in diameters:
        crossings, probabilities = buffon_disc(d, n)
        print(f"Diameter: {d}")
        for i in range(len(crossings)):
            if (i == 0):
                print(f"Number of discs crossing at least {i+1} line: {crossings[i]}")
            else:
                print(f"Number of discs crossing at least {i+1} lines: {crossings[i]}")
        for i in range(len(probabilities)):
            if (i == 0):
                print(f"P[disc crossing at least {i+1} line]: {probabilities[i]:.4f}")
            else:
                print(f"P[disc crossing at least {i+1} lines]: {probabilities[i]:.4f}")
        probs[d] = probabilities
        print()

    # Referenced from https://matplotlib.org/stable/gallery/lines_bars_and_markers/barchart.html#sphx-glr-gallery-lines-bars-and-markers-barchart-py
    # Refined with ChatGPT
    diameter_labels = [f"d={d}" for d in diameters]
    prob = np.array([probs[d] for d in diameters]).T
    x = np.arange(len(diameters))*5
    width = 1
    fig, ax = plot.subplots(figsize=(20,20), layout="constrained")
    for i, probability in enumerate(prob):
        offset = width * i
        rects = ax.bar(x + offset, probability, width)
        ax.bar_label(rects, padding=10, fmt="%.2f", fontsize=6)
    ax.set_ylabel('Probability')
    ax.set_xlabel('Diameter')
    ax.set_title('Buffon Disc: Probability of Crossing at least 1/2/3/4 Lines by Diameter')
    ax.set_xticks(x + width * 1.5, diameter_labels)
    ax.set_ylim(0, 1.1)
    custom_legend = [
        mpatches.Patch(color='C0', label='probability of crossing at least 1 line'),
        mpatches.Patch(color='C1', label='probability of crossing at least 2 lines'),
        mpatches.Patch(color='C2', label='probability of crossing at least 3 lines'),
        mpatches.Patch(color='C3', label='probability of crossing at least 4 lines'),
    ]
    ax.legend(handles=custom_legend, loc='upper left', fontsize=8)
    plot.show()

if __name__ == "__main__":
    main()
