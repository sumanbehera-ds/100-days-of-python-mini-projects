# Count Character Frequency
def character_frequency(text):
    frequency = {}

    for char in text:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

    return frequency


word = "banana"

result = character_frequency(word)

print("Word:", word)
print("Frequency:", result)