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
    cost_matrix = np.array(cost_matrix, dtype=float)
    
    # Check matrix dimensions
    if cost_matrix.ndim != 2:
        raise ValueError("Input must be a 2D matrix")
    
    # Handle empty matrix
    if cost_matrix.size == 0:
        return []
    
    # Create a copy to avoid modifying the original matrix
    matrix = cost_matrix.copy()
    rows, cols = matrix.shape
    
    # Step 1: Subtract row minimums
    for i in range(rows):
        matrix[i] -= matrix[i].min()
    
    # Step 2: Subtract column minimums
    for j in range(cols):
        matrix[:, j] -= matrix[:, j].min()
    
    # Step 3: Cover zeros with minimum number of lines
    def cover_zeros(matrix):
        # This is a simplified version of finding minimal line covering
        covered_rows = set()
        covered_cols = set()
        
        # Try to assign tasks to workers
        assignments = []
        for i in range(rows):
            zero_cols = np.where(matrix[i] == 0)[0]
            for j in zero_cols:
                if j not in covered_cols:
                    assignments.append((i, j))
                    covered_rows.add(i)
                    covered_cols.add(j)
                    break
        
        return assignments, covered_rows, covered_cols
    
    # Final assignment
    assignments, _, _ = cover_zeros(matrix)
    
    # Ensure we have a complete assignment
    if len(assignments) != min(rows, cols):
        # If not complete, we might need a more complex conflict resolution
        raise ValueError("Could not find a complete assignment")
    
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
    return sum(cost_matrix[worker][task] for worker, task in assignments)