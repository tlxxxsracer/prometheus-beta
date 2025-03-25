import lzma
import typing

def compress_with_xz(data: typing.Union[str, bytes], compression_level: int = 6) -> bytes:
    """
    Compress input data using XZ compression algorithm.

    Args:
        data (str or bytes): The data to compress
        compression_level (int, optional): Compression level from 0-9. Defaults to 6.

    Returns:
        bytes: Compressed data

    Raises:
        TypeError: If input is not str or bytes
        ValueError: If compression level is not between 0-9
    """
    # Input validation
    if not isinstance(data, (str, bytes)):
        raise TypeError("Input must be str or bytes")
    
    if compression_level < 0 or compression_level > 9:
        raise ValueError("Compression level must be between 0 and 9")

    # Convert str to bytes if necessary
    if isinstance(data, str):
        data = data.encode('utf-8')

    # Compress using lzma
    compressed_data = lzma.compress(data, preset=compression_level)
    
    return compressed_data

def decompress_with_xz(compressed_data: bytes) -> bytes:
    """
    Decompress XZ compressed data.

    Args:
        compressed_data (bytes): The data to decompress

    Returns:
        bytes: Decompressed data

    Raises:
        TypeError: If input is not bytes
        lzma.LZMAError: If data cannot be decompressed
    """
    # Input validation
    if not isinstance(compressed_data, bytes):
        raise TypeError("Input must be bytes")

    # Decompress using lzma
    try:
        decompressed_data = lzma.decompress(compressed_data)
    except lzma.LZMAError as e:
        raise lzma.LZMAError(f"Failed to decompress data: {e}")
    
    return decompressed_data