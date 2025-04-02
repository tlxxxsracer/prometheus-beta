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
        self._tracking_attempts = 0
    
    def start_tracking(self):
        """
        Start tracking frame rates.
        
        Resets previous frame data and begins a new tracking session.
        
        Returns:
            None
        """
        self._tracking_attempts += 1
        
        # Only start if not already tracking
        if not self.is_tracking:
            self.frame_times = []
            self.is_tracking = True
            self._start_tracking_internal()
    
    def _start_tracking_internal(self):
        """
        Internal method to start actual tracking.
        """
        current_tracking_attempt = self._tracking_attempts
        
        def track_frame():
            """
            Nested function to track individual frames.
            """
            # Verify we're still the active tracking session
            if not self.is_tracking or self._tracking_attempts != current_tracking_attempt:
                return
            
            current_time = self._get_current_time()
            
            # First frame: initialize start time
            if not self.frame_times:
                self._start_time = current_time
            
            self.frame_times.append(current_time)
            
            # Check duration
            if (current_time - self._start_time) >= self.sample_duration:
                self.is_tracking = False
                return
            
            self._request_next_frame(track_frame)
        
        # Start initial tracking
        self._request_next_frame(track_frame)
    
    def get_frame_rate(self):
        """
        Calculate the frame rate based on tracked frames.
        
        Returns:
            float: Frames per second (FPS), or 0 if not enough data.
        """
        if len(self.frame_times) <= 1:
            return 0
        
        total_frames = len(self.frame_times) - 1  # Subtract 1 to get actual frame count
        duration_seconds = (self.frame_times[-1] - self.frame_times[0]) / 1000.0
        
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