import numpy as np

def hungarian_algorithm(cost_matrix):
    """
    Implement the Hungarian algorithm for solving the assignment problem.
    
    The Hungarian algorithm finds the optimal assignment that minimizes the total cost
    in an assignment problem where each task must be assigned to exactly one worker.
    
    Args:
        cost_matrix (list or np.ndarray): A 2D matrix of costs where rows represent workers 
                                          and columns represent tasks.
    
    Returns:
        list: A list of (worker, task) assignments that minimize the total cost.
        
    Raises:
        ValueError: If the input is not a valid 2D matrix or has inconsistent dimensions.
    """
    # Validate input
    if not isinstance(cost_matrix, (list, np.ndarray)):
        raise ValueError("Input must be a 2D list or NumPy array")
    
    # Convert to NumPy array for consistency
    try:
        matrix = np.array(cost_matrix, dtype=float)
    except Exception:
        raise ValueError("Input must be a 2D list or NumPy array")
    
    # Handle empty matrix
    if matrix.size == 0:
        return []
    
    # Check matrix dimensions
    if matrix.ndim != 2:
        raise ValueError("Input must be a 2D matrix")
    
    rows, cols = matrix.shape
    
    # Create a working copy of the matrix
    work_matrix = matrix.copy()
    
    # Ensure square matrix by padding if necessary
    max_dim = max(rows, cols)
    padded_matrix = np.full((max_dim, max_dim), np.max(work_matrix) + 1)
    padded_matrix[:rows, :cols] = work_matrix
    
    # Step 1: Subtract row minimums
    for i in range(max_dim):
        padded_matrix[i] -= padded_matrix[i].min()
    
    # Step 2: Subtract column minimums
    for j in range(max_dim):
        padded_matrix[:, j] -= padded_matrix[:, j].min()
    
    # Find optimal assignments
    assignments = []
    row_covered = [False] * max_dim
    col_covered = [False] * max_dim
    
    for _ in range(max_dim):
        # Find an uncovered zero
        for i in range(max_dim):
            if row_covered[i]:
                continue
            
            zero_cols = np.where(padded_matrix[i] == 0)[0]
            for j in zero_cols:
                if not col_covered[j]:
                    # Assign if within original matrix dimensions
                    if i < rows and j < cols:
                        assignments.append((i, j))
                    row_covered[i] = True
                    col_covered[j] = True
                    break
    
    return assignments

def calculate_total_cost(cost_matrix, assignments):
    """
    Calculate the total cost of the given assignment.
    
    Args:
        cost_matrix (list or np.ndarray): Original cost matrix
        assignments (list): List of (worker, task) assignments
    
    Returns:
        int: Total cost of the assignment
    """
    # Convert to NumPy array if it's a list
    cost_matrix = np.array(cost_matrix)
    
    # Calculate total cost
    return int(sum(cost_matrix[worker][task] for worker, task in assignments))