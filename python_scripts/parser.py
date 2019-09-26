import re


def parser(text, key):
    return_list = []
    remove_list = ["@", "#", ",", ";", "."]

    word_list = text.split(" ")

    for word in word_list:
        if(word[0] == key):
            for remove_item in remove_list:
                remove_index = word.find(remove_item, 1)
                if(remove_index != -1):
                    word = word[:remove_index]
            return_list.append(word[1:])

    return return_list


def parser2(text, key):
    return_list = []
    word_list = re.findall("{}\w+".format(key), text)
    for word in word_list:
        return_list.append(word[1:])

    return return_list
