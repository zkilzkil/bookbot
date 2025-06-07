import sys
from stats import count_words
from stats import num_char
from stats import sort_char_count

# read file
def get_book_text(filepath):
	with open(filepath) as f: 
		filecontents = f.read()
		return filecontents

# execute program
def main():
	if len(sys.argv) != 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	text = get_book_text(sys.argv[1])
	num_words = count_words(text)
	char_count = num_char(text)
	sorted_count = sort_char_count(char_count)
	sorted_count.reverse()
	
	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {sys.argv[1]}...")
	print("----------- Word Count ----------")
	print(f"Found {num_words} total words")
	print("--------- Character Count -------")
	for item in sorted_count:
		if item["char"].isalpha():
			print(f"{item["char"]}: {item["count"]}")
	print("============= END ===============")
main()
