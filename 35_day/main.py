# Find Maximum Occurring Character
def max_occurring_character(text):
    frequency = {}

    for char in text:
        frequency[char] = frequency.get(char, 0) + 1

    max_char = None
    max_count = 0

    for char, count in frequency.items():
        if count > max_count:
            max_char = char
            max_count = count

    return max_char, max_count


print(max_occurring_character("programming"))