def mask_credit_card(text):
    words = text.split()
    result = []
    for word in words:
        stripped = word.strip(".,!?")
        blocks = stripped.split("-")
        if len(blocks) == 4 and all(len(b) == 4 and b.isdigit() for b in blocks):
            masked = "XXXX-XXXX-XXXX-" + blocks[3]
            trailing_punct = word[len(stripped):]
            result.append(masked + trailing_punct)
        else:
            result.append(word)
    return " ".join(result)

text = "My card number is 1234-5678-9012-3456."
print(mask_credit_card(text))