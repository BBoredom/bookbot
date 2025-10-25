def count_words(text):
    words = text.split()
    return len(words)

def get_character_counts(text: str) -> dict[str, int]:
    counts: dict[str, int] = {}
    for characters in text.lower():
        counts[characters] = counts.get(characters, 0) + 1
    return counts

def sort_character_counts(char_counts_dict: dict) -> list[dict]:
    char_list = []
    for char, count in char_counts_dict.items():
        char_list.append({"char": char, "num": count})
    def sort_on(dict_item):
        return dict_item["num"]
    char_list.sort(key=sort_on, reverse=True)
    return char_list