def get_book_text(filepath):
    with open(filepath) as f:
        text = f.read()
        return text

def main():
    book_text = get_book_text("books/frankenstein.txt")
    print(book_text)

main()
