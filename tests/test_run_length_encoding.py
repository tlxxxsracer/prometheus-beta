import pytest
from src.run_length_encoding import run_length_encode, run_length_decode

def test_run_length_encode_string():
    """Test RLE encoding with a string input"""
    input_data = "AABBBCCCC"
    expected = [(2, 'A'), (3, 'B'), (4, 'C')]
    assert run_length_encode(input_data) == expected

def test_run_length_encode_list():
    """Test RLE encoding with a list input"""
    input_data = [1, 1, 2, 2, 2, 3, 3, 3, 3]
    expected = [(2, 1), (3, 2), (4, 3)]
    assert run_length_encode(input_data) == expected

def test_run_length_encode_empty():
    """Test RLE encoding with empty input"""
    assert run_length_encode([]) == []
    assert run_length_encode("") == []

def test_run_length_encode_single_item():
    """Test RLE encoding with single item"""
    assert run_length_encode([42]) == [(1, 42)]
    assert run_length_encode("X") == [(1, 'X')]

def test_run_length_encode_invalid_input():
    """Test RLE encoding with invalid input types"""
    with pytest.raises(TypeError):
        run_length_encode(123)
    with pytest.raises(TypeError):
        run_length_encode(None)

def test_run_length_decode_string():
    """Test RLE decoding with a list of tuples"""
    input_data = [(2, 'A'), (3, 'B'), (4, 'C')]
    expected = ['A', 'A', 'B', 'B', 'B', 'C', 'C', 'C', 'C']
    assert run_length_decode(input_data) == expected

def test_run_length_decode_list():
    """Test RLE decoding with a list of number tuples"""
    input_data = [(2, 1), (3, 2), (4, 3)]
    expected = [1, 1, 2, 2, 2, 3, 3, 3, 3]
    assert run_length_decode(input_data) == expected

def test_run_length_decode_empty():
    """Test RLE decoding with empty input"""
    assert run_length_decode([]) == []

def test_run_length_decode_invalid_input():
    """Test RLE decoding with invalid inputs"""
    with pytest.raises(TypeError):
        run_length_decode(123)
    with pytest.raises(TypeError):
        run_length_decode(None)
    with pytest.raises(ValueError):
        run_length_decode([(0, 'A')])
    with pytest.raises(ValueError):
        run_length_decode([(-1, 'B')])

def test_encode_decode_roundtrip():
    """Test complete encode-decode roundtrip for various inputs"""
    test_cases = [
        [1, 1, 2, 2, 2, 3, 3, 3, 3],
        ['A', 'A', 'B', 'B', 'B', 'C', 'C', 'C'],
        [42],
        ['X']
    ]
    
    for case in test_cases:
        encoded = run_length_encode(case)
        decoded = run_length_decode(encoded)
        assert decoded == case