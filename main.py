import sys
from stats import get_num_words, letter_count, sort_letters

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def print_report(book):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(get_book_text(book))} total words")
    print("--------- Character Count -------")
    for item in sort_letters(letter_count(get_book_text(book))):
        print(f"{item[0][0]}: {item[1]}")
    print("============= END ===============")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book = sys.argv[1]
    print_report(book)




if __name__ == "__main__":
    main()