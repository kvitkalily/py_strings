import pytest

from py_strings import *


def test_reverse():
    assert reverse("abcd") == "dcba"


def test_first_to_upper():
    assert first_to_upper("abcd") == "Abcd"
    assert first_to_upper("litwo oJCZYZNO MoJa") == "Litwo OJCZYZNO Moja"


def test_count_vowels():
    assert count_vowels("abcdef") == 2
    assert count_vowels("AbcdeF") == 2
    assert count_vowels("XYZ") == 1
    assert count_vowels("XZ") == 0


def test_sum_digits():
    assert sum_digits("It's 911, what is your emergency?") == 11
    assert sum_digits("3... 2... 1... kaboom!") == 6
    assert sum_digits("Failure is not an option") == 0


def test_search_substr():
    assert search_substr("Litwo, Ojczyzno moja", "wo") == 3
    assert search_substr("Litwo, Ojczyzno moja", "wa") == None
