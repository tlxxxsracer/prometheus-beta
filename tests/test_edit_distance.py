import pytest
from src.edit_distance import compute_edit_distance

def test_same_strings():
    """Test when both strings are identical"""
    assert compute_edit_distance("hello", "hello") == 0

def test_empty_strings():
    """Test edit distance with empty strings"""
    assert compute_edit_distance("", "") == 0
    assert compute_edit_distance("hello", "") == 5
    assert compute_edit_distance("", "world") == 5

def test_basic_edits():
    """Test basic edit scenarios"""
    # Deletion
    assert compute_edit_distance("kitten", "kit") == 3
    
    # Insertion
    assert compute_edit_distance("kit", "kitten") == 3
    
    # Substitution
    assert compute_edit_distance("kitten", "sitting") == 3

def test_complex_edits():
    """Test more complex edit distance scenarios"""
    assert compute_edit_distance("saturday", "sunday") == 3
    assert compute_edit_distance("intention", "execution") == 5

def test_case_sensitivity():
    """Test case sensitivity"""
    assert compute_edit_distance("Hello", "hello") == 1

def test_unicode_strings():
    """Test edit distance with unicode strings"""
    assert compute_edit_distance("café", "cafe") == 1

def test_error_handling():
    """Test error handling for invalid input types"""
    with pytest.raises(TypeError):
        compute_edit_distance(123, "hello")
    
    with pytest.raises(TypeError):
        compute_edit_distance("hello", ["world"])
    
    with pytest.raises(TypeError):
        compute_edit_distance(None, None)