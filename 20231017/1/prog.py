def count_letter_pairs(text):
    pairs = {}
    for i in range(len(text) - 1):
        if text[i].isalpha() and text[i + 1].isalpha():
            pair = (text[i].lower(), text[i + 1].lower())
            if pair in pairs:
                pairs[pair] += 1
            else:
                pairs[pair] = 1
    return len(pairs)

print(count_letter_pairs(input()))
