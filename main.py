import sys
from stats import get_book_word_count, get_char_count, chars_dict_to_sorted_list

def get_book_text(filepath: str) -> str:
     with open(filepath, "r+", encoding="utf-8") as file:
         file_content = file.read()
     return file_content

def print_report(text: str, count: int, sorted_char_count: list[tuple[str, int]]) -> str:
    string_result = ""
    for data in sorted_char_count:
        if data[0].isalpha() == False:
            continue
        string_result += f"{data[0]}: {data[1]}\n"
        
    print(f"============ BOOKBOT ============\nAnalyzing book found at {text}...\n----------- Word Count ----------\nFound {count} total words\n--------- Character Count -------\n{string_result}============= END ===============")

def main() -> str:
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    print_report(sys.argv[1], get_book_word_count(get_book_text(sys.argv[1])), chars_dict_to_sorted_list(get_char_count(get_book_text(sys.argv[1]))))
main()
