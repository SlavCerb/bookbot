def get_word_count(book_path):
    with open(book_path) as file:
        file_contents = file.read()
        words = file_contents.split()
        print(len(words))

def main():
    get_word_count("books/13 - Text - Frankenstein.txt")

main()