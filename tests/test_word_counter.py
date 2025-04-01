import pytest
from src.word_counter import count_words

def test_count_words_normal_string():
    """Test counting words in a normal sentence."""
    assert count_words("Hello world") == 2
    assert count_words("Python is awesome") == 3

def test_count_words_edge_cases():
    """Test various edge cases."""
    assert count_words("") == 0  # Empty string
    assert count_words("   ") == 0  # Only whitespace
    assert count_words("  multiple   spaces  ") == 2  # Multiple whitespaces
    assert count_words(None) == 0  # None input
    assert count_words(123) == 1  # Non-string input is converted
    assert count_words(" Single ") == 1  # Leading/trailing spaces

def test_count_words_special_characters():
    """Test strings with special characters."""
    assert count_words("Hello, world!") == 2
    assert count_words("Python-programming is fun") == 4
    assert count_words("One\tTwo\nThree") == 3  # Tab and newline separators