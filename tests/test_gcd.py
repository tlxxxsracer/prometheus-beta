import pytest
from src.gcd import euclidean_gcd

def test_gcd_basic_cases():
    """Test basic GCD calculations"""
    assert euclidean_gcd(48, 18) == 6
    assert euclidean_gcd(54, 24) == 6
    assert euclidean_gcd(17, 23) == 1

def test_gcd_zero_cases():
    """Test GCD with zero inputs"""
    assert euclidean_gcd(0, 5) == 5
    assert euclidean_gcd(5, 0) == 5
    assert euclidean_gcd(0, 0) == 0

def test_gcd_same_number():
    """Test GCD when both inputs are the same"""
    assert euclidean_gcd(7, 7) == 7
    assert euclidean_gcd(100, 100) == 100

def test_gcd_large_numbers():
    """Test GCD with larger numbers"""
    assert euclidean_gcd(1071, 462) == 21
    assert euclidean_gcd(462, 1071) == 21

def test_gcd_error_handling():
    """Test error handling for invalid inputs"""
    with pytest.raises(TypeError, match="Inputs must be integers"):
        euclidean_gcd(10.5, 20)
    
    with pytest.raises(TypeError, match="Inputs must be integers"):
        euclidean_gcd("10", 20)
    
    with pytest.raises(ValueError, match="Inputs must be non-negative integers"):
        euclidean_gcd(-10, 20)
    
    with pytest.raises(ValueError, match="Inputs must be non-negative integers"):
        euclidean_gcd(10, -20)