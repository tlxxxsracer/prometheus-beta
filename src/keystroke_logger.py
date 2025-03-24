import logging
import sys
import threading

class KeystrokeLogger:
    """
    A class to log keystrokes entered by the user.
    
    This logger provides methods to start and stop keystroke logging,
    with safety mechanisms and error handling.
    """
    
    def __init__(self, log_file='keystrokes.log'):
        """
        Initialize the KeystrokeLogger.
        
        Args:
            log_file (str, optional): Path to the log file. Defaults to 'keystrokes.log'.
        """
        self._logging_active = False
        self._log_file = log_file
        
        # Configure logging
        logging.basicConfig(
            filename=self._log_file, 
            level=logging.INFO, 
            format='%(asctime)s - %(message)s'
        )
    
    def start_logging(self):
        """
        Start logging keystrokes.
        
        Raises:
            RuntimeError: If logging is already active.
        """
        if self._logging_active:
            raise RuntimeError("Keystroke logging is already in progress.")
        
        self._logging_active = True
        logging.info("Keystroke logging started.")
    
    def stop_logging(self):
        """
        Stop logging keystrokes.
        
        Raises:
            RuntimeError: If logging is not currently active.
        """
        if not self._logging_active:
            raise RuntimeError("Keystroke logging is not currently active.")
        
        self._logging_active = False
        logging.info("Keystroke logging stopped.")
    
    def log_keystroke(self, key):
        """
        Log a single keystroke.
        
        Args:
            key (str): The key that was pressed.
        
        Raises:
            RuntimeError: If logging is not active.
            ValueError: If an invalid key is provided.
        """
        if not self._logging_active:
            raise RuntimeError("Keystroke logging is not active.")
        
        if not isinstance(key, str) or len(key) != 1:
            raise ValueError("Key must be a single character.")
        
        logging.info(f"Keystroke: {key}")
    
    def is_logging_active(self):
        """
        Check if keystroke logging is currently active.
        
        Returns:
            bool: True if logging is active, False otherwise.
        """
        return self._logging_active