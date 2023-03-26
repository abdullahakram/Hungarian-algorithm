import numpy as np

def hungarian_algorithm(cost_matrix):
    """
    Solve the assignment problem using the Hungarian algorithm.

    Parameters:
    cost_matrix (numpy.ndarray): cost matrix of size n x n, where n is the number of rows and columns.

    Returns:
    tuple: a tuple containing the minimum cost and the assignment matrix of size n x n.
    """
    # Step 1: Subtract the minimum value of each row from each element of that row.
    reduced_matrix = cost_matrix - np.min(cost_matrix, axis=1, keepdims=True)

    # Step 2: Subtract the minimum value of each column from each element of that column.
    reduced_matrix = reduced_matrix - np.min(reduced_matrix, axis=0, keepdims=True)

    # Step 3: Mark all the zeros in the reduced matrix.
    n = reduced_matrix.shape[0]
    assignment_matrix = np.zeros((n, n), dtype=int)
    rows_covered = np.zeros(n, dtype=bool)
    cols_covered = np.zeros(n, dtype=bool)

    for i in range(n):
        for j in range(n):
            if reduced_matrix[i, j] == 0 and not rows_covered[i] and not cols_covered[j]:
                assignment_matrix[i, j] = 1
                rows_covered[i] = True
                cols_covered[j] = True

    # Step 4: Repeat until all the zeros are covered.
    while np.sum(rows_covered) < n:
        # Find an uncovered zero.
        i, j = np.where(assignment_matrix == 0)

        # Find the row with the fewest number of uncovered zeros.
        row_counts = np.sum(assignment_matrix == 0, axis=1)
        min_row_count = np.min(row_counts[~rows_covered])
        rows_with_min_count = np.where(row_counts == min_row_count)[0]

        # Choose the first uncovered zero in a row with the fewest number of uncovered zeros.
        for k in range(len(i)):
            if i[k] in rows_with_min_count and not cols_covered[j[k]]:
                assignment_matrix[i[k], j[k]] = 2  # Mark the zero as starred.
                cols_covered[j[k]] = True
                rows_covered[i[k]] = True
                break

        # Find a column with no starred zero.
        if min_row_count == 0:
            cols_with_no_starred_zero = np.where(~cols_covered)[0]
            if len(cols_with_no_starred_zero) == 0:
                break
            j = cols_with_no_starred_zero[0]
            assignment_matrix[np.where(reduced_matrix[:, j] == 0)[0][0], j] = 2
            cols_covered[j] = True
            rows_covered[np.where(reduced_matrix[:, j] == 0)[0][0]] = True

        # Repeat from step 4.
    assignment_matrix = (assignment_matrix == 2).astype(int)
    assignment_cost = np.sum(assignment_matrix * cost_matrix)

    return assignment_cost, assignment_matrix
