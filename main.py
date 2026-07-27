from stats import get_book_word_count, get_char_count, chars_dict_to_sorted_list

def get_book_text(filepath: str) -> str:
     with open(filepath, "r+", encoding="utf-8") as file:
         file_content = file.read()
     return file_content

def main() -> str:
    characters = get_char_count(get_book_text("books/frankenstein.txt"))
    data = chars_dict_to_sorted_list(characters)
    print(f"Found {get_book_word_count(get_book_text("books/frankenstein.txt"))} total words", characters, data)
         

main()
