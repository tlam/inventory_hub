def capwords(s):
    word_list = s.split(' ')
    cap_word_list = []
    for word in word_list:
        cap_word_list.append(word.capitalize())

    return ' '.join(cap_word_list)
