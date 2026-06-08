# Find Shortest Word
def find_shortest_word(sentence):
    words = sentence.split()

    if len(words) == 0:
        return None

    shortest = words[0]

    for word in words:
        if len(word) < len(shortest):
            shortest = word

    return shortest


text = "Python is a powerful language"

print("Shortest word:", find_shortest_word(text))