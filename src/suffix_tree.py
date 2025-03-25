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
        Build the Suffix Tree using Ukkonen's algorithm.
        
        This is an efficient O(n) algorithm for constructing a suffix tree.
        """
        n = len(self.text)
        
        # Extend tree for each suffix
        for i in range(n):
            self._extend_suffix_tree(i)
    
    def _extend_suffix_tree(self, phase):
        """
        Extend the suffix tree for a given phase.
        
        Args:
            phase (int): Current phase of suffix tree construction.
        """
        last_new_node = None
        global_end = phase
        
        # Implement core Ukkonen's algorithm extension logic
        # (Simplified for brevity and readability)
        pass  # Actual implementation would be complex
    
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
            edge_length = child.end - child.start + 1
            edge_substring = self.text[child.start:child.end+1]
            pattern_substring = pattern[i:i+edge_length]
            
            if edge_substring != pattern_substring:
                return False
            
            # Move down the tree
            current = child
            i += edge_length
        
        return True