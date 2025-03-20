# AMS326 - Numerical Analysis, Spring 2025
# Professor Yuefan Deng
# Homework 2, Problem 2.2
# Ralf Pacia

import numpy as np

"""
Method 1 - Gaussian Elimination

Arguments:
    A:  the input matrix A in Ax = b
    b:  the output vector b in Ax = b

Returns:
    The solution vector x in Ax = b for the given A and b.

Acknowledgements:
    I consulted ChatGPT and Microsoft Copilot to partially generate the code and understand the algorithm behind Gaussian elimination.
"""
def gaussian_elimination(A, b):
    n = len(A)
    # Step 1: Augment matrix A and vector b.
    aug = np.hstack([A, b.reshape(-1, 1)])

    for i in range(n):
        # Step 2: Perform partial pivoting to avoid divide-by-zero errors when performing row operations as part of forward elimination.

        # Find element with max absolute value in column, equal to or below the pivot element aug[i][i].
        max_row_index = i
        max_element = abs(aug[i][i])
        for k in range (i, n):
            if (abs(aug[k][i]) > max_element):
                max_element = abs(aug[k][i])
                max_row_index = k
        # If the max pivot value is on another row, swap rows.
        if (max_row_index != i):
            aug[[i, max_row_index]] = aug[[max_row_index, i]]
        
        # Step 3: Perform row operations to eliminate any elements that are "forward" of the pivot element.
        for j in range(i + 1, n):
            # First, calculate the elimination factor. This allows us to know what to multiply the pivot element by in order to eliminate aug[j][i].
            elim_factor = aug[j][i] / aug[i][i]
            # Perform the elimination of aug[j][i] by multiplying row i by the elimination factor and subtracting it from row j.
            aug[j] = aug[j] - elim_factor * aug[i]
        
    # The augmented matrix is now in upper triangular form, so back substitution can be performed.

    # Step 4 & 5: Back substitution to solve for the solution vector x.
    x = np.zeros(n)
    # Iterate backwards from n-1 to 0.
    for i in range(n-1, -1, -1):
        # Calculate the sum of aug[i][j] * x[j] for j > i.
        # Note that we are only iterating for j > i in order to optimize computing resources by not multiplying out the unknown x-values.
        # This allows us to set up the equation A * x = b', as described in my report.
        partial_total = 0.0
        for j in range(i + 1, n):
            partial_total += aug[i][j] * x[j]
        # Solve for x[i] using the b-value (aug[i][-1]).
        # Numpy syntax denotes that negative indices are traversing the row backwards, so -1 gives us the last column (as a reminder, the b-values are in the last column).
        b_prime = aug[i][-1] - partial_total
        x[i] = b_prime / aug[i][i]

    # Step 6: Return the solution vector x.
    return x.reshape(-1, 1)


def main():
    # Given matrix dimension is 66.
    n = 66
    # Generate matrix A (n by n) with uniform distribution U(-1,1).
    A = np.random.uniform(-1, 1, (n, n))
    # Generate vector b (n by 1) with all values set to 1.
    b = np.ones((n, 1))
    print("My Gaussian Elimination:")
    my_gauss = gaussian_elimination(A, b)
    print(f"{my_gauss}\n")
    print("np.linalg.solve():")
    numpy_sol = np.linalg.solve(A, b)
    print(f"{numpy_sol}\n")
    print(f"Solution vectors approximately equal?: {np.allclose(my_gauss, numpy_sol)}")

if __name__ == "__main__":
    main()