def translation(text):
    vowels = "aeiouAEIOU"
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    translated = ""
    counter = 0
    while counter < len(text):
        char = text[counter]
        if char in vowels:
            counter += 3
            translated += char
        elif char in consonants:
            counter += 2
            translated += char
        else:
            counter += 1
            translated += char
    return translated


preklad = translation("hieeelalaooo")
preklad2 = translation("hoooowe yyyooouuu duoooiiine")
preklad3 = translation("aaa bo cy da eee fe")
preklad4 = translation("sooooso aaaaaaaaa")
print(preklad)
print(preklad2)
print(preklad3)
print(preklad4)


def reverse_translation(text):
    import random
    vowels = "aeiouAEIOU"
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    encoded = ""
    counter = 0
    while counter < len(text):
        char = text[counter]
        if char in vowels:
            encoded += char*3
            counter += 1
        elif char in consonants:
            encoded += char
            encoded += random.choice(vowels)
            counter += 1
        else:
            encoded += char
            counter += 1
    return encoded


zakodovane = reverse_translation("hello")
print(zakodovane)
prekladfinal = translation(zakodovane)
print(prekladfinal)

        