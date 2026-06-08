def separate_letters_digits(text):
    letters = ""
    digits = ""

    for char in text:
        if char.isalpha():
            letters += char
        elif char.isdigit():
            digits += char

    return letters, digits


data = "abc123def456"

alphabets, numbers = separate_letters_digits(data)

print("Letters:", alphabets)
print("Digits:", numbers)