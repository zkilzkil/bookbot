# func for number of words in file
def count_words(text):
	return len(text.split())

# func take text from book as string, return num char
def num_char(text):
	lowercase_text = text.lower()
	char_count = {}
	for char in lowercase_text:
		if char in char_count:
			char_count[char] += 1
		else: 
			char_count[char] = 1
	return char_count
