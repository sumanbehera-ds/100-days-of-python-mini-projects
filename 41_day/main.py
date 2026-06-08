# Remove Spaces From String
def remove_spaces(text):
    result = ""

    for char in text:
        if char != " ":
            result += char

    return result


sentence = "Python is very useful"

cleaned = remove_spaces(sentence)

print("Original:", sentence)
print("Without spaces:", cleaned)