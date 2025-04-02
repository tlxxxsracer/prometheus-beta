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
        
        # Check that the creation time is within a reasonable range
        assert isinstance(creation_time, datetime.datetime)
        assert before_creation <= creation_time <= after_creation
    
    finally:
        # Clean up the temporary file
        os.unlink(temp_path)

def test_nonexistent_file():
    with pytest.raises(FileNotFoundError):
        get_file_creation_date('nonexistent_file.txt')

@pytest.mark.skipif(platform.system() == 'Windows', 
                    reason="Cannot simulate permission error on Windows")
def test_permission_error(tmpdir):
    # Create a file with no read permissions
    import os
    import stat
    
    test_file = tmpdir.join("no_permission.txt")
    test_file.write("test")
    os.chmod(str(test_file), 0o000)  # Remove all permissions
    
    try:
        with pytest.raises(PermissionError):
            get_file_creation_date(str(test_file))
    finally:
        # Restore permissions to allow cleanup
        os.chmod(str(test_file), 0o644)

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