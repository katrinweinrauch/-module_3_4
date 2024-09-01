def single_root_words(root_word, *other_words):
    same_words = []
    root_word = root_word.lower()
    for element in other_words:
        if root_word in element.lower() or element.lower() in root_word:
            same_words.append(element)
    return same_words


print(single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies'))
print(single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel'))



