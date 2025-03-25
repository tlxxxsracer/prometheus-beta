import pytest
from src.alternating_case import convert_to_alternating_case

def test_convert_to_alternating_case_basic():
    """Test basic string conversion."""
    assert convert_to_alternating_case("hello world") == "HeLlO WoRlD"

def test_convert_to_alternating_case_empty_string():
    """Test conversion of an empty string."""
    assert convert_to_alternating_case("") == ""

def test_convert_to_alternating_case_single_char():
    """Test conversion of a single character."""
    assert convert_to_alternating_case("a") == "A"
    assert convert_to_alternating_case("Z") == "Z"

def test_convert_to_alternating_case_with_spaces():
    """Test conversion with multiple spaces."""
    assert convert_to_alternating_case("   space   test   ") == "   SpAcE   TeSt   "

def test_convert_to_alternating_case_with_punctuation():
    """Test conversion with punctuation and mixed characters."""
    assert convert_to_alternating_case("hello, world! 123") == "HeLlO, WoRlD! 123"

def test_convert_to_alternating_case_error_handling():
    """Test error handling for non-string input."""
    with pytest.raises(TypeError, match="Input must be a string"):
        convert_to_alternating_case(123)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        convert_to_alternating_case(None)

def test_convert_to_alternating_case_unicode():
    """Test conversion with Unicode characters."""
    assert convert_to_alternating_case("áéíóú") == "ÁéÍóÚ"