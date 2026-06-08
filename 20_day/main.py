#  Count Vowels in a String
def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0

    for char in text:
        if char in vowels:
            count += 1

    return count


sentence = "Data Science is powerful"

total_vowels = count_vowels(sentence)

print("Sentence:", sentence)
print("Vowels:", total_vowels)