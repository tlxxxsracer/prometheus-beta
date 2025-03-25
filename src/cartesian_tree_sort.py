from typing import List, TypeVar, Any

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
        self.parent = None  # Track parent for sorting
        self.index = None  # Original index for stable sorting

def build_cartesian_tree(arr: List[T]) -> CartesianTreeNode:
    """
    Build a Cartesian Tree from a given list.
    
    The Cartesian Tree is built to satisfy two properties:
    1. For each node, its value is the min in its subtree
    2. Heap-like property for node relationships
    
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
    
    # Create nodes with tracking
    nodes = [CartesianTreeNode(val) for val in arr]
    for i, node in enumerate(nodes):
        node.index = i
    
    # Stack-based tree construction
    stack = []
    
    for node in nodes:
        # Remove nodes from stack that are larger 
        while stack and stack[-1].value > node.value:
            last_node = stack.pop()
            
            # Update parent relationships
            if not stack:
                # Smallest node becomes parent
                node.left = last_node
                last_node.parent = node
            else:
                # Decide between left and right based on values
                if stack[-1].value > node.value:
                    node.left = last_node
                    last_node.parent = node
                else:
                    stack[-1].right = last_node
                    last_node.parent = stack[-1]
        
        # Connect to top of stack
        if stack:
            stack[-1].right = node
            node.parent = stack[-1]
        
        stack.append(node)
    
    # Last node in stack is the root
    return stack[0]

def cartesian_tree_sort(arr: List[T]) -> List[T]:
    """
    Perform sorting using Cartesian Tree Sort.
    
    The algorithm constructs a Cartesian Tree and uses
    its structure to create a sorted order.
    
    :param arr: Input list to be sorted
    :return: Sorted list
    :raises TypeError: If input is not a list
    :raises ValueError: If input list is empty
    """
    # Build Cartesian Tree
    root = build_cartesian_tree(arr)
    
    # Collect nodes in order, preserving original indices
    sorted_nodes = []
    
    def collect_nodes(node):
        """Recursive collection of nodes."""
        if not node:
            return
        
        collect_nodes(node.left)
        sorted_nodes.append(node)
        collect_nodes(node.right)
    
    collect_nodes(root)
    
    # Sort by the original index to make sorting stable
    sorted_nodes.sort(key=lambda x: x.index)
    
    # Return the values in sorted order
    return [node.value for node in sorted_nodes]