import os
import pytest
import tempfile

from src.file_writer import write_string_to_file

def test_write_string_to_file_success():
    """Test successfully writing a string to a file."""
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
        temp_path = temp_file.name
    
    test_content = "Hello, world!"
    write_string_to_file(temp_path, test_content)
    
    # Verify the file contents
    with open(temp_path, 'r', encoding='utf-8') as file:
        assert file.read() == test_content
    
    # Clean up
    os.unlink(temp_path)

def test_write_string_to_empty_file():
    """Test writing an empty string to a file."""
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
        temp_path = temp_file.name
    
    write_string_to_file(temp_path, "")
    
    # Verify the file is empty
    with open(temp_path, 'r', encoding='utf-8') as file:
        assert file.read() == ""
    
    # Clean up
    os.unlink(temp_path)

def test_invalid_file_path_type():
    """Test raising TypeError for invalid file_path type."""
    with pytest.raises(TypeError, match="file_path must be a string"):
        write_string_to_file(123, "content")

def test_invalid_content_type():
    """Test raising TypeError for invalid content type."""
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
        temp_path = temp_file.name
    
    with pytest.raises(TypeError, match="content must be a string"):
        write_string_to_file(temp_path, 123)
    
    # Clean up
    os.unlink(temp_path)

def test_empty_file_path():
    """Test raising ValueError for empty file path."""
    with pytest.raises(ValueError, match="file_path cannot be an empty string"):
        write_string_to_file("", "content")

def test_none_content():
    """Test raising ValueError for None content."""
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
        temp_path = temp_file.name
    
    with pytest.raises(ValueError, match="content cannot be None"):
        write_string_to_file(temp_path, None)
    
    # Clean up
    os.unlink(temp_path)