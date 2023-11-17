from pathlib import Path
import zeroing
import os
import lang
import re
import delpred
import sys

zeroing.zeroing_file('result.txt')
zeroing.zeroing_folder('task1')

path = os.getcwd()
folder = Path(path + '/data/docs/')
theme = Path(path + '/data/themes/')

for file_doc in folder.iterdir():  # перебор файлов  # перебор файлов
    file_doc = open(file_doc, 'r', encoding='utf-8')
    words_in_one_file = file_doc.read()
    words_in_one_file = re.findall('[a-zа-яё]+', words_in_one_file, flags=re.IGNORECASE)
    functors_pos = {'INTJ', 'PRCL', 'CONJ', 'PREP', 'ADVB', 'NPRO'}
    words_in_one_file = ([word1 for word1 in words_in_one_file if delpred.pos(word1) not in functors_pos])
    word_in_file = {}

    for word in words_in_one_file:  # подсчёт idf
        word = lang.initial(word).upper()

        if word not in word_in_file:
            word_in_file.update({word: 1})

        elif word in word_in_file:
            word_in_file[word] += 1

    f = open('task1/'+ str(os.path.basename(file_doc.name)) + '.txt', 'w', encoding='utf-8')

    for j in word_in_file:
        f.write(j + ' ' + str(word_in_file[j]) + '\n')
    f.close()

    nam = '1.txt'

    mTheme = 0

    for file_theme in theme.iterdir():  # перебор файлов  # перебор файлов
        file_theme = open(file_theme, 'r', encoding='utf-8')
        words_in_one_file_theme = file_theme.read().split(' ')

        word_in_file_theme = {}

        for word in words_in_one_file_theme:  # подсчёт idf
            word = lang.initial(word).upper()

            if word not in word_in_file_theme:
                word_in_file_theme.update({word: 1})

            elif word in word_in_file_theme:
                word_in_file_theme[word] += 1

        m = 0



        for i in word_in_file:
            if i in word_in_file_theme:
                m += word_in_file[i] * word_in_file_theme[i]



        if m > mTheme:
            mTheme = m
            nam = (os.path.basename(file_theme.name))+'.txt'



    result = open('result.txt', 'a', encoding='utf-8')
    result.write(str(os.path.basename(file_doc.name)) + '.txt' + ' ' + nam + '\n')
    result.close()


