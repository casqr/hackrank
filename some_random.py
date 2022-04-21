def main():
    file = input('File name: ')
    word_list = get_dict(file)

    print(f'These are words: {list(word_list.keys())}')

    sent = input("Type your sentence: ")
    if find_words(sent, word_list) is None:
        print('Sorry No words found in the database')
    else:
        print(f'Words and their synonym found in your sentence are: {find_words(sent, word_list)}')
        th = input('Would you like to replace it to one of the synonyms above? ')

        if th == 'yes':
            n = int(input(f'Which word would u like to replace it with from 1-3 pick a position that describes the '
                          f'word: '
                          f' {find_words(sent, word_list)[1]}: '))
            # print(find_synWords(find_words(sent, word_list), n))
            print(display_synWords(sent, find_words(sent, word_list)[0], find_synWords(find_words(sent, word_list), n)))


def get_dict(file_name):
    words = dict()
    try:
        with open(file_name) as f:
            for i in f:
                c = i.split()
                words[c[0]] = c[1:]
        return words

    except FileNotFoundError:
        file_n = input('Please input the correct file name again: ')
        file_name = file_n
        with open(file_name) as f:
            for i in f:
                c = i.split()
                words[c[0]] = c[1:]
            return words


def find_words(userSent, synDict):
    for i in userSent.split():
        if i in synDict.keys():
            return i, synDict[i]


def find_synWords(tup, userNumber):
    synonym = tup[1]
    return synonym[userNumber - 1]


def display_synWords(userSent, Word, synWord):
    sent = userSent.split()
    updated_sent = sent.index(Word)
    sent[updated_sent] = synWord
    return ' '.join(sent)


if __name__ == '__main__':
    main()
