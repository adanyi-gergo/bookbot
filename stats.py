def get_word_count(book):
    splited_book = book.split()
    return f"Found {len(splited_book)} total words"


def get_num_char(book):
    char_count = {}
    book = book.lower()
    for char in book:
        if char not in char_count.keys():
            char_count[char] = book.count(char)
            book.replace(char, "")

    return char_count


def sort_dict(characters):
    transformed_char_list = []
    for key, value in characters.items():
        transformed_char_list.append({
            "name": key,
            "num": value
        })
    transformed_char_list.sort(reverse=True, key=sort_on)

    return transformed_char_list


def sort_on(characters):
    return characters["num"]