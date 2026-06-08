# Find First Non-Repeating Character
def first_non_repeating_char(text):
    frequency = {}

    for char in text:
        frequency[char] = frequency.get(char, 0) + 1

    for char in text:
        if frequency[char] == 1:
            return char

    return None


word = "aabbcde"

answer = first_non_repeating_char(word)

print("Word:", word)
print("First non-repeating character:", answer)