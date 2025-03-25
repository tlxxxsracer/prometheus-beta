import pytest
import lzma
from src.xz_compression import compress_with_xz, decompress_with_xz

def test_compress_string():
    text = "Hello, world! This is a test of XZ compression."
    compressed = compress_with_xz(text)
    assert isinstance(compressed, bytes)
    assert len(compressed) > 0
    assert compressed != text.encode('utf-8')

def test_decompress_string():
    text = "Hello, world! This is a test of XZ compression."
    compressed = compress_with_xz(text)
    decompressed = decompress_with_xz(compressed)
    assert decompressed.decode('utf-8') == text

def test_compress_bytes():
    data = b'\x00\x01\x02\x03\x04'
    compressed = compress_with_xz(data)
    assert isinstance(compressed, bytes)
    assert len(compressed) > 0
    assert compressed != data

def test_decompress_bytes():
    data = b'\x00\x01\x02\x03\x04'
    compressed = compress_with_xz(data)
    decompressed = decompress_with_xz(compressed)
    assert decompressed == data

def test_compression_levels():
    text = "Hello, world!" * 100
    for level in range(10):
        compressed = compress_with_xz(text, compression_level=level)
        assert isinstance(compressed, bytes)
        assert len(compressed) > 0

def test_invalid_input_type():
    with pytest.raises(TypeError):
        compress_with_xz(123)
    with pytest.raises(TypeError):
        decompress_with_xz("not bytes")

def test_invalid_compression_level():
    with pytest.raises(ValueError):
        compress_with_xz("test", compression_level=-1)
    with pytest.raises(ValueError):
        compress_with_xz("test", compression_level=10)

def test_invalid_compression_data():
    with pytest.raises(lzma.LZMAError):
        decompress_with_xz(b'invalid compressed data')

def test_roundtrip_compression():
    original_texts = [
        "Short text",
        "Longer text with multiple words and some complexity",
        "",  # Empty string
        "🌍 Unicode characters こんにちは"
    ]

    for text in original_texts:
        compressed = compress_with_xz(text)
        decompressed = decompress_with_xz(compressed)
        assert decompressed.decode('utf-8') == text