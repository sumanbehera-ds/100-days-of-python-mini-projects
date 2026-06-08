# Flatten a Nested List
def flatten_list(nested_list):
    flat = []

    for item in nested_list:
        if isinstance(item, list):
            for value in item:
                flat.append(value)
        else:
            flat.append(item)

    return flat


data = [1, [2, 3], 4, [5, 6]]

result = flatten_list(data)

print("Original:", data)
print("Flattened:", result)