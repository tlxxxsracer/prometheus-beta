import pytest
import numpy as np
from src.hungarian_algorithm import hungarian_algorithm, calculate_total_cost

def test_basic_assignment():
    """Test a simple assignment problem"""
    cost_matrix = [
        [3, 2, 3],
        [1, 5, 4],
        [2, 4, 6]
    ]
    assignments = hungarian_algorithm(cost_matrix)
    
    # Verify assignments
    assert len(assignments) == 3
    
    # Verify total assignments
    assigned_workers = set(w for w, _ in assignments)
    assigned_tasks = set(t for _, t in assignments)
    assert len(assigned_workers) == 3
    assert len(assigned_tasks) == 3
    
    # Calculate and check total cost
    total_cost = calculate_total_cost(cost_matrix, assignments)
    assert total_cost == 6  # Specific to the given matrix

def test_rectangular_matrix():
    """Test assignment with rectangular matrix"""
    cost_matrix = [
        [3, 2, 3, 1],
        [1, 5, 4, 2],
        [2, 4, 6, 3]
    ]
    assignments = hungarian_algorithm(cost_matrix)
    
    # Verify assignments match the shorter dimension
    assert len(assignments) == 3
    
    # Verify unique assignments
    assigned_workers = set(w for w, _ in assignments)
    assigned_tasks = set(t for _, t in assignments)
    assert len(assigned_workers) == 3
    assert len(assigned_tasks) == min(len(cost_matrix[0]), len(cost_matrix))

def test_empty_matrix():
    """Test empty matrix handling"""
    cost_matrix = []
    assignments = hungarian_algorithm(cost_matrix)
    assert assignments == []

def test_single_element_matrix():
    """Test single element matrix"""
    cost_matrix = [[5]]
    assignments = hungarian_algorithm(cost_matrix)
    assert assignments == [(0, 0)]

def test_invalid_input_types():
    """Test error handling for invalid input types"""
    with pytest.raises(ValueError, match="Input must be a 2D"):
        hungarian_algorithm(None)
    
    with pytest.raises(ValueError, match="Input must be a 2D"):
        hungarian_algorithm([1, 2, 3])

def test_cost_calculation():
    """Test cost calculation function"""
    cost_matrix = [
        [3, 2, 3],
        [1, 5, 4],
        [2, 4, 6]
    ]
    assignments = [(0, 1), (1, 0), (2, 2)]
    total_cost = calculate_total_cost(cost_matrix, assignments)
    assert total_cost == 6