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
    # Handle various input scenarios
    if cost_matrix is None:
        raise ValueError("Input cannot be None")
    
    # Convert to NumPy array with proper error handling
    try:
        matrix = np.array(cost_matrix, dtype=float)
    except Exception:
        raise ValueError("Input must be a 2D list or NumPy array")
    
    # Handle empty matrix
    if matrix.size == 0:
        return []
    
    # Ensure 2D matrix
    if matrix.ndim != 2:
        raise ValueError("Input must be a 2D matrix")
    
    rows, cols = matrix.shape
    
    # Create a working copy of the matrix
    work_matrix = matrix.copy()
    
    # Step 1: Subtract the minimum from each row
    for i in range(rows):
        work_matrix[i] -= work_matrix[i].min()
    
    # Step 2: Subtract the minimum from each column
    for j in range(cols):
        work_matrix[:, j] -= work_matrix[:, j].min()
    
    # Step 3: Find the optimal assignment
    assignments = []
    row_covered = [False] * rows
    col_covered = [False] * cols
    
    for i in range(rows):
        for j in range(cols):
            # If the element is zero and neither row nor column is covered
            if (work_matrix[i, j] == 0 and 
                not row_covered[i] and 
                not col_covered[j]):
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
        float: Total cost of the assignment
    """
    # Convert to NumPy array if it's a list
    cost_matrix = np.array(cost_matrix)
    
    # Calculate total cost
    return sum(cost_matrix[worker][task] for worker, task in assignments)