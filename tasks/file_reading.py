from pathlib import Path
import re
from initial_form import initial
from zeroing import zeroing_file, zeroing


def main_idf(dir_way):
    zeroing_file()
    zeroing("idf.txt")

    folder = Path(dir_way) #переход в папку с файлами
    count_all_words = {}
    words_in_files = {}
    how_much_files = 0

    if folder.is_dir():

        for file in folder.iterdir(): # перебор файлов
            file = open(file, 'r', encoding='utf-8')

            how_much_files += 1
            words = file.read()
            words = re.findall('[a-zа-яё]+', words, flags=re.IGNORECASE)
            count_words = {}
            name = Path(file.name).stem
            tf = {}
            count_for_tf = 0

            file.close()

            res_file_name = 'output_docs/' + name + '.txt'

            for word_ch in words:
                word = initial(word_ch).upper()

                if word not in count_words and len(word) > 2:
                    count_words.update({word: 1})
                    count_all_words.update({word: 1})

                elif word in count_words:
                    count_words[word] += 1
                    count_all_words[word] += 1

                count_for_tf += 1

            for word in count_words:

                if word not in words_in_files and len(word) > 2:
                    words_in_files.update({word: 1})

                elif word in words_in_files:
                    words_in_files[word] += 1

            result = open(res_file_name, "w+")
            for keys in count_words:
                result.write(keys + ' ' + str(count_words[keys]) + '\n')

            result.close()

    idf_file = open("idf.txt", "w+", encoding="utf-8")

    for i in words_in_files:
        idf_file.write(i + ' ' + str((words_in_files[i])/(how_much_files)) + "\n")

