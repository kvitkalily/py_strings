def reverse(text: str) -> str:

    return text[::-1]


def first_to_upper(text: str) -> str:
	a = text.split()
	c = [word[:1].upper() + word[1:] for word in a] 
	result = ' '.join(c)
	return result #tutaj potknelam. na poczatku kod wygladal tak:    c = text.capitalize()
									#b = c.split()
									#if len(b) >= 2:
									#b[1] = b[1].upper()
									#result = ' '.join(b)
									#return result 
		#ale on tez nie dziala

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
	
