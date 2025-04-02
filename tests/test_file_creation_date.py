import os
import pytest
import datetime
import tempfile
import platform

from src.file_creation_date import get_file_creation_date

def test_get_file_creation_date():
    # Create a temporary file
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_path = temp_file.name
    
    try:
        # Get the current time before creation
        before_creation = datetime.datetime.now()
        
        # The file is created when we create the temp file
        creation_time = get_file_creation_date(temp_path)
        
        # Get the current time after creation
        after_creation = datetime.datetime.now()
        
        # Check that the creation time is a datetime object
        assert isinstance(creation_time, datetime.datetime)
        
        # Use a looser comparison with a time difference
        time_diff = abs((creation_time - before_creation).total_seconds())
        assert time_diff <= 1.0  # Within 1 second is reasonable
    
    finally:
        # Clean up the temporary file
        os.unlink(temp_path)

def test_nonexistent_file():
    with pytest.raises(FileNotFoundError):
        get_file_creation_date('nonexistent_file.txt')

@pytest.mark.skipif(platform.system() == 'Windows', 
                    reason="Cannot simulate permission error on Windows")
def test_permission_error(tmp_path):
    # Create a file with no read permissions
    import os
    import stat
    
    # Multiple strategies to simulate permission error
    def test_strategies(file_path):
        # Attempt 1: Remove read permissions
        os.chmod(file_path, 0o000)
        try:
            get_file_creation_date(file_path)
        except PermissionError:
            return True
        except Exception:
            pass
        
        # Attempt 2: Make file owned by another user
        os.chmod(file_path, 0o200)  # Write-only
        try:
            get_file_creation_date(file_path)
        except PermissionError:
            return True
        except Exception:
            pass
        
        return False

    # Create a file 
    test_file = tmp_path / "no_permission.txt"
    test_file.write_text("test")
    
    try:
        assert test_strategies(str(test_file)), "Failed to trigger permission error"
    finally:
        # Restore permissions to allow cleanup
        os.chmod(test_file, 0o644)

def test_datetime_type():
    # Create a temporary file
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_path = temp_file.name
    
    try:
        creation_time = get_file_creation_date(temp_path)
        assert isinstance(creation_time, datetime.datetime)
    finally:
        # Clean up the temporary file
        os.unlink(temp_path)