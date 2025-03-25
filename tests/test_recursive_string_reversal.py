import pytest
from src.recursive_string_reversal import recursive_string_reversal

def test_recursive_string_reversal_normal():
    """Test reversing a standard string"""
    assert recursive_string_reversal("hello") == "olleh"
    assert recursive_string_reversal("python") == "nohtyp"

def test_recursive_string_reversal_empty():
    """Test reversing an empty string"""
    assert recursive_string_reversal("") == ""

def test_recursive_string_reversal_single_char():
    """Test reversing a single character"""
    assert recursive_string_reversal("a") == "a"

def test_recursive_string_reversal_with_spaces():
    """Test reversing a string with spaces"""
    assert recursive_string_reversal("hello world") == "dlrow olleh"

def test_recursive_string_reversal_with_special_chars():
    """Test reversing a string with special characters"""
    assert recursive_string_reversal("a1b2c3!@#") == "#@!3c2b1a"

def test_recursive_string_reversal_invalid_input():
    """Test handling of invalid input types"""
    with pytest.raises(TypeError):
        recursive_string_reversal(123)
    
    with pytest.raises(TypeError):
        recursive_string_reversal(None)
    
    with pytest.raises(TypeError):
        recursive_string_reversal(["list"])