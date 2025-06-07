def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    text = text.lower()
    char_counts = {}
    for char in text:
        char_counts[char] = char_counts.get(char, 0) + 1
    return char_counts

def sort_on(dict):
    return dict["num"]

def sort_characters(char_counts):
    sorted_list = []
    for char, count in char_counts.items():
        if char.isalpha():
            sorted_list.append({"char": char, "num": count})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
