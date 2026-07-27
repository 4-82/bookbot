def get_book_word_count(text: str) -> int:
    return len(text.split())

def get_char_count(text: str) -> dict[str, int]:
        log = dict.fromkeys(list(text.lower()), 0)
        for char in list(text.lower()):
            log[char] += 1
        return log

