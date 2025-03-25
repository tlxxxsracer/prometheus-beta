from typing import List, TypeVar, Optional, Any

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
    
    A Cartesian Tree satisfies the following properties:
    1. Binary tree structure
    2. Minimum heap property
    3. In-order traversal matches input array
    
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
    
    # Construct nodes
    nodes = [CartesianTreeNode(val) for val in arr]
    
    # First node is always the root
    for i in range(1, len(nodes)):
        # Find insertion point
        parent = i - 1
        while parent >= 0 and nodes[parent].value > nodes[i].value:
            parent -= 1
        
        if parent == -1:
            # Becomes the new root
            nodes[i].left = nodes[0]
            nodes[0] = nodes[i]
        else:
            # Becomes right child of parent
            nodes[i].left = nodes[parent].right
            nodes[parent].right = nodes[i]
    
    return nodes[0]

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