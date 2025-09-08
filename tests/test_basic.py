import pytest
from textlib import reverse, count_vowels, is_palindrome, to_upper, concat


# ----------------------------
# reverse
# ----------------------------
def test_reverse_happy_path():
    assert reverse("hola") == "hola"
    assert reverse("12345") == "54321"

def test_reverse_empty_string():
    assert reverse("") == ""

def test_reverse_type_error():
    with pytest.raises(TypeError):
        reverse(123)  # no es str


# ----------------------------
# count_vowels
# ----------------------------
def test_count_vowels_happy_path():
    assert count_vowels("hola") == 2        # o, a
    assert count_vowels("Pingüino rápido") == 7  # i,u,i,o,a,i,o

def test_count_vowels_no_vowels():
    assert count_vowels("rhythm") == 0

def test_count_vowels_type_error():
    with pytest.raises(TypeError):
        count_vowels(123)


# ----------------------------
# is_palindrome
# ----------------------------
def test_is_palindrome_happy_path():
    assert is_palindrome("oso")
    assert is_palindrome("¿Acaso hubo búhos acá?")  # ignora acentos, espacios y signos

def test_is_palindrome_not_palindrome():
    assert not is_palindrome("hola")

def test_is_palindrome_type_error():
    with pytest.raises(TypeError):
        is_palindrome(123)


# ----------------------------
# to_upper
# ----------------------------
def test_to_upper_happy_path():
    assert to_upper("hola") == "HOLA"
    assert to_upper("mañana") == "MAÑANA"

def test_to_upper_empty():
    assert to_upper("") == ""

def test_to_upper_type_error():
    with pytest.raises(TypeError):
        to_upper(123)


# ----------------------------
# concat
# ----------------------------
def test_concat_happy_path():
    assert concat("ab", "cd") == "abcd"
    assert concat("hola", " mundo") == "hola mundo"

def test_concat_empty_strings():
    assert concat("", "") == ""

def test_concat_type_error():
    with pytest.raises(TypeError):
        concat("a", 123)
