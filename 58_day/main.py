# Count Special Characters
def count_special_characters(text):
    count = 0

    for char in text:
        if not char.isalnum() and not char.isspace():
            count += 1

    return count


sentence = "Hello@Python#2026!"

answer = count_special_characters(sentence)

print("Text:", sentence)
print("Special characters:", answer)