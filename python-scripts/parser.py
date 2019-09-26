def parser(text, key):
    return_list = []

    word_list = text.split(" ")

    for word in word_list:
        if(word[0] == key):
            at_index = word.find("@", 1, len(word)-1)
            if(at_index != -1):
                word = word[:at_index]
            word = word.replace(',', '')
            word = word.replace('.', '')
            word = word.replace(';', '')
            return_list.append(word[1:])

    return return_list

text = "pomeon@liu,,,#bicudo"

print(parser(text, "@"))