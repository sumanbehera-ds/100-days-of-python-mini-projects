def capitalize_words(sentence):
    words = sentence.split()

    result = []

    for word in words:
        first_letter = word[0].upper()
        remaining_letters = word[1:].lower()
        new_word = first_letter + remaining_letters
        result.append(new_word)

    final_sentence = " ".join(result)

    return final_sentence


text = "python programming language"

print(capitalize_words(text))