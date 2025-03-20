import pytest
import re
from src.verification_code import VerificationCodeGenerator

def test_generate_code():
    """Test that generate_code returns a valid 6-digit code."""
    generator = VerificationCodeGenerator()
    code = generator.generate_code()
    
    # Check code length
    assert len(code) == 6, "Code should be 6 digits long"
    
    # Check code contains only digits
    assert code.isdigit(), "Code should contain only digits"

def test_code_uniqueness():
    """Test that generated codes are unique."""
    generator = VerificationCodeGenerator()
    generated_codes = set()
    
    # Generate multiple codes
    for _ in range(100):
        code = generator.generate_code()
        assert code not in generated_codes, "Generated code should be unique"
        generated_codes.add(code)

def test_validate_code():
    """Test code validation."""
    generator = VerificationCodeGenerator()
    
    # Generate a code
    code = generator.generate_code()
    
    # Validate the generated code
    assert generator.validate_code(code) == True, "Generated code should be valid"
    
    # Validate an invalid code
    assert generator.validate_code('123456') == False, "Ungenerated code should be invalid"

def test_validate_code_invalid_inputs():
    """Test validation with various invalid inputs."""
    generator = VerificationCodeGenerator()
    
    # Test non-string input
    with pytest.raises(ValueError, match="Code must be a string"):
        generator.validate_code(123456)
    
    # Test non-digit strings
    assert generator.validate_code('abcdef') == False, "Non-digit string should be invalid"
    assert generator.validate_code('12345') == False, "Too short code should be invalid"
    assert generator.validate_code('1234567') == False, "Too long code should be invalid"

def test_invalidate_code():
    """Test code invalidation."""
    generator = VerificationCodeGenerator()
    
    # Generate a code
    code = generator.generate_code()
    
    # Validate the code before invalidation
    assert generator.validate_code(code) == True
    
    # Invalidate the code
    generator.invalidate_code(code)
    
    # Check that the code is no longer valid
    assert generator.validate_code(code) == False
    
    # Try to invalidate an already removed code
    with pytest.raises(ValueError, match="Code not found"):
        generator.invalidate_code(code)