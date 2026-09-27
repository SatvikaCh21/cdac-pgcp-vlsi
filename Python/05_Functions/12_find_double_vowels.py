def find_double_vowels(word):
    vowels = "aeiou"
    result = []

    for i in range(len(word) - 1):
        if word[i].lower() in vowels and word[i + 1].lower() in vowels:
            pair = word[i] + word[i + 1]
            result.append(pair)
    return result

# Ask the user to enter a word
word = input("Enter a word: ")
print(find_double_vowels(word))