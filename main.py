def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

from stats import count_words, get_character_counts

def main():
    book_text = get_book_text("books/frankenstein.txt")
    num_words = count_words(book_text)
    print(f"Found {num_words} total words")

    character_counts = get_character_counts(book_text)
    print(character_counts)

main()
