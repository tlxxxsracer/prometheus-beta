"""
Unit tests for LZ78 Compression Algorithm
"""

import pytest
from src.lz78_compression import lz78_compress, lz78_decompress

def test_lz78_compress_simple_string():
    """Test compression of a simple string"""
    input_str = "TOBEORNOTTOBEORTOBEORNOT"
    compressed = lz78_compress(input_str)
    assert isinstance(compressed, list)
    assert len(compressed) > 0

def test_lz78_decompress_simple_string():
    """Test decompression of a simple compressed string"""
    input_str = "TOBEORNOTTOBEORTOBEORNOT"
    compressed = lz78_compress(input_str)
    decompressed = lz78_decompress(compressed)
    assert decompressed == input_str

def test_lz78_compress_repeat_patterns():
    """Test compression of string with repeating patterns"""
    input_str = "ABABABABAB"
    compressed = lz78_compress(input_str)
    assert isinstance(compressed, list)
    assert len(compressed) < len(input_str)

def test_lz78_end_to_end():
    """Comprehensive end-to-end test of compression and decompression"""
    test_cases = [
        "TOBEORNOTTOBEORTOBEORNOT",
        "hello world",
        "aaaaaaaaaa",
        "abcdefghijklmnop",
        "12345678901234567890"
    ]
    
    for test_str in test_cases:
        compressed = lz78_compress(test_str)
        decompressed = lz78_decompress(compressed)
        assert decompressed == test_str, f"Failed for input: {test_str}"

def test_lz78_compress_error_handling():
    """Test error handling for compression"""
    with pytest.raises(TypeError):
        lz78_compress(123)
    
    with pytest.raises(TypeError):
        lz78_compress(None)
    
    with pytest.raises(ValueError):
        lz78_compress("")

def test_lz78_decompress_error_handling():
    """Test error handling for decompression"""
    with pytest.raises(TypeError):
        lz78_decompress("not a list")
    
    with pytest.raises(ValueError):
        lz78_decompress([(1, 'a'), (99, 'b')])  # Invalid index
    
    with pytest.raises(ValueError):
        lz78_decompress([(1, 123)])  # Invalid tuple format

def test_lz78_empty_compression():
    """Test edge case of near-empty inputs"""
    test_cases = ["a", "b", "1"]
    
    for test_str in test_cases:
        compressed = lz78_compress(test_str)
        decompressed = lz78_decompress(compressed)
        assert decompressed == test_str, f"Failed for input: {test_str}"