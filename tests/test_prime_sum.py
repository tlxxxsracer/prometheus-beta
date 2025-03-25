import pytest
from src.prime_sum import sum_primes

def test_sum_primes_basic():
    """Test basic functionality with small numbers."""
    assert sum_primes(10) == 17  # 2 + 3 + 5 + 7 = 17
    assert sum_primes(20) == 77  # 2 + 3 + 5 + 7 + 11 + 13 + 17 + 19 = 77

def test_sum_primes_edge_cases():
    """Test edge cases and boundary conditions."""
    with pytest.raises(ValueError):
        sum_primes(1)
    
    with pytest.raises(ValueError):
        sum_primes(0)
    
    with pytest.raises(ValueError):
        sum_primes(-5)

def test_sum_primes_type_checking():
    """Ensure type checking works correctly."""
    with pytest.raises(TypeError):
        sum_primes(3.14)
    
    with pytest.raises(TypeError):
        sum_primes("10")
    
    with pytest.raises(TypeError):
        sum_primes(None)

def test_sum_primes_larger_numbers():
    """Test with larger prime sum calculations."""
    assert sum_primes(30) == 129  # 2 + 3 + 5 + 7 + 11 + 13 + 17 + 19 + 23 + 29 = 129
    assert sum_primes(50) == 328  # Sum of primes up to 50

def test_sum_primes_minimal_cases():
    """Test the smallest valid input."""
    assert sum_primes(2) == 2  # Only prime is 2 itself