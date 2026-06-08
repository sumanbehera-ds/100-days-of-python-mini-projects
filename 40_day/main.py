# Find Number of Uppercase and Lowercase Letters
def count_case_letters(text):
    uppercase = 0
    lowercase = 0

    for char in text:
        if char.isupper():
            uppercase += 1
        elif char.islower():
            lowercase += 1

    return uppercase, lowercase


sentence = "Python Is Easy"

upper, lower = count_case_letters(sentence)

print("Uppercase:", upper)
print("Lowercase:", lower)