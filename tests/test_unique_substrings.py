import pytest
from src.unique_substrings import find_unique_substrings

def test_basic_unique_substrings():
    """Test basic functionality with a simple string."""
    result = find_unique_substrings("abab")
    expected = ['a', 'ab', 'aba', 'abab', 'b', 'ba', 'bab']
    assert sorted(result) == sorted(expected)

def test_empty_string():
    """Test with an empty string."""
    assert find_unique_substrings("") == []

def test_single_character_string():
    """Test with a single character string."""
    assert find_unique_substrings("a") == ['a']

def test_repeated_character_string():
    """Test with a string of repeated characters."""
    result = find_unique_substrings("aaa")
    expected = ['a', 'aa', 'aaa']
    assert sorted(result) == sorted(expected)

def test_different_substrings():
    """Test a string with multiple unique substrings."""
    result = find_unique_substrings("hello")
    expected = ['h', 'he', 'hel', 'hell', 'hello', 
                'e', 'el', 'ell', 'ello', 
                'l', 'll', 'llo', 
                'lo', 
                'o']
    assert sorted(result) == sorted(expected)

def test_input_type_error():
    """Test that a TypeError is raised for non-string input."""
    with pytest.raises(TypeError, match="Input must be a string"):
        find_unique_substrings(123)
    with pytest.raises(TypeError, match="Input must be a string"):
        find_unique_substrings(None)

def test_result_is_sorted():
    """Verify that the result is sorted lexicographically."""
    result = find_unique_substrings("cab")
    assert result == sorted(result)