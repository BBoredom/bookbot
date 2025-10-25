def count_words(text):
    words = text.split()
    return len(words)

def get_character_counts(text: str) -> dict[str, int]:
    counts: dict[str, int] = {}
    for characters in text.lower():
        counts[characters] = counts.get(characters, 0) + 1
    return counts

