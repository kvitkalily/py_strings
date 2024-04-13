# pylint: disable=C0114
import string

#1 zadanie
def reverse(text: str) -> str:

    return text[::-1]
#2 zadanie
def first_to_upper(text: str) -> str:
	newznak = ""
	first_letter = True
	for indeks in text:
		if indeks in string.whitespace or indeks in string.punctuation:
			newznak += indeks 
			first_letter = True
			continue		
		if indeks in string.digits:
			newznak += indeks
			first_letter = False
			continue	
		if indeks.islower() and first_letter:
			newznak += indeks.upper()
			first_letter = False
			continue			
		newznak += indeks      							
		first_letter = False
	return newznak
	
	
def count_vowels(text: str) -> int:
	vowels = 0
	l = len(text)
	for i in range (l):
		if text[i] in "ĄAEĘUOÓIYyaąeęóuio":#na linuksie nie mam dostepu do polskich znakow, więc ich wpisałam z gita w telefonie
			vowels +=1
	return vowels


def sum_digits(text: str) -> int:
	total = 0
	for i in text:
		if i.isdigit():#sprawdzamy znaczek i czy jest cyfra - isdigit.
			total += int(i) #konwertujemy w liczbe calkowita
	return total


def search_substr(text: str, sub: str) -> int:
	c = text.find(sub) #indeks tego wyrazu
	if c == -1:
		print("None")
	else: return c
	
