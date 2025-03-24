import logging
import pytest
from src.debug_logger import conditional_debug_log

# Configure logging to capture log messages
class LogCapture:
    def __init__(self):
        self.logger = logging.getLogger('test_logger')
        self.logger.setLevel(logging.DEBUG)
        self.handler = logging.Handler()
        self.handler.records = []
        
        def emit(record):
            self.handler.records.append(record)
        
        self.handler.emit = emit
        self.logger.addHandler(self.handler)

    def get_log_messages(self):
        return [record.getMessage() for record in self.handler.records]

def test_conditional_debug_log_enabled():
    """Test that debug logs are recorded when condition is True."""
    log_capture = LogCapture()
    
    @conditional_debug_log(condition=True, logger=log_capture.logger)
    def test_func(x, y):
        return x + y
    
    result = test_func(3, 4)
    
    # Check function works correctly
    assert result == 7
    
    # Check log messages
    log_messages = log_capture.get_log_messages()
    assert len(log_messages) == 2
    assert "Calling test_func with args: (3, 4), kwargs: {}" in log_messages[0]
    assert "test_func returned: 7" in log_messages[1]

def test_conditional_debug_log_disabled():
    """Test that debug logs are not recorded when condition is False."""
    log_capture = LogCapture()
    
    @conditional_debug_log(condition=False, logger=log_capture.logger)
    def test_func(x, y):
        return x + y
    
    result = test_func(3, 4)
    
    # Check function works correctly
    assert result == 7
    
    # Check no log messages were recorded
    log_messages = log_capture.get_log_messages()
    assert len(log_messages) == 0

def test_conditional_debug_log_default_logger():
    """Test that the decorator works with the default root logger."""
    # Capture root logger
    root_logger = logging.getLogger()
    original_level = root_logger.level
    
    try:
        # Set up logging capture
        log_capture = logging.Handler()
        log_capture.records = []
        
        def emit(record):
            log_capture.records.append(record)
        
        log_capture.emit = emit
        root_logger.addHandler(log_capture)
        root_logger.setLevel(logging.DEBUG)
        
        @conditional_debug_log()  # Use default parameters
        def test_func(x, y):
            return x + y
        
        result = test_func(5, 6)
        
        # Check function works correctly
        assert result == 11
        
        # Check log messages
        log_messages = [record.getMessage() for record in log_capture.records]
        assert len(log_messages) == 2
        assert "Calling test_func with args: (5, 6), kwargs: {}" in log_messages[0]
        assert "test_func returned: 11" in log_messages[1]
    
    finally:
        # Reset root logger
        root_logger.removeHandler(log_capture)
        root_logger.setLevel(original_level)