# Find Longest Word
def find_longest_word(sentence):
    words = sentence.split()

    longest = ""

    for word in words:
        if len(word) > len(longest):
            longest = word

    return longest


text = "Machine learning creates intelligent applications"

answer = find_longest_word(text)

print("Sentence:", text)
print("Longest word:", answer)