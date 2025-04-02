import pytest
from src.longest_word import find_longest_word

def test_find_longest_word_basic():
    """Test finding the longest word in a simple sentence."""
    assert find_longest_word("The quick brown fox jumps") == "quick"

def test_find_longest_word_multiple_longest():
    """Test when multiple words have the same longest length."""
    assert find_longest_word("hello world great") == "hello"

def test_find_longest_word_single_word():
    """Test with a single word."""
    assert find_longest_word("programming") == "programming"

def test_find_longest_word_with_punctuation():
    """Test with words containing punctuation."""
    assert find_longest_word("Hello, world! Programming is fun.") == "Programming"

def test_find_longest_word_multiple_spaces():
    """Test with multiple spaces between words."""
    assert find_longest_word("one   two    three") == "three"

def test_find_longest_word_empty_input():
    """Test that an empty string raises a ValueError."""
    with pytest.raises(ValueError, match="Input sentence cannot be empty"):
        find_longest_word("")

def test_find_longest_word_whitespace_only():
    """Test that a string with only whitespace raises a ValueError."""
    with pytest.raises(ValueError, match="Input sentence cannot be empty"):
        find_longest_word("   \t\n")

def test_find_longest_word_invalid_type():
    """Test that non-string input raises a TypeError."""
    with pytest.raises(TypeError, match="Input must be a string"):
        find_longest_word(123)

def test_find_longest_word_with_numbers():
    """Test finding longest word with numbers included."""
    assert find_longest_word("The year 2023 is great") == "great"