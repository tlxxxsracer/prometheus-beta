import pytest
from src.permission_logger import PermissionLogger, UserPermissionLevel

def test_permission_logger_default_initialization():
    """Test default initialization of PermissionLogger."""
    logger = PermissionLogger()
    assert logger is not None

def test_log_with_default_permission():
    """Test logging with default permission level."""
    logged_messages = []
    def mock_log(message):
        logged_messages.append(message)
    
    logger = PermissionLogger(logging_func=mock_log)
    
    # Log a message at default (USER) level
    result = logger.log("Test message")
    assert result is True
    assert len(logged_messages) == 1
    assert logged_messages[0] == "Test message"

def test_log_above_permission_level():
    """Test logging a message above current permission level."""
    logged_messages = []
    def mock_log(message):
        logged_messages.append(message)
    
    # Set default permission to USER
    logger = PermissionLogger(
        logging_func=mock_log, 
        default_permission_level=UserPermissionLevel.USER
    )
    
    # Try to log an ADMIN-level message
    result = logger.log("Admin message", min_permission_level=UserPermissionLevel.ADMIN)
    assert result is False
    assert len(logged_messages) == 0

def test_log_at_matching_permission_level():
    """Test logging a message at matching permission level."""
    logged_messages = []
    def mock_log(message):
        logged_messages.append(message)
    
    # Set default permission to ADMIN
    logger = PermissionLogger(
        logging_func=mock_log, 
        default_permission_level=UserPermissionLevel.ADMIN
    )
    
    # Log an ADMIN-level message
    result = logger.log("Admin message", min_permission_level=UserPermissionLevel.ADMIN)
    assert result is True
    assert len(logged_messages) == 1
    assert logged_messages[0] == "Admin message"

def test_log_below_permission_level():
    """Test logging a message below current permission level."""
    logged_messages = []
    def mock_log(message):
        logged_messages.append(message)
    
    # Set default permission to ADMIN
    logger = PermissionLogger(
        logging_func=mock_log, 
        default_permission_level=UserPermissionLevel.ADMIN
    )
    
    # Try to log a GUEST-level message
    result = logger.log("Guest message", min_permission_level=UserPermissionLevel.GUEST)
    assert result is True
    assert len(logged_messages) == 1
    assert logged_messages[0] == "Guest message"

def test_log_empty_message_error():
    """Test that logging an empty message raises a ValueError."""
    logger = PermissionLogger()
    
    with pytest.raises(ValueError, match="Message cannot be empty"):
        logger.log("")
    
    with pytest.raises(ValueError, match="Message cannot be empty"):
        logger.log(None)  # type: ignore