def reverse_string(text):
    result = ""

    index = len(text) - 1

    while index >= 0:
        result += text[index]
        index -= 1

    return result


word = "python"
reversed_word = reverse_string(word)

print("Original:", word)
print("Reversed:", reversed_word)