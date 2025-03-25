import os
import pytest
import tempfile
import shutil

from src.file_rename import rename_file

def test_rename_file_success():
    """Test successful file renaming."""
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create a source file
        source_path = os.path.join(temp_dir, 'original.txt')
        with open(source_path, 'w') as f:
            f.write('Test content')

        # Define destination path
        dest_path = os.path.join(temp_dir, 'renamed.txt')

        # Rename the file
        result = rename_file(source_path, dest_path)

        # Verify file is renamed
        assert result == dest_path
        assert os.path.exists(dest_path)
        assert not os.path.exists(source_path)

def test_rename_across_directories():
    """Test renaming a file across different directories."""
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create source directory and file
        source_dir = os.path.join(temp_dir, 'source')
        dest_dir = os.path.join(temp_dir, 'destination')
        os.makedirs(source_dir)
        os.makedirs(dest_dir)

        source_path = os.path.join(source_dir, 'original.txt')
        with open(source_path, 'w') as f:
            f.write('Test content')

        dest_path = os.path.join(dest_dir, 'renamed.txt')

        # Move the file
        result = rename_file(source_path, dest_path)

        # Verify file is moved
        assert result == dest_path
        assert os.path.exists(dest_path)
        assert not os.path.exists(source_path)

def test_rename_nonexistent_file():
    """Test renaming a non-existent file raises FileNotFoundError."""
    with tempfile.TemporaryDirectory() as temp_dir:
        source_path = os.path.join(temp_dir, 'nonexistent.txt')
        dest_path = os.path.join(temp_dir, 'renamed.txt')

        with pytest.raises(FileNotFoundError):
            rename_file(source_path, dest_path)

def test_rename_to_existing_file():
    """Test renaming to an already existing file raises FileExistsError."""
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create source file
        source_path = os.path.join(temp_dir, 'original.txt')
        with open(source_path, 'w') as f:
            f.write('Test content')

        # Create destination file
        dest_path = os.path.join(temp_dir, 'existing.txt')
        with open(dest_path, 'w') as f:
            f.write('Existing content')

        with pytest.raises(FileExistsError):
            rename_file(source_path, dest_path)

def test_rename_directory_not_file():
    """Test attempting to rename a directory raises IsADirectoryError."""
    with tempfile.TemporaryDirectory() as temp_dir:
        source_dir = os.path.join(temp_dir, 'source_dir')
        os.makedirs(source_dir)
        dest_path = os.path.join(temp_dir, 'renamed')

        with pytest.raises(IsADirectoryError):
            rename_file(source_dir, dest_path)

def test_invalid_input_types():
    """Test handling of invalid input types."""
    with tempfile.TemporaryDirectory() as temp_dir:
        # Test non-string inputs
        with pytest.raises(TypeError):
            rename_file(123, 'test.txt')
        with pytest.raises(TypeError):
            rename_file('test.txt', 123)