import logging
from enum import Enum, auto
from typing import Optional, Callable

class UserPermissionLevel(Enum):
    """Enumeration of user permission levels."""
    GUEST = 0
    USER = 1
    ADMIN = 2

class PermissionLogger:
    """
    A logger that controls message output based on user permission levels.
    
    This class provides a flexible logging mechanism where messages are 
    only logged if the user's permission level meets or exceeds the 
    specified logging threshold.
    """
    
    def __init__(self, 
                 logging_func: Optional[Callable[[str], None]] = None,
                 default_permission_level: UserPermissionLevel = UserPermissionLevel.USER):
        """
        Initialize the PermissionLogger.
        
        Args:
            logging_func (Optional[Callable]): Custom logging function. 
                If None, defaults to print().
            default_permission_level (UserPermissionLevel): Minimum permission 
                level required to log messages. Defaults to USER level.
        """
        self._logging_func = logging_func or print
        self._default_permission_level = default_permission_level
    
    def log(self, 
            message: str, 
            min_permission_level: Optional[UserPermissionLevel] = None) -> bool:
        """
        Log a message based on user permission level.
        
        Args:
            message (str): The message to log
            min_permission_level (Optional[UserPermissionLevel]): 
                Minimum permission level required to log this message. 
                If None, uses the default permission level.
        
        Returns:
            bool: True if message was logged, False otherwise
        
        Raises:
            ValueError: If message is empty or None
        """
        # Validate input
        if not message:
            raise ValueError("Message cannot be empty")
        
        # Use default permission level if not specified
        if min_permission_level is None:
            min_permission_level = self._default_permission_level
        
        # Check if current permission level meets the minimum requirement
        try:
            if self._default_permission_level.value >= min_permission_level.value:
                self._logging_func(message)
                return True
            return False
        except Exception as e:
            # Handle any unexpected errors during logging
            print(f"Logging error: {e}")
            return False