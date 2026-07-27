def get_book_word_count(text: str) -> int:
    return len(text.split())

def get_book_text(filepath: str) -> str:
     with open(filepath) as file:
         file_content = file.read()
     return file_content

def main() -> str:
    print(f"Found {get_book_word_count(get_book_text("books/frankenstein.txt"))} total words")
         

main()
