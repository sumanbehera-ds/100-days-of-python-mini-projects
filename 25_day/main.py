# Count Words in Sentence
def count_words(sentence):
    words = sentence.split()

    count = 0

    for word in words:
        count += 1

    return count


text = "Python is useful for data science"

word_count = count_words(text)

print("Sentence:", text)
print("Word count:", word_count)