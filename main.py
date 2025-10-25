from stats import count_words, get_character_counts, sort_character_counts



def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


def main():
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    book_text = get_book_text("books/frankenstein.txt")
    num_words = count_words(book_text)
    print(f"Found {num_words} total words")

    character_counts = get_character_counts(book_text)

    sorted_chars = sort_character_counts(character_counts)

    print("--------- Character Count -------")
    for item in sorted_chars:
        char = item["char"]
        count = item["num"]
        if char.isalpha():
            print(f"{char}: {count}")
    print("============= END ===============")

main()
