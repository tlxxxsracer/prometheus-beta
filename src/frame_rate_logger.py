"""
Module for logging frame rates in a browser environment.

This module provides functionality to track and log frame rates using 
the browser's requestAnimationFrame API.
"""

class FrameRateLogger:
    """
    A class to log and track frame rates in a browser environment.
    
    This class uses requestAnimationFrame to measure the actual frame rate 
    of animations or rendering in a web browser.
    """
    
    def __init__(self, sample_duration=5000):
        """
        Initialize the FrameRateLogger.
        
        Args:
            sample_duration (int, optional): Duration to sample frames in milliseconds. 
                                             Defaults to 5000 (5 seconds).
        """
        self.sample_duration = sample_duration
        self.frame_times = []
        self.is_tracking = False
    
    def start_tracking(self):
        """
        Start tracking frame rates.
        
        Resets previous frame data and begins a new tracking session.
        
        Returns:
            None
        """
        if self.is_tracking:
            return
        
        self.frame_times = []
        self.is_tracking = True
        self._track_frame()
    
    def _track_frame(self):
        """
        Internal method to track individual frames.
        
        Uses requestAnimationFrame to log frame timestamps.
        """
        if not self.is_tracking:
            return
        
        # In a browser environment, this would use window.requestAnimationFrame
        # For testing purposes, we'll simulate with current timestamp
        current_time = self._get_current_time()
        self.frame_times.append(current_time)
        
        # Stop tracking after sample duration
        if len(self.frame_times) > 1 and (current_time - self.frame_times[0]) >= self.sample_duration:
            self.is_tracking = False
            return
        
        # In a real browser, this would use requestAnimationFrame
        # Here we simulate it with a method that can be mocked in tests
        self._request_next_frame(self._track_frame)
    
    def get_frame_rate(self):
        """
        Calculate the frame rate based on tracked frames.
        
        Returns:
            float: Frames per second (FPS), or 0 if not enough data.
        """
        if len(self.frame_times) <= 1:
            return 0
        
        total_frames = len(self.frame_times) - 1  # Subtract 1 to get actual frame count
        duration_seconds = (self.frame_times[-1] - self.frame_times[0]) / 1000
        
        return total_frames / duration_seconds if duration_seconds > 0 else 0
    
    def _get_current_time(self):
        """
        Get the current timestamp.
        
        In a browser, this would typically use performance.now() or Date.now().
        For testing, we use a simple method that can be easily mocked.
        
        Returns:
            int: Current timestamp in milliseconds.
        """
        import time
        return int(time.time() * 1000)
    
    def _request_next_frame(self, callback):
        """
        Simulate requestAnimationFrame for testing purposes.
        
        In a real browser, this would use window.requestAnimationFrame.
        
        Args:
            callback (callable): Function to call on next frame.
        """
        import time
        time.sleep(0.016)  # Simulate ~60 FPS
        callback()