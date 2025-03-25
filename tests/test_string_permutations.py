import pytest
from src.string_permutations import generate_unique_permutations

def test_basic_permutations():
    """Test basic string permutations"""
    result = generate_unique_permutations("abc")
    assert set(result) == set(['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    assert len(result) == 6

def test_repeated_chars_permutations():
    """Test permutations with repeated characters"""
    result = generate_unique_permutations("aba")
    assert set(result) == set(['aba', 'aab', 'baa'])
    assert len(result) == 3

def test_single_char_permutation():
    """Test permutation of a single character"""
    result = generate_unique_permutations("a")
    assert result == ['a']

def test_empty_string():
    """Test empty string input"""
    result = generate_unique_permutations("")
    assert result == []

def test_invalid_input():
    """Test invalid input type"""
    with pytest.raises(TypeError, match="Input must be a string"):
        generate_unique_permutations(123)
        generate_unique_permutations(None)

def test_unique_output():
    """Ensure all permutations are unique"""
    result = generate_unique_permutations("aab")
    assert len(result) == len(set(result))

def test_result_always_sorted():
    """Verify that the result is always sorted"""
    result = generate_unique_permutations("bac")
    assert result == sorted(result)