def get_word_count(book_path):
    with open(book_path) as file:
        file_contents = file.read()
        words = file_contents.split()
        # print(len(words))
        return len(words)

def get_letter_count(book_path):
    with open(book_path) as file:
        file_contents = file.read()
        file_contents = file_contents.lower()
        letter_dictionary = {}
        for char in file_contents:
            if char not in letter_dictionary.keys():
                letter_dictionary[char] = file_contents.count(char)
        # print(letter_dictionary)
        return letter_dictionary

def get_report(book_path):
    word_count = get_word_count(book_path)
    let_dic = get_letter_count(book_path)

    # Checks the dictionary for characters in the alphabet and discards the rest
    alpha_dic = {}
    for char in let_dic:
        if char.isalpha():
            alpha_dic[char] = let_dic[char]
    # print(alpha_dic)

    # Sorts the items of the dictionary by value
    sorted_dic = dict(sorted(alpha_dic.items(), key=lambda item: item[1], reverse = True))
    # print(sorted_dic)
    
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document")
    print()
    for char in sorted_dic:
        print(f"The '{char}' character was found {sorted_dic[char]} times")
    print("--- End report ---")

def main():
    get_report("books/frankenstein.txt")

main()