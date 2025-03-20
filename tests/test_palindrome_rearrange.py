import pytest
from src.palindrome_rearrange import can_form_palindrome, rearrange_to_palindrome

def test_can_form_palindrome_basic():
    """Test basic palindrome formation possibility"""
    assert can_form_palindrome("racecar") == True
    assert can_form_palindrome("aab") == True
    assert can_form_palindrome("abc") == False

def test_can_form_palindrome_edge_cases():
    """Test edge cases for palindrome formation"""
    assert can_form_palindrome("") == True
    assert can_form_palindrome("a") == True
    assert can_form_palindrome("aa") == True
    assert can_form_palindrome("aabaa") == True

def test_can_form_palindrome_errors():
    """Test error handling for invalid inputs"""
    with pytest.raises(TypeError):
        can_form_palindrome(123)
    with pytest.raises(TypeError):
        can_form_palindrome(None)

def test_rearrange_to_palindrome_basic():
    """Test basic palindrome rearrangement"""
    assert rearrange_to_palindrome("racecar") == "racecar"
    
    result = rearrange_to_palindrome("aab")
    assert result == "aba" or result == "baa"
    
    assert rearrange_to_palindrome("abc") == ""

def test_rearrange_to_palindrome_edge_cases():
    """Test edge cases for palindrome rearrangement"""
    assert rearrange_to_palindrome("") == ""
    assert rearrange_to_palindrome("a") == "a"
    assert rearrange_to_palindrome("aa") == "aa"

def test_rearrange_to_palindrome_multiple_chars():
    """Test rearrangement with multiple characters"""
    result = rearrange_to_palindrome("aaabbb")
    assert len(result) == 6
    assert result.count('a') == 3
    assert result.count('b') == 3
    
    result = rearrange_to_palindrome("aabbcc")
    assert len(result) == 6
    assert sorted(result) == list("aabbcc")

def test_rearrange_to_palindrome_errors():
    """Test error handling for invalid inputs"""
    with pytest.raises(TypeError):
        rearrange_to_palindrome(123)
    with pytest.raises(TypeError):
        rearrange_to_palindrome(None)