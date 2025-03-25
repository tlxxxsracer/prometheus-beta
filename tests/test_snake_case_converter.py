import pytest
from src.snake_case_converter import to_snake_case

def test_camel_case_conversion():
    assert to_snake_case("helloWorld") == "hello_world"
    assert to_snake_case("camelCaseString") == "camel_case_string"

def test_pascal_case_conversion():
    assert to_snake_case("HelloWorld") == "hello_world"
    assert to_snake_case("PascalCaseString") == "pascal_case_string"

def test_kebab_case_conversion():
    assert to_snake_case("hello-world") == "hello_world"
    assert to_snake_case("kebab-case-string") == "kebab_case_string"

def test_space_separated_conversion():
    assert to_snake_case("hello world") == "hello_world"
    assert to_snake_case("  Hello   World  ") == "hello_world"

def test_mixed_case_conversion():
    assert to_snake_case("Hello-World Test") == "hello_world_test"
    assert to_snake_case("snake_Case-Test") == "snake_case_test"

def test_edge_cases():
    assert to_snake_case("") == ""
    assert to_snake_case("a") == "a"
    assert to_snake_case("A") == "a"

def test_special_characters():
    assert to_snake_case("hello!world") == "hello_world"
    assert to_snake_case("hello@world#test") == "hello_world_test"

def test_numbers():
    assert to_snake_case("hello2World") == "hello2_world"
    assert to_snake_case("2helloWorld") == "2_hello_world"

def test_error_handling():
    with pytest.raises(TypeError):
        to_snake_case(None)
    with pytest.raises(TypeError):
        to_snake_case(123)
    with pytest.raises(TypeError):
        to_snake_case(["hello", "world"])