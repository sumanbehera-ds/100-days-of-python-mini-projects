def remove_empty_strings(items):
    result = []

    for item in items:
        if item != "":
            result.append(item)

    return result


data = ["Python", "", "Java", "", "SQL"]

cleaned = remove_empty_strings(data)

print("Original:", data)
print("Cleaned:", cleaned)