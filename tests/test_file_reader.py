import os
import pytest
from src.file_reader import read_file_lines

def test_read_file_lines_normal():
    # Create a temporary test file
    test_file_path = 'tests/test_file.txt'
    with open(test_file_path, 'w') as f:
        f.write("Hello\nWorld\nPython")
    
    # Test reading the file
    lines = read_file_lines(test_file_path)
    assert lines == ['Hello', 'World', 'Python']
    
    # Clean up the test file
    os.remove(test_file_path)

def test_read_file_lines_empty_file():
    # Create an empty test file
    test_file_path = 'tests/empty_file.txt'
    with open(test_file_path, 'w') as f:
        pass
    
    # Test reading the empty file
    lines = read_file_lines(test_file_path)
    assert lines == []
    
    # Clean up the test file
    os.remove(test_file_path)

def test_read_file_lines_single_line():
    # Create a single-line test file
    test_file_path = 'tests/single_line.txt'
    with open(test_file_path, 'w') as f:
        f.write("Single line")
    
    # Test reading the file
    lines = read_file_lines(test_file_path)
    assert lines == ['Single line']
    
    # Clean up the test file
    os.remove(test_file_path)

def test_read_file_lines_file_with_newlines():
    # Create a file with multiple newlines
    test_file_path = 'tests/newlines_file.txt'
    with open(test_file_path, 'w') as f:
        f.write("Line 1\n\nLine 2\n\n\nLine 3")
    
    # Test reading the file
    lines = read_file_lines(test_file_path)
    assert lines == ['Line 1', '', 'Line 2', '', '', 'Line 3']
    
    # Clean up the test file
    os.remove(test_file_path)

def test_read_file_lines_nonexistent_file():
    # Test reading a nonexistent file
    with pytest.raises(FileNotFoundError):
        read_file_lines('nonexistent_file.txt')