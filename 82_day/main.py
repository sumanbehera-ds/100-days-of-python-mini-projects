def ascii_values(text):
    result = {}

    for char in text:
        value = ord(char)
        result[char] = value

    return result


word = "Python"

answer = ascii_values(word)

print("Word:", word)
print("ASCII values:", answer)