import logging
import functools

def conditional_debug_log(condition=True, logger=None):
    """
    A decorator for conditionally logging debug messages.

    Args:
        condition (bool, optional): Whether debugging should be enabled. 
            Defaults to True.
        logger (logging.Logger, optional): Custom logger to use. 
            If None, uses the root logger.

    Returns:
        callable: A decorator that conditionally logs debug messages.

    Example:
        >>> @conditional_debug_log(condition=True)
        ... def example_function():
        ...     return "Function executed"
    """
    # Use root logger if no logger is provided
    if logger is None:
        logger = logging.getLogger()

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Only log if condition is True
            if condition:
                logger.debug(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")
            
            # Execute the function
            result = func(*args, **kwargs)
            
            # Only log if condition is True
            if condition:
                logger.debug(f"{func.__name__} returned: {result}")
            
            return result
        return wrapper
    return decorator