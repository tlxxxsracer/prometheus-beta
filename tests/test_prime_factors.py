import pytest
from src.prime_factors import get_prime_factors

def test_prime_factors_basic():
    """Test basic prime factorization scenarios."""
    assert get_prime_factors(12) == [2, 2, 3]
    assert get_prime_factors(15) == [3, 5]
    assert get_prime_factors(100) == [2, 2, 5, 5]

def test_prime_factors_prime_numbers():
    """Test prime numbers are returned correctly."""
    assert get_prime_factors(2) == [2]
    assert get_prime_factors(7) == [7]
    assert get_prime_factors(11) == [11]
    assert get_prime_factors(13) == [13]

def test_prime_factors_large_number():
    """Test factorization of larger numbers."""
    assert get_prime_factors(84) == [2, 2, 3, 7]
    assert get_prime_factors(360) == [2, 2, 2, 3, 3, 5]

def test_prime_factors_one():
    """Test that 1 returns an empty list."""
    assert get_prime_factors(1) == []

def test_prime_factors_invalid_inputs():
    """Test error handling for invalid inputs."""
    with pytest.raises(ValueError, match="Input must be an integer"):
        get_prime_factors("12")
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        get_prime_factors(0)
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        get_prime_factors(-5)
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        get_prime_factors(-100)

def test_prime_factors_sorted():
    """Ensure factors are always returned in ascending order."""
    assert get_prime_factors(12) == [2, 2, 3]  # 12 = 2^2 * 3
    assert get_prime_factors(18) == [2, 3, 3]  # 18 = 2 * 3^2
    assert get_prime_factors(100) == [2, 2, 5, 5]  # 100 = 2^2 * 5^2