import pytest
from src.lcm_recursive import lcm_recursive, gcd_recursive

def test_gcd_recursive_basic():
    """Test basic GCD calculations"""
    assert gcd_recursive(48, 18) == 6
    assert gcd_recursive(54, 24) == 6
    assert gcd_recursive(17, 23) == 1

def test_gcd_recursive_zero():
    """Test GCD with zero and other numbers"""
    assert gcd_recursive(0, 5) == 5
    assert gcd_recursive(5, 0) == 5
    assert gcd_recursive(0, 0) == 0

def test_gcd_recursive_negative():
    """Test GCD with negative numbers"""
    assert gcd_recursive(-48, 18) == 6
    assert gcd_recursive(48, -18) == 6
    assert gcd_recursive(-48, -18) == 6

def test_lcm_recursive_basic():
    """Test basic LCM calculations"""
    assert lcm_recursive(4, 6) == 12
    assert lcm_recursive(21, 6) == 42
    assert lcm_recursive(17, 23) == 391

def test_lcm_recursive_ones():
    """Test LCM with one as an input"""
    assert lcm_recursive(1, 5) == 5
    assert lcm_recursive(5, 1) == 5

def test_lcm_recursive_same_number():
    """Test LCM when both inputs are the same"""
    assert lcm_recursive(7, 7) == 7

def test_lcm_recursive_zero_error():
    """Test that LCM raises ZeroDivisionError for zero inputs"""
    with pytest.raises(ZeroDivisionError):
        lcm_recursive(0, 5)
    with pytest.raises(ZeroDivisionError):
        lcm_recursive(5, 0)
    with pytest.raises(ZeroDivisionError):
        lcm_recursive(0, 0)

def test_lcm_recursive_type_error():
    """Test that non-integer inputs raise a TypeError"""
    with pytest.raises(ValueError):
        lcm_recursive(3.14, 5)
    with pytest.raises(ValueError):
        lcm_recursive(5, '10')
    with pytest.raises(ValueError):
        lcm_recursive([1], 10)