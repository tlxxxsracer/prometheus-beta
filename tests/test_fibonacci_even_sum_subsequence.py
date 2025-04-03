import pytest
from src.fibonacci_even_sum_subsequence import generate_fibonacci_subsequence

def test_zero_input():
    """Test that input 0 returns [0]"""
    assert generate_fibonacci_subsequence(0) == [0]

def test_basic_cases():
    """Test some basic subsequence generations"""
    # Even index sum: 0 + 2 + 8 = 10
    result = generate_fibonacci_subsequence(10)
    assert result == [0, 1, 2, 3, 5, 8]
    
    # Even index sum: 0 + 2 + 34 = 36
    result = generate_fibonacci_subsequence(36)
    assert result == [0, 1, 2, 3, 5, 8, 13, 21, 34]

def test_negative_input():
    """Test that negative inputs raise ValueError"""
    with pytest.raises(ValueError, match="Input must be a non-negative integer"):
        generate_fibonacci_subsequence(-5)

def test_impossible_sum():
    """Test that impossible sums raise ValueError"""
    with pytest.raises(ValueError, match="No Fibonacci subsequence found"):
        generate_fibonacci_subsequence(1000000)

def test_even_index_sum():
    """Verify that even-indexed sum matches input"""
    for target in [0, 10, 36, 100]:
        subsequence = generate_fibonacci_subsequence(target)
        even_sum = sum(subsequence[::2])
        assert even_sum == target, f"Failed for target {target}"