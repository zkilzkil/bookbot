# import stats.py
from stats import count_words
from stats import num_char

# read file
def get_book_text(filepath):
	with open(filepath) as f: 
		filecontents = f.read()
		return filecontents

# execute program
def main():
	text = get_book_text("books/frankenstein.txt")
	num_words = count_words(text)
	char_count = num_char(text)
	print(char_count)
#	print(f"{num_words} words found in the document")
#	print(get_book_text("books/frankenstein.txt"))
main()
