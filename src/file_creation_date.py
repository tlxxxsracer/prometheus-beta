import os
import platform
import datetime
import time

def get_file_creation_date(file_path):
    """
    Get the creation date of a file across different operating systems.

    Args:
        file_path (str): Path to the file.

    Returns:
        datetime.datetime: The creation date of the file.

    Raises:
        FileNotFoundError: If the file does not exist.
        PermissionError: If there's no permission to access the file.
        OSError: If the creation time cannot be retrieved.
    """
    # Validate file existence
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    
    # Different approaches for different platforms
    system = platform.system()
    
    try:
        # Use os.stat for most accurate and consistent results
        stat_info = os.stat(file_path)
        
        # Prefer birth time if available
        if hasattr(stat_info, 'st_birthtime'):  # macOS
            creation_time = stat_info.st_birthtime
        elif system == 'Windows':
            # Windows metadata time
            creation_time = os.path.getctime(file_path)
        else:
            # Fallback to metadata change time for Linux/other systems
            creation_time = stat_info.st_ctime
        
        return datetime.datetime.fromtimestamp(creation_time)
    
    except PermissionError:
        raise PermissionError(f"Permission denied to access file: {file_path}")
    except Exception as e:
        raise OSError(f"Could not retrieve file creation time: {str(e)}")