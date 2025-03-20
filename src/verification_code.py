import random
import string
import re

class VerificationCodeGenerator:
    """
    A class to generate and validate unique 6-digit verification codes.
    
    Attributes:
        _used_codes (set): A set to track previously generated codes to ensure uniqueness.
    """
    
    def __init__(self):
        """
        Initialize the VerificationCodeGenerator with an empty set of used codes.
        """
        self._used_codes = set()
    
    def generate_code(self):
        """
        Generate a unique 6-digit verification code.
        
        Returns:
            str: A unique 6-digit verification code.
        """
        while True:
            # Generate a random 6-digit code
            code = ''.join(random.choices(string.digits, k=6))
            
            # Ensure the code is unique
            if code not in self._used_codes:
                self._used_codes.add(code)
                return code
    
    def validate_code(self, code):
        """
        Validate a verification code.
        
        Args:
            code (str): The code to validate.
        
        Returns:
            bool: True if the code is valid, False otherwise.
        
        Raises:
            ValueError: If the input is not a string.
        """
        # Check if input is a string
        if not isinstance(code, str):
            raise ValueError("Code must be a string")
        
        # Check if code matches 6-digit pattern
        if not re.match(r'^\d{6}$', code):
            return False
        
        # Check if code has been used
        return code in self._used_codes
    
    def invalidate_code(self, code):
        """
        Remove a code from the set of valid codes.
        
        Args:
            code (str): The code to invalidate.
        
        Raises:
            ValueError: If the code is not in the used codes set.
        """
        if code not in self._used_codes:
            raise ValueError("Code not found")
        
        self._used_codes.remove(code)