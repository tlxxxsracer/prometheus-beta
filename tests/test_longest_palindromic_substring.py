import pytest
from src.longest_palindromic_substring import longest_palindromic_substring

def test_empty_string():
    """Test empty string input"""
    assert longest_palindromic_substring("") == ""

def test_single_character():
    """Test single character input"""
    assert longest_palindromic_substring("a") == "a"

def test_palindrome_whole_string():
    """Test when entire string is a palindrome"""
    assert longest_palindromic_substring("racecar") == "racecar"

def test_multiple_palindromes():
    """Test when multiple palindromes exist"""
    assert longest_palindromic_substring("babad") in ["bab", "aba"]

def test_even_length_palindrome():
    """Test even-length palindrome"""
    assert longest_palindromic_substring("abba") == "abba"

def test_mixed_palindromes():
    """Test a string with multiple palindromic substrings"""
    assert longest_palindromic_substring("forgeeksskeegfor") == "geeksskeeg"

def test_no_palindrome_longer_than_one():
    """Test string with no palindrome longer than one character"""
    assert longest_palindromic_substring("abc") in ["a", "b", "c"]

def test_repeated_characters():
    """Test string with repeated characters"""
    assert longest_palindromic_substring("aaaaaa") == "aaaaaa"

def test_complex_palindrome():
    """Test a more complex palindrome scenario"""
    assert longest_palindromic_substring("cbbd") == "bb"

def test_long_string():
    """Test a longer string with multiple palindromes"""
    long_str = "civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavetakenthatcityofGettysburgasafinaintlrestaingtplaceFotrhosewhoheregavetheirlivesthatlastwefullnrevolutionhavingintheirmindshowtheycameheresua@dediicatetoparculiarparetheirownlongago&ccmemotryWEcannordedicewecaxnnothallowthisgroundtobealterformundertheultimateinexorableprocessofhistorythecitadelofhumancivilizationmustbedefendedorelsewefallintomeaninglessruinLoremipsumdolorsitametconsecteturadipiscingelitseddoeiusmodtemporincididuntlaboreetdolmagnaaliquaUtenimnullam" 
    assert len(longest_palindromic_substring(long_str)) > 0