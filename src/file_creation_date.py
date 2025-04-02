import os
import platform
import datetime

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
        if system == 'Windows':
            # Windows uses os.path.getctime()
            creation_time = os.path.getctime(file_path)
        elif system == 'Darwin':  # macOS
            # macOS uses metadata creation time
            stat = os.stat(file_path)
            creation_time = stat.st_birthtime
        else:  # Linux and other Unix-like systems
            # Linux doesn't have a standard way to get creation time
            # Use metadata change time as a fallback
            stat = os.stat(file_path)
            creation_time = stat.st_ctime
        
        return datetime.datetime.fromtimestamp(creation_time)
    
    except PermissionError:
        raise PermissionError(f"Permission denied to access file: {file_path}")
    except Exception as e:
        raise OSError(f"Could not retrieve file creation time: {str(e)}")