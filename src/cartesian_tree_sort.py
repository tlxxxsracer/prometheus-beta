from typing import List, TypeVar, Optional, Union

T = TypeVar('T')

class CartesianTreeNode:
    """Node class for Cartesian Tree."""
    def __init__(self, value):
        """
        Initialize a Cartesian Tree node.
        
        :param value: The value stored in the node
        """
        self.value = value
        self.left = None
        self.right = None

def build_cartesian_tree(arr: List[T]) -> Optional[CartesianTreeNode]:
    """
    Build a Cartesian Tree from a given list.
    
    A Cartesian Tree is a binary tree constructed from a list where:
    1. The tree has the heap property for values
    2. In-order traversal reproduces the original array
    
    :param arr: Input list to build the Cartesian Tree from
    :return: Root of the Cartesian Tree
    :raises TypeError: If input is not a list
    :raises ValueError: If input list is empty
    """
    # Input validation
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    if not arr:
        raise ValueError("Input list cannot be empty")
    
    # Use monotonic stack to build the Cartesian Tree
    stack = []
    last_root = None
    
    for value in arr:
        last_node = None
        
        # Pop nodes from stack while current value is less than top value
        while stack and stack[-1].value > value:
            last_node = stack.pop()
        
        # Current node
        current = CartesianTreeNode(value)
        
        # If last node exists, it becomes left child of current
        if last_node:
            current.left = last_node
        
        # If stack is not empty, current becomes right child of top node
        if stack:
            stack[-1].right = current
        
        # Push current node
        stack.append(current)
    
    # The last element in the stack is the root
    return stack[0]

def cartesian_tree_sort(arr: List[T]) -> List[T]:
    """
    Sort a list using Cartesian Tree Sort algorithm.
    
    This algorithm works by:
    1. Building a Cartesian Tree from the input list
    2. Performing an in-order traversal to get sorted elements
    
    :param arr: Input list to be sorted
    :return: Sorted list
    :raises TypeError: If input is not a list
    :raises ValueError: If input list is empty
    """
    # Build Cartesian Tree
    root = build_cartesian_tree(arr)
    
    # Initialize result list and perform in-order traversal
    sorted_arr = []
    
    def in_order_traversal(node):
        """Recursive in-order traversal to extract sorted elements."""
        if not node:
            return
        
        in_order_traversal(node.left)
        sorted_arr.append(node.value)
        in_order_traversal(node.right)
    
    in_order_traversal(root)
    
    return sorted_arr