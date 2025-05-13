# AMS326 - Numerical Analysis, Spring 2025
# Professor Yuefan Deng
# Final Exam, Problem F.3
# Ralf Pacia

import numpy as np

# Generate matrices A and B using range ~U(-1, 1) of dimension n = 2^10
n = 2**10
def generate_matrices(n):
    A = np.random.uniform(low=-1, high=1, size=(n, n))
    B = np.random.uniform(low=-1, high=1, size=(n, n))
    return A, B
