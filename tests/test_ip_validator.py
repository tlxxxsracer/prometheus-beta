import pytest
from src.ip_validator import is_valid_ip_address

def test_valid_ip_addresses():
    """Test various valid IP addresses"""
    valid_ips = [
        "0.0.0.0",
        "255.255.255.255", 
        "192.168.0.1", 
        "10.0.0.1", 
        "172.16.0.1"
    ]
    for ip in valid_ips:
        assert is_valid_ip_address(ip) == True, f"{ip} should be valid"

def test_invalid_ip_addresses():
    """Test various invalid IP addresses"""
    invalid_ips = [
        # Wrong number of octets
        "192.168.0", 
        "192.168.0.1.2",
        
        # Out of range numbers
        "256.0.0.0", 
        "-1.0.0.0",
        "192.168.0.256",
        
        # Non-numeric
        "a.b.c.d", 
        "192.168.0.abc",
        
        # Leading zeros
        "01.02.03.04",
        
        # Empty strings and non-strings
        "", 
        None,
        123,
        "192.168.0.",  # Trailing dot
        ".192.168.0.1"  # Leading dot
    ]
    for ip in invalid_ips:
        assert is_valid_ip_address(ip) == False, f"{ip} should be invalid"

def test_edge_cases():
    """Test edge case IP addresses"""
    # Boundary values
    assert is_valid_ip_address("0.0.0.0") == True
    assert is_valid_ip_address("255.255.255.255") == True
    
    # Whitespace should not be valid
    assert is_valid_ip_address(" 192.168.0.1 ") == False
    assert is_valid_ip_address("192.168.0.1 ") == False