def two_sum(nums, target):
    """
    Find two indices in an array that add up to a target sum.

    Args:
        nums (list): A list of integers to search through
        target (int): The target sum to find

    Returns:
        list: A list containing two indices where the corresponding 
              values add up to the target. Returns an empty list 
              if no such indices are found.

    Raises:
        TypeError: If input is not a list or if target is not an integer
        ValueError: If the input list contains non-integer elements
    """
    # Input validation
    if not isinstance(nums, list):
        raise TypeError("Input must be a list")
    
    if not isinstance(target, int):
        raise TypeError("Target must be an integer")
    
    # Validate all list elements are integers
    if not all(isinstance(x, int) for x in nums):
        raise ValueError("All list elements must be integers")
    
    # Create a dictionary to store complement values
    complement_dict = {}
    
    # Iterate through the list with enumeration to keep track of indices
    for i, num in enumerate(nums):
        # Calculate the complement needed to reach the target
        complement = target - num
        
        # Check if the complement exists in our dictionary
        if complement in complement_dict:
            # Return the indices of the two numbers
            return [complement_dict[complement], i]
        
        # Store the current number and its index
        complement_dict[num] = i
    
    # If no solution is found, return an empty list
    return []