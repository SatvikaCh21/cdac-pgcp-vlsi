def findp(text):
    words = text.split()
    result = []
    for word in words:
        if word.lower().startswith('p') and len(word) >= 3:
            result.append(word)
    return result

sentence = "Python program is FUN!"
words = findp(sentence)
print(words)