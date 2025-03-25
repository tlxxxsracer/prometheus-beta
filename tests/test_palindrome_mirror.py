import pytest
from src.palindrome_mirror import palindrome_mirror

def test_basic_string():
    """Test palindrome mirror with a basic string."""
    assert palindrome_mirror("hello") == "helloolleh"

def test_empty_string():
    """Test palindrome mirror with an empty string."""
    assert palindrome_mirror("") == ""

def test_single_character():
    """Test palindrome mirror with a single character."""
    assert palindrome_mirror("a") == "aa"

def test_string_with_numbers():
    """Test palindrome mirror with a string containing numbers."""
    assert palindrome_mirror("12") == "1221"

def test_string_with_special_characters():
    """Test palindrome mirror with special characters."""
    assert palindrome_mirror("A1!") == "A1!!1A"

def test_string_with_spaces():
    """Test palindrome mirror with spaces."""
    assert palindrome_mirror("hello world") == "hello worlddlrow olleh"

def test_mixed_characters():
    """Test palindrome mirror with mixed character types."""
    assert palindrome_mirror("abc123!@#") == "abc123!@##@!321cba"