def parser(text, key):
    return_list = []

    word_list = text.split(" ")

    for word in word_list:
        if(word[0] == key):
            word = word.replace(',', '')
            word = word.replace('.', '')
            word = word.replace(';', '')
            return_list.append(word[1:])

    return return_list
