import pytest
import logging
import psutil
from src.memory_logger import log_memory_usage

class MockLogger:
    def __init__(self):
        self.logs = []
    
    def info(self, msg):
        self.logs.append(('info', msg))
    
    def error(self, msg):
        self.logs.append(('error', msg))

def test_log_memory_usage_returns_correct_keys():
    """Test that the function returns a dictionary with expected keys."""
    memory_stats = log_memory_usage()
    
    expected_keys = [
        'total_memory', 
        'available_memory', 
        'used_memory', 
        'memory_percent', 
        'free_memory'
    ]
    
    for key in expected_keys:
        assert key in memory_stats, f"Missing key: {key}"

def test_log_memory_usage_with_custom_logger():
    """Test logging with a custom logger."""
    mock_logger = MockLogger()
    memory_stats = log_memory_usage(mock_logger)
    
    # Check that an info log was created
    assert len(mock_logger.logs) > 0
    assert mock_logger.logs[0][0] == 'info'
    assert 'Memory Usage Statistics' in mock_logger.logs[0][1]

def test_log_memory_usage_memory_values():
    """Test that memory values are reasonable."""
    memory_stats = log_memory_usage()
    
    # Total memory should be greater than 0
    assert memory_stats['total_memory'] > 0
    
    # Memory percent should be between 0 and 100
    assert 0 <= memory_stats['memory_percent'] <= 100
    
    # Available memory should not exceed total memory
    assert memory_stats['available_memory'] <= memory_stats['total_memory']

def test_log_memory_usage_mock_psutil_error(monkeypatch):
    """Test error handling when psutil fails."""
    def mock_virtual_memory():
        raise Exception("Simulated psutil error")
    
    monkeypatch.setattr(psutil, 'virtual_memory', mock_virtual_memory)
    
    with pytest.raises(RuntimeError, match="Failed to retrieve memory usage"):
        log_memory_usage()