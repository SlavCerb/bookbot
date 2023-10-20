def get_word_count(book_path):
    with open(book_path) as file:
        file_contents = file.read()
        words = file_contents.split()
        print(len(words))

def get_letter_count(book_path):
    with open(book_path) as file:
        file_contents = file.read()
        file_contents = file_contents.lower()
        letter_dictionary = {}
        for char in file_contents:
            if char not in letter_dictionary.keys():
                letter_dictionary[char] = file_contents.count(char)
        print(letter_dictionary)

def main():
    get_word_count("books/13 - Text - Frankenstein.txt")
    get_letter_count("books/13 - Text - Frankenstein.txt")

main()