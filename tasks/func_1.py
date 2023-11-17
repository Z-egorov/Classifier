from pathlib import Path
import re
from initial_form import initial
from zeroing import zeroing_file, zeroing


def main_idf(dir_way):

    folder = Path(dir_way)  # переход в папку с файлами
    word_in_files = {}
    how_much_files = 0

    if folder.is_dir():

        for file in folder.iterdir(): # перебор файлов  # перебор файлов
            file = open(file, 'r', encoding='utf-8')

            how_much_files += 1
            words = file.read()
            words = re.findall('[a-zа-яё]+', words, flags=re.IGNORECASE)
            count_words = {}

            tf = {}
            count_for_tf = 0

            file.close()

            for word_ch in words:
                count_for_tf += 1  # подсчёт слов в одном файле для tf

            for word_ch1 in count_words:  # подсчёт idf
                word1 = initial(word_ch1).upper()

                if word1 not in word_in_files and len(word1) > 2:
                    word_in_files.update({word1: 1})

                elif word1 in word_in_files:
                    word_in_files[word1] += 1
