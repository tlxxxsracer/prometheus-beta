from typing import List, Tuple

def cleanRoom(grid: List[List[int]], r: int, c: int, direction: int) -> int:
    """
    Clean a room using a robot vacuum cleaner algorithm.
    
    Args:
    - grid (List[List[int]]): 2D grid representing the room layout
        0 represents an empty cell that can be cleaned
        1 represents an obstacle that cannot be cleaned
    - r (int): Starting row of the robot
    - c (int): Starting column of the robot
    - direction (int): Initial direction of the robot (0: North, 1: East, 2: South, 3: West)
    
    Returns:
    - int: Minimum number of steps required to clean the entire room
    
    Raises:
    - ValueError: If the grid is invalid or starting position is out of bounds
    """
    # Validate input
    if not grid or not grid[0]:
        raise ValueError("Grid cannot be empty")
    
    if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
        raise ValueError("Starting position is out of bounds")
    
    # Directions: North, East, South, West
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    
    # Track visited cells and total cells to clean
    rows, cols = len(grid), len(grid[0])
    visited = set()
    total_cells_to_clean = sum(row.count(0) for row in grid)
    
    def is_valid_move(x: int, y: int) -> bool:
        """Check if a move is valid (within grid and not an obstacle)"""
        return (0 <= x < rows and 
                0 <= y < cols and 
                grid[x][y] == 0)
    
    def dfs(x: int, y: int, curr_dir: int, steps: int) -> int:
        """
        Depth-first search to clean the room
        
        Args:
        - x (int): Current row
        - y (int): Current column
        - curr_dir (int): Current direction
        - steps (int): Current number of steps
        
        Returns:
        - int: Minimum steps to clean the room
        """
        # Mark current cell as visited if it's cleanable
        if (x, y) not in visited and grid[x][y] == 0:
            visited.add((x, y))
        
        # If all cleanable cells are visited, return steps
        if len(visited) == total_cells_to_clean:
            return steps
        
        # Try all 4 directions
        min_steps = float('inf')
        for i in range(4):
            # Calculate new direction and position
            new_dir = (curr_dir + i) % 4
            dx, dy = directions[new_dir]
            new_x, new_y = x + dx, y + dy
            
            # If move is valid and not visited
            if is_valid_move(new_x, new_y) and (new_x, new_y) not in visited:
                # Recursively explore this path
                curr_steps = dfs(new_x, new_y, new_dir, steps + 1)
                min_steps = min(min_steps, curr_steps)
        
        return min_steps
    
    # Start cleaning from the initial position
    return dfs(r, c, direction, 0)