import pytest
from src.longest_substring import find_longest_substring

def test_find_longest_substring_basic():
    """Test basic functionality of the function"""
    assert find_longest_substring("abcabcbb") == "abc"
    assert find_longest_substring("bbbbb") == "b"
    assert find_longest_substring("pwwkew") == "wke"

def test_find_longest_substring_edge_cases():
    """Test edge cases"""
    assert find_longest_substring("") == ""
    assert find_longest_substring("a") == "a"
    assert find_longest_substring("aab") == "ab"

def test_find_longest_substring_case_sensitivity():
    """Verify case-sensitive behavior"""
    assert find_longest_substring("AbcA") == "Abc"
    assert find_longest_substring("aA") == "aA"

def test_find_longest_substring_special_characters():
    """Test with special characters and mixed input"""
    assert find_longest_substring("!@#$%^&*()") == "!@#$%^&*()"
    assert find_longest_substring("abcd123efg") == "abcd123efg"

def test_find_longest_substring_repeated_patterns():
    """Test scenarios with repeated patterns"""
    assert find_longest_substring("dvdf") == "vdf"
    assert find_longest_substring("tmmzuxt") == "mzuxt"