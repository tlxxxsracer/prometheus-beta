import psutil
import logging
from typing import Dict, Any

def log_memory_usage(logger: logging.Logger = None) -> Dict[str, Any]:
    """
    Log current memory usage statistics and return a dictionary of memory details.

    Args:
        logger (logging.Logger, optional): Logger to use for reporting memory stats. 
                                           If not provided, uses basic logging.

    Returns:
        Dict[str, Any]: A dictionary containing memory usage statistics.

    Raises:
        RuntimeError: If unable to retrieve memory information.
    """
    try:
        # Get memory information
        memory = psutil.virtual_memory()
        
        # Prepare memory statistics dictionary
        memory_stats = {
            'total_memory': memory.total,
            'available_memory': memory.available,
            'used_memory': memory.used,
            'memory_percent': memory.percent,
            'free_memory': memory.free
        }
        
        # Log memory statistics if logger is provided
        if logger:
            logger.info(f"Memory Usage Statistics: {memory_stats}")
        else:
            # If no logger is provided, use basic logging
            logging.info(f"Memory Usage Statistics: {memory_stats}")
        
        return memory_stats
    
    except Exception as e:
        # Handle potential errors in retrieving memory information
        error_msg = f"Failed to retrieve memory usage: {str(e)}"
        if logger:
            logger.error(error_msg)
        else:
            logging.error(error_msg)
        raise RuntimeError(error_msg) from e