import pytest
from src.parentheses_balance import is_balanced_parentheses

def test_balanced_parentheses():
    """Test various balanced parentheses scenarios"""
    assert is_balanced_parentheses("()") == True
    assert is_balanced_parentheses("((()))") == True
    assert is_balanced_parentheses("()()") == True
    assert is_balanced_parentheses("(())()") == True
    assert is_balanced_parentheses("") == True

def test_unbalanced_parentheses():
    """Test various unbalanced parentheses scenarios"""
    assert is_balanced_parentheses("(") == False
    assert is_balanced_parentheses(")") == False
    assert is_balanced_parentheses(")(") == False
    assert is_balanced_parentheses("((()") == False
    assert is_balanced_parentheses("())") == False

def test_nested_parentheses():
    """Test more complex nested parentheses scenarios"""
    assert is_balanced_parentheses("((()))") == True
    assert is_balanced_parentheses("(()())") == True
    assert is_balanced_parentheses("((())())") == True

def test_invalid_input():
    """Test scenarios with unexpected input"""
    with pytest.raises(TypeError):
        is_balanced_parentheses(None)
    with pytest.raises(TypeError):
        is_balanced_parentheses(123)

def test_mixed_characters():
    """Test input with non-parentheses characters"""
    with pytest.raises(TypeError):
        is_balanced_parentheses("(a)")
    with pytest.raises(TypeError):
        is_balanced_parentheses("hello()")