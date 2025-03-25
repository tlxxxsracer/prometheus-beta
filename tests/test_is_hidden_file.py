import os
import pytest
import tempfile
import sys

from src.is_hidden_file import is_hidden_file


def test_unix_hidden_file():
    """Test hidden files with Unix/Linux dot prefix convention."""
    with tempfile.NamedTemporaryFile(prefix='.') as hidden_file:
        assert is_hidden_file(hidden_file.name) is True


def test_normal_file():
    """Test a regular file is not considered hidden."""
    with tempfile.NamedTemporaryFile() as regular_file:
        assert is_hidden_file(regular_file.name) is False


def test_invalid_path():
    """Test that a non-existent file raises FileNotFoundError."""
    with pytest.raises(FileNotFoundError):
        is_hidden_file('/path/to/nonexistent/file')


def test_invalid_input_type():
    """Test that invalid input types raise TypeError."""
    with pytest.raises(TypeError):
        is_hidden_file(123)
    with pytest.raises(TypeError):
        is_hidden_file(None)


def test_hidden_file_in_directory():
    """Test hidden file in a directory."""
    with tempfile.TemporaryDirectory() as temp_dir:
        hidden_file_path = os.path.join(temp_dir, '.hidden_file.txt')
        with open(hidden_file_path, 'w') as f:
            f.write('hidden content')
        
        assert is_hidden_file(hidden_file_path) is True


def test_relative_path():
    """Test that function works with relative paths."""
    with tempfile.TemporaryDirectory() as temp_dir:
        hidden_file_path = os.path.join(temp_dir, '.hidden_file.txt')
        with open(hidden_file_path, 'w') as f:
            f.write('hidden content')
        
        # Change current working directory
        original_dir = os.getcwd()
        os.chdir(temp_dir)
        
        try:
            assert is_hidden_file('.hidden_file.txt') is True
        finally:
            # Restore original working directory
            os.chdir(original_dir)