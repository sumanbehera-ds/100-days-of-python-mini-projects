# Find Words Longer Than N
def words_longer_than(sentence, length):
    words = sentence.split()

    result = []

    for word in words:
        if len(word) > length:
            result.append(word)

    return result


text = "Python programming improves logical thinking"

answer = words_longer_than(text, 6)

print("Sentence:", text)
print("Long words:", answer)