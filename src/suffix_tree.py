class SuffixTree:
    """
    A Suffix Tree implementation for efficient string matching.
    
    The Suffix Tree allows for fast substring search and pattern matching 
    with O(m) time complexity for search, where m is the length of the pattern.
    """
    
    class Node:
        """
        Internal node class for the Suffix Tree.
        
        Each node represents a point in the tree and contains:
        - children: dictionary of child nodes
        - suffix_link: link to another node for efficient traversal
        - start: starting index of the edge label
        - end: ending index of the edge label
        """
        def __init__(self, start=-1, end=-1):
            """
            Initialize a node in the Suffix Tree.
            
            Args:
                start (int, optional): Starting index of the edge label. Defaults to -1.
                end (int, optional): Ending index of the edge label. Defaults to -1.
            """
            self.children = {}
            self.suffix_link = None
            self.start = start
            self.end = end
    
    def __init__(self, text):
        """
        Construct a Suffix Tree for the given text.
        
        Args:
            text (str): Input text to build the suffix tree for.
        
        Raises:
            ValueError: If input text is empty or not a string.
        """
        if not isinstance(text, str):
            raise ValueError("Input must be a string")
        
        if not text:
            raise ValueError("Input text cannot be empty")
        
        self.text = text + "$"  # Add termination symbol
        self.root = self.Node()
        self._build_suffix_tree()
    
    def _build_suffix_tree(self):
        """
        Build the Suffix Tree using a simplified approach.
        
        This method adds all suffixes to the tree directly.
        """
        n = len(self.text)
        
        # Add each suffix to the tree
        for i in range(n):
            self._add_suffix(i)
    
    def _add_suffix(self, start_index):
        """
        Add a single suffix to the Suffix Tree.
        
        Args:
            start_index (int): Starting index of the suffix.
        """
        current = self.root
        suffix = self.text[start_index:]
        
        # Traverse or create path for the suffix
        j = 0
        while j < len(suffix):
            current_char = suffix[j]
            
            if current_char not in current.children:
                # Create new leaf node
                new_leaf = self.Node(start=start_index + j, end=len(self.text) - 1)
                current.children[current_char] = new_leaf
                break
            
            # Follow existing path
            child = current.children[current_char]
            edge_length = child.end - child.start + 1
            
            # Check for partial match
            k = 0
            while k < edge_length and j + k < len(suffix) and \
                  self.text[child.start + k] == suffix[j + k]:
                k += 1
            
            if k == edge_length:
                # Move to child node
                current = child
                j += k
            else:
                # Split the edge
                split_node = self.Node(start=child.start, end=child.start + k - 1)
                current.children[current_char] = split_node
                
                # Modify existing child
                child.start += k
                split_node.children[self.text[child.start]] = child
                
                # Create new leaf
                new_leaf = self.Node(start=start_index + j + k, end=len(self.text) - 1)
                split_node.children[suffix[j + k]] = new_leaf
                break
    
    def search(self, pattern):
        """
        Search for a pattern in the Suffix Tree.
        
        Args:
            pattern (str): Pattern to search for.
        
        Returns:
            bool: True if pattern is found, False otherwise.
        
        Raises:
            ValueError: If pattern is empty or not a string.
        """
        if not isinstance(pattern, str):
            raise ValueError("Pattern must be a string")
        
        if not pattern:
            raise ValueError("Pattern cannot be empty")
        
        # Traverse the tree to find the pattern
        current = self.root
        i = 0
        
        while i < len(pattern):
            # Check if current character is a valid child
            if pattern[i] not in current.children:
                return False
            
            # Move to the matching child node
            child = current.children[pattern[i]]
            
            # Compare edge label with remaining pattern
            j = 0
            while j < child.end - child.start + 1 and i < len(pattern):
                if self.text[child.start + j] != pattern[i]:
                    return False
                j += 1
                i += 1
            
            # Move to next node
            current = child
        
        return True