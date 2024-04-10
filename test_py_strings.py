import pytest

from py_strings import *


def test_reverse():
    data = (
        ("abc", "cba"),
        ("xZz qwe", "ewq zZx"),
        ("xZz\nqwe", "ewq\nzZx"),
        ("xZz\tqwe", "ewq\tzZx"),
        ("Litwo, ojczyzno moja", "ajom onzyzcjo ,owtiL"),
        ("łabudibu łabidudaj ą ę ó ń", "ń ó ę ą jadudibał ubidubał"),
    )

    for d in data:
        assert reverse(d[0]) == d[1], f"input: {d[0]}"


def test_first_to_upper():
    data = (
        ("abc", "Abc"),
        ("xZz qwe", "XZz Qwe"),
        ("xZz\nqwe", "XZz\nQwe"),
        ("xZz\tqwe", "XZz\tQwe"),
        ("Litwo, ojczyzno moja", "Litwo, Ojczyzno Moja"),
        ("bielsko-biała", "Bielsko-Biała"),
        ("raz.dwa,trzy;cztery", "Raz.Dwa,Trzy;Cztery"),
        ("łabudibu łabidudaj ą ę ó ń", "Łabudibu Łabidudaj Ą Ę Ó Ń"),
        ("997zgłoś się", "997zgłoś Się"),
    )

    for d in data:
        assert first_to_upper(d[0]) == d[1], f"input: {d[0]}"


def test_count_vowels():
    data = (
        ("abc", 1),
        ("xZz", 0),
        ("xZz\nqwe", 1),
        ("Litwo, ojczyzno moja", 7),
        ("łabudibu łabidudaj ą ę ó ń", 11),
        ("ŁABUDIBU ŁABIDUDAJ Ą Ę Ó Ń", 11),
    )

    for d in data:
        assert count_vowels(d[0]) == d[1], f"input: {d[0]}"


def test_sum_digits():
    data = (
        ("abc", 0),
        ("xZz", 0),
        ("Countdown: 3... 2... 1... Start!", 6),
        ("First prime numbers are: 3, 5, 7, 11, 13", 21),
        ("Fiłst płime numbełs are: 3, 5, 7, 11, 13", 21),
    )

    for d in data:
        assert sum_digits(d[0]) == d[1], f"input: {d[0]}"


def test_search_substr():
    data = (
        ("abc", "d", None),
        ("xZz", "z", 2),
        ("Litwo, ojczyzno moja", "ojcz", 7),
        ("First prime numbers are: 3, 5, 7, 11, 13", "3", 25),
        ("łabudibu łabidudaj ą ę ó ń", "łabi", 9),
        ("łabudibu łabidudaj ą ę ó ń", "abi", 10),
        ("abcde", "abcdefgh", None),
    )

    for d in data:
        assert search_substr(d[0], d[1]) == d[2], f"inputs: {d[0]} {d[1]}"
