"""
Unit tests for the FrameRateLogger class.

This test suite covers various scenarios and edge cases for the 
frame rate logging functionality.
"""

import pytest
import time
from src.frame_rate_logger import FrameRateLogger

class MockFrameRateLogger(FrameRateLogger):
    """
    Mock version of FrameRateLogger for more controlled testing.
    """
    def __init__(self, sample_duration=5000, mock_frames=None):
        """
        Initialize with optional mock frame times.
        
        Args:
            sample_duration (int): Duration to sample frames.
            mock_frames (list, optional): Predefined frame timestamps.
        """
        super().__init__(sample_duration)
        self._mock_frames = mock_frames or []
        self._mock_frame_index = 0
    
    def _get_current_time(self):
        """
        Override current time with mock frames.
        
        Returns:
            int: Mocked timestamp.
        """
        if self._mock_frames:
            time = self._mock_frames[self._mock_frame_index]
            self._mock_frame_index = min(
                self._mock_frame_index + 1, 
                len(self._mock_frames) - 1
            )
            return time
        return super()._get_current_time()
    
    def _request_next_frame(self, callback):
        """
        Override frame request to simulate controlled environment.
        
        Args:
            callback (callable): Function to call on next frame.
        """
        callback()

def test_frame_rate_logger_initialization():
    """
    Test that the FrameRateLogger initializes correctly.
    """
    logger = FrameRateLogger()
    assert logger.sample_duration == 5000
    assert not logger.is_tracking
    assert len(logger.frame_times) == 0

def test_frame_rate_tracking():
    """
    Test basic frame rate tracking functionality.
    """
    # Simulate frames every 16ms (roughly 60 FPS)
    mock_frames = [0, 16, 32, 48, 64, 5000]
    logger = MockFrameRateLogger(sample_duration=5000, mock_frames=mock_frames)
    
    logger.start_tracking()
    
    assert logger.is_tracking == False  # Tracking stops after sample duration
    assert len(logger.frame_times) > 0
    
    fps = logger.get_frame_rate()
    assert abs(fps - 60) < 1  # Allow small variance

def test_zero_frame_rate():
    """
    Test frame rate calculation with insufficient frames.
    """
    logger = FrameRateLogger()
    assert logger.get_frame_rate() == 0

def test_frame_rate_multiple_tracking():
    """
    Ensure multiple tracking calls are handled correctly.
    """
    logger = FrameRateLogger()
    logger.start_tracking()
    logger.start_tracking()  # Should not restart or cause errors
    
    # Verify state remains consistent
    assert logger.is_tracking

def test_frame_rate_edge_cases():
    """
    Test various edge cases for frame rate logging.
    """
    # Very short sample duration
    logger = FrameRateLogger(sample_duration=10)
    logger.start_tracking()
    time.sleep(0.02)  # Ensure some time passes
    
    fps = logger.get_frame_rate()
    assert fps > 0  # Should capture at least one frame