def get_book_word_count(text: str) -> int:
    return len(text.split())

def get_char_count(text: str) -> dict[str, int]:
        log = dict.fromkeys(list(text.lower()), 0)
        for char in list(text.lower()):
            log[char] += 1
        return log

def sort_on(data: tuple[str, int]) -> int:
    return data[1]

def chars_dict_to_sorted_list(data: dict[str, int]) -> list[tuple[str, int]]:
    values = []
    for key in data:
        values.append((key, data[key])) 
    values = sorted(values, key=sort_on, reverse=True)
    return values
