import pytest
from src.hyphen_to_space import replace_hyphens_with_spaces

def test_replace_hyphens_with_spaces():
    """Test replacing hyphens with spaces in various scenarios."""
    # Normal case with multiple hyphens
    assert replace_hyphens_with_spaces('hello-world-test') == 'hello world test'
    
    # Single hyphen
    assert replace_hyphens_with_spaces('single-word') == 'single word'
    
    # No hyphens
    assert replace_hyphens_with_spaces('nochange') == 'nochange'
    
    # Empty string
    assert replace_hyphens_with_spaces('') == ''
    
    # Multiple consecutive hyphens
    assert replace_hyphens_with_spaces('multiple----hyphens') == 'multiple    hyphens'

def test_replace_hyphens_with_spaces_error_handling():
    """Test error handling for invalid input types."""
    # Non-string input
    with pytest.raises(TypeError, match="Input must be a string"):
        replace_hyphens_with_spaces(123)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        replace_hyphens_with_spaces(None)