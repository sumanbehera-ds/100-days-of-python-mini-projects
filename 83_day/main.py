def contains_only_digits(text):
    if len(text) == 0:
        return False

    for char in text:
        if not char.isdigit():
            return False

    return True


value = "123456"

result = contains_only_digits(value)

print("Value:", value)
print("Only digits:", result)