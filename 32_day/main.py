# Check Anagram
def is_anagram(word1, word2):
    word1 = word1.lower()
    word2 = word2.lower()

    if len(word1) != len(word2):
        return False

    sorted_word1 = sorted(word1)
    sorted_word2 = sorted(word2)

    return sorted_word1 == sorted_word2


print(is_anagram("listen", "silent"))