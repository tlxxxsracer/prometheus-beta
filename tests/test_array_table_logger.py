import pytest
from src.array_table_logger import log_array_table

def test_log_array_table_basic():
    """Test basic functionality with default index headers"""
    arr = [1, 2, 3]
    expected_output = (
        "0  | 1  | 2  \n"
        "---------------\n"
        "1  | 2  | 3  "
    )
    assert log_array_table(arr).replace(' ', '') == expected_output.replace(' ', '')

def test_log_array_table_with_headers():
    """Test functionality with custom headers"""
    arr = [1, 2, 3]
    headers = ['A', 'B', 'C']
    expected_output = (
        "A  | B  | C  \n"
        "---------------\n"
        "1  | 2  | 3  "
    )
    assert log_array_table(arr, headers).replace(' ', '') == expected_output.replace(' ', '')

def test_log_array_table_mixed_types():
    """Test with mixed types of data"""
    arr = [1, 'two', 3.14]
    headers = ['Number', 'String', 'Float']
    expected_output = (
        "Number | String | Float\n"
        "------------------------\n"
        "1      | two    | 3.14 "
    )
    assert log_array_table(arr, headers).replace(' ', '') == expected_output.replace(' ', '')

def test_log_array_table_error_invalid_input():
    """Test error handling for non-list input"""
    with pytest.raises(TypeError, match="Input must be a list"):
        log_array_table("not a list")

def test_log_array_table_error_header_mismatch():
    """Test error handling for header length mismatch"""
    with pytest.raises(ValueError, match="Number of headers must match array length"):
        log_array_table([1, 2, 3], ['A', 'B'])

def test_log_array_table_empty_list():
    """Test handling of empty list"""
    assert log_array_table([]) == ''
    assert log_array_table([], []) == ''