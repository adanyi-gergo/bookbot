import sys
from stats import get_word_count, get_num_char, sort_dict

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_uri = sys.argv[1]
    book = get_book_text(book_uri)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_uri}...")
    print("----------- Word Count ----------")
    print(get_word_count(book))
    print("--------- Character Count -------")
    num_of_char = get_num_char(book)
    sorted_chars = sort_dict(num_of_char)
    for item in sorted_chars:
        if item["name"].isalpha():
            print(f"{item["name"]}: {item["num"]}")

main()