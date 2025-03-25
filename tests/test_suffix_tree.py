import pytest
from src.suffix_tree import SuffixTree

def test_suffix_tree_initialization():
    """Test basic initialization of Suffix Tree."""
    text = "banana"
    suffix_tree = SuffixTree(text)
    assert suffix_tree.text == "banana$"
    assert suffix_tree.root is not None

def test_suffix_tree_empty_input():
    """Test error handling for empty input."""
    with pytest.raises(ValueError, match="Input text cannot be empty"):
        SuffixTree("")

def test_suffix_tree_invalid_input():
    """Test error handling for non-string input."""
    with pytest.raises(ValueError, match="Input must be a string"):
        SuffixTree(123)

def test_search_basic_pattern():
    """Test basic pattern searching."""
    text = "banana"
    suffix_tree = SuffixTree(text)
    
    # Existing patterns
    assert suffix_tree.search("banana") == True
    assert suffix_tree.search("ana") == True
    assert suffix_tree.search("ban") == True
    
    # Non-existing patterns
    assert suffix_tree.search("apple") == False
    assert suffix_tree.search("bananaa") == False

def test_search_edge_cases():
    """Test edge cases for pattern searching."""
    text = "mississippi"
    suffix_tree = SuffixTree(text)
    
    # Single character patterns
    assert suffix_tree.search("m") == True
    assert suffix_tree.search("x") == False
    
    # Patterns at different positions
    assert suffix_tree.search("iss") == True
    assert suffix_tree.search("ssi") == True
    assert suffix_tree.search("ippi") == True

def test_search_invalid_inputs():
    """Test error handling for search method."""
    text = "hello"
    suffix_tree = SuffixTree(text)
    
    with pytest.raises(ValueError, match="Pattern must be a string"):
        suffix_tree.search(123)
    
    with pytest.raises(ValueError, match="Pattern cannot be empty"):
        suffix_tree.search("")

def test_long_text_search():
    """Test pattern searching in a longer text."""
    text = "abracadabra" * 10
    suffix_tree = SuffixTree(text)
    
    assert suffix_tree.search("abracadabra") == True
    assert suffix_tree.search("acadabra") == True
    assert suffix_tree.search("nonexistent") == False