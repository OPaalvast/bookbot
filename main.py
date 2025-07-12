from stats import get_num_words, count_characters, sort_dictionary
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()

    return file_contents


if __name__ == "__main__":

    args = sys.argv
    if len(args) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        file_path = args[1]

        file_contents = get_book_text(file_path)
        dictionary = count_characters(file_contents)
        sorted_dictionary_list = sort_dictionary(dictionary)

        print(f"Found {get_num_words(file_contents)} total words")
        print(f"{count_characters(file_contents)}")
        for line in sorted_dictionary_list:
            print(f"{line['char']}: {line['num']}")