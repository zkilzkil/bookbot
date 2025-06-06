# read file
def get_book_text(filepath):
	with open(filepath) as f: 
		filecontents = f.read()
		return filecontents
# func for number of words in file
def count_words(text):
	return len(text.split())
# execute program
def main():
	text = get_book_text("books/frankenstein.txt")
	num_words = count_words(text)
	print(f"{num_words} words found in the document")
#	print(get_book_text("books/frankenstein.txt"))
main()
