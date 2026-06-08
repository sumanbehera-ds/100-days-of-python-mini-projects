# Replace Vowels With Star
def replace_vowels(text):
    vowels = "aeiouAEIOU"

    result = ""

    for char in text:
        if char in vowels:
            result += "*"
        else:
            result += char

    return result


sentence = "Data Science"

print(replace_vowels(sentence))