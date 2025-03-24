import os
import pytest
import logging
from src.keystroke_logger import KeystrokeLogger

def test_keystroke_logger_initialization():
    """Test initializing the KeystrokeLogger."""
    logger = KeystrokeLogger()
    assert logger is not None
    assert not logger.is_logging_active()

def test_start_logging():
    """Test starting keystroke logging."""
    logger = KeystrokeLogger()
    logger.start_logging()
    assert logger.is_logging_active()

def test_stop_logging():
    """Test stopping keystroke logging."""
    logger = KeystrokeLogger()
    logger.start_logging()
    logger.stop_logging()
    assert not logger.is_logging_active()

def test_log_keystroke(tmp_path):
    """Test logging a single keystroke."""
    log_file = str(tmp_path / 'keystrokes.log')
    logger = KeystrokeLogger(log_file)
    logger.start_logging()
    logger.log_keystroke('a')
    logger.stop_logging()

    with open(log_file, 'r') as f:
        log_contents = f.read()
        assert 'Keystroke: a' in log_contents

def test_start_logging_twice_raises_error():
    """Test that starting logging twice raises an error."""
    logger = KeystrokeLogger()
    logger.start_logging()
    with pytest.raises(RuntimeError, match="Keystroke logging is already in progress."):
        logger.start_logging()

def test_stop_logging_without_starting_raises_error():
    """Test that stopping logging without starting raises an error."""
    logger = KeystrokeLogger()
    with pytest.raises(RuntimeError, match="Keystroke logging is not currently active."):
        logger.stop_logging()

def test_log_keystroke_without_starting_raises_error():
    """Test that logging a keystroke without starting raises an error."""
    logger = KeystrokeLogger()
    with pytest.raises(RuntimeError, match="Keystroke logging is not active."):
        logger.log_keystroke('a')

def test_log_invalid_keystroke():
    """Test logging an invalid keystroke raises an error."""
    logger = KeystrokeLogger()
    logger.start_logging()
    
    with pytest.raises(ValueError, match="Key must be a single character."):
        logger.log_keystroke('')
    
    with pytest.raises(ValueError, match="Key must be a single character."):
        logger.log_keystroke('ab')
    
    with pytest.raises(ValueError, match="Key must be a single character."):
        logger.log_keystroke(123)