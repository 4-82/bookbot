def get_book_text(filepath: str) -> str:
     with open(filepath) as file:
         file_content = file.read()
     return file_content

def main() -> str:
    print(get_book_text("books/frankenstein.txt"))
         

main()
