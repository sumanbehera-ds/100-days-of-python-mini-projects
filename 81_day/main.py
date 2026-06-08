def count_lines(text):
    lines = text.split("\n")

    count = 0

    for line in lines:
        count += 1

    return count


paragraph = """Python is simple
Python is powerful
Python is useful"""

answer = count_lines(paragraph)

print("Text:")
print(paragraph)
print("Total lines:", answer)